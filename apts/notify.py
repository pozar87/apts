import logging
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Import the config object from the new config module
from .config import config
from .utils import Utils


logger = logging.getLogger(__name__)


class Notify:
    """
    Handles sending email notifications using configured SMTP settings.

    It reads SMTP server details from apts.config ("notification" section).
    Provides methods for sending complex notifications (with plots) and simple emails.
    """

    def __init__(self, recipient_email):
        self.recipient_email = recipient_email
        self.smtp_host = config.get("notification", "smtp_host", fallback=None)
        self.smtp_port = config.getint("notification", "smtp_port", fallback=587)
        self.smtp_user = config.get("notification", "smtp_user", fallback=None)
        self.smtp_password = config.get("notification", "smtp_password", fallback=None)
        self.smtp_use_tls = config.getboolean(
            "notification", "smtp_use_tls", fallback=True
        )
        self.sender_email = config.get("notification", "sender_email", fallback=None)

        if not self.smtp_host or not self.smtp_user:
            logger.warning(
                f"SMTP host ('{self.smtp_host}') or user ('{self.smtp_user}') not configured. Email notifications may fail."
            )

    def _send_email(self, msg):
        """Internal helper to send a MIME message using configured SMTP."""
        try:
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            server.ehlo()
            if self.smtp_use_tls:
                server.starttls()
                server.ehlo()

            if self.smtp_user and self.smtp_password:
                server.login(self.smtp_user, self.smtp_password)

            logger.info(
                f"Sending email to {msg['To']} via {self.smtp_host}:{self.smtp_port}"
            )
            server.sendmail(msg["From"], msg["To"], msg.as_string())
            logger.info("Email sent successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to send email: {e}", exc_info=True)
            return False
        finally:
            try:
                if "server" in locals() and server:
                    server.quit()
            except Exception:
                pass

    def send_simple_email(self, subject, body, html_body=None):
        """Sends a simple email with optional HTML content."""
        msg_root = MIMEMultipart("alternative")
        msg_root["Subject"] = subject
        msg_root["From"] = self.sender_email
        msg_root["To"] = self.recipient_email

        # Plain text part
        text_part = MIMEText(body, "plain")
        msg_root.attach(text_part)

        # Optional HTML part
        if html_body:
            html_part = MIMEText(html_body, "html")
            msg_root.attach(html_part)

        return self._send_email(msg_root)  # Use the internal helper

    def send(self, observations, custom_template=None, css=None, plain_text_fallback=None):
        """Sends a complex email notification with observation details and plots."""
        # Overall message container: multipart/alternative for text and HTML versions
        msg_root = MIMEMultipart("alternative")
        msg_root["Subject"] = f"Good weather in {observations.place.name}"
        msg_root["From"] = self.sender_email
        msg_root["To"] = self.recipient_email

        # Fallback plain text message
        if plain_text_fallback is None:
            plain_text_fallback = "This is a fallback message. Please enable HTML to see the full content."
        text_part = MIMEText(plain_text_fallback, "plain")
        msg_root.attach(text_part)

        # Create multipart/related for HTML and inline images
        msg_related = MIMEMultipart("related")

        # HTML message content
        html_content = observations.to_html(custom_template=custom_template, css=css)
        html_part = MIMEText(html_content, "html")
        msg_related.attach(html_part)  # First part of related is the HTML

        # Add weather image (inline)
        logger.info("Generating weather plot for email...")
        weather_plot_fig = observations.plot_weather()  # Call public method
        if weather_plot_fig:
            self.attach_image(
                msg_related, weather_plot_fig, filename="weather_plot.png"
            )
        else:
            logger.warning(
                "observations.plot_weather() returned None or an invalid plot object, not attaching weather plot."
            )

        # Add planets image (inline)
        logger.info("Generating Solar Objects plot for email...")
        planets_plot_fig = observations.plot_planets()  # Call public method
        if planets_plot_fig:
            self.attach_image(
                msg_related, planets_plot_fig, filename="planets_plot.png"
            )
        else:
            logger.warning(
                "observations.plot_planets() returned None or an invalid plot object, not attaching planets plot."
            )

        # Add messier image (inline)
        logger.info("Generating messier plot for email...")
        messier_plot_fig = observations.plot_messier()  # Call public method
        if messier_plot_fig:
            self.attach_image(
                msg_related, messier_plot_fig, filename="messier_plot.png"
            )
        else:
            logger.warning(
                "observations.plot_messier() returned None or an invalid plot object, not attaching messier plot."
            )

        # Attach the multipart/related part to the multipart/alternative part
        msg_root.attach(msg_related)

        return self._send_email(msg_root)  # Use the internal helper

    @staticmethod
    def attach_image(message, plot, filename="image.png"):
        """Attaches a plot image to the email message for inline display."""
        if plot is None:  # Check if plot object itself is None
            logger.warning(f"Plot object for {filename} is None. Skipping attachment.")
            return

        plot_bytes = Utils.plot_to_bytes(plot)
        if plot_bytes is None:
            logger.warning(
                f"plot_to_bytes returned None for {filename}. Skipping attachment."
            )
            return

        try:
            # If plot_bytes is already bytes, use it directly.
            # Otherwise, assume it's a file-like object (like BytesIO) and try getvalue or read.
            if isinstance(plot_bytes, bytes):
                img_data = plot_bytes
            elif hasattr(plot_bytes, "getvalue"):
                img_data = plot_bytes.getvalue()
            else:
                img_data = plot_bytes.read()

            if not img_data:
                logger.warning(
                    f"Image data is empty for {filename} after plot_to_bytes. Skipping attachment."
                )
                return

            image = MIMEImage(img_data, _subtype="png")  # Added _subtype
            image.add_header("Content-ID", f"<{filename}>")
            image.add_header("Content-Disposition", "inline", filename=filename)
            message.attach(image)
            logger.info(f"Attached inline image {filename} with CID <{filename}>")
        except Exception as e:
            logger.error(
                f"Failed to create or attach MIMEImage for {filename}: {e}",
                exc_info=True,
            )

    def __str__(self) -> str:
        return (
            f"Notify(recipient_email='{self.recipient_email}', "
            f"smtp_host='{self.smtp_host}',"
            f"smtp_port={self.smtp_port}, "
            f"smtp_user='{self.smtp_user}', "
            f"sender_email='{self.sender_email}')"
        )
