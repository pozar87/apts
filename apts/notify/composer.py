import logging
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ..config import get_plot_format
from ..i18n import gettext_, language_context
from ..utils import Utils
from ..utils.plot import PlotUtils

logger = logging.getLogger(__name__)


class NotificationComposer:
    """
    Handles composition of MIME email messages for notifications.
    """

    @staticmethod
    def compose_simple_email(sender, recipient, subject, body, html_body=None):
        """Composes a simple email with optional HTML content."""
        msg_root = MIMEMultipart("alternative")
        msg_root["Subject"] = Utils.sanitize_header(subject)
        msg_root["From"] = Utils.sanitize_header(sender)
        msg_root["To"] = Utils.sanitize_header(recipient)

        # Plain text part
        text_part = MIMEText(body, "plain", "utf-8")
        msg_root.attach(text_part)

        # Optional HTML part
        if html_body:
            html_part = MIMEText(html_body, "html", "utf-8")
            msg_root.attach(html_part)

        return msg_root

    @staticmethod
    def compose_observation_email(
        sender,
        recipient,
        observations,
        custom_template=None,
        css=None,
        plain_text_fallback=None,
        language: str | None = None,
        dark_mode: bool | None = None,
    ):
        """Composes a complex email notification with observation details and plots."""
        with language_context(language):
            # Overall message container: multipart/alternative for text and HTML versions
            msg_root = MIMEMultipart("alternative")
            msg_root["Subject"] = Utils.sanitize_header(
                gettext_("Good weather in {name}").format(name=observations.place.name)
            )
            msg_root["From"] = Utils.sanitize_header(sender)
            msg_root["To"] = Utils.sanitize_header(recipient)

            # Fallback plain text message
            if plain_text_fallback is None:
                num_planets = len(observations.get_visible_planets(language=language))
                num_messier = len(observations.get_visible_messier(language=language))
                num_ngc = len(observations.get_visible_ngc(language=language))
                plain_text_fallback = gettext_(
                    "Tonight you can see {num_planets} planets, {num_messier} Messier objects, and {num_ngc} NGC/IC objects. "
                    "Enable HTML to see the full content."
                ).format(
                    num_planets=num_planets, num_messier=num_messier, num_ngc=num_ngc
                )
            text_part = MIMEText(plain_text_fallback, "plain", "utf-8")
            msg_root.attach(text_part)

            # Create multipart/related for HTML and inline images
            msg_related = MIMEMultipart("related")

            # HTML message content
            html_content = observations.to_html(
                custom_template=custom_template, css=css, language=language
            )
            html_part = MIMEText(html_content, "html", "utf-8")
            msg_related.attach(html_part)  # First part of related is the HTML

            # Helper for plots
            def attach_observation_plot(plot_func, name):
                logger.info(f"Generating {name} plot for email...")
                plot_fig = plot_func(dark_mode_override=dark_mode, language=language)
                if plot_fig:
                    NotificationComposer.attach_image(
                        msg_related,
                        plot_fig,
                        filename=f"{name}_plot.{get_plot_format()}",
                    )
                else:
                    plot_func_name = getattr(plot_func, "__name__", str(plot_func))
                    logger.warning(
                        f"observations.{plot_func_name}() returned None or an invalid plot object, not attaching {name} plot."
                    )

            # Add plots
            attach_observation_plot(observations.plot_weather, "weather")
            attach_observation_plot(observations.plot_planets, "planets")
            attach_observation_plot(observations.plot_messier, "messier")
            attach_observation_plot(observations.plot_ngc, "ngc")

            # Attach the multipart/related part to the multipart/alternative part
            msg_root.attach(msg_related)

            return msg_root

    @staticmethod
    def attach_image(message, plot, filename=None):
        """
        Attaches a plot image to the email message for inline display.
        The image format is determined by the 'plot_format' setting in apts.ini.
        """
        if plot is None:
            logger.warning(f"Plot object for {filename} is None. Skipping attachment.")
            return

        plot_bytes = PlotUtils.plot_to_bytes(plot)
        if plot_bytes is None:
            logger.warning(
                f"plot_to_bytes returned None for {filename}. Skipping attachment."
            )
            return

        try:
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

            if filename is None:
                filename = f"image.{get_plot_format()}"

            image = MIMEImage(img_data, _subtype=get_plot_format())
            image.add_header("Content-ID", f"<{filename}>")
            image.add_header("Content-Disposition", "inline", filename=filename)
            message.attach(image)
            logger.info(f"Attached inline image {filename} with CID <{filename}>")
        except Exception as e:
            logger.error(
                f"Failed to create or attach MIMEImage for {filename}: {e}",
                exc_info=True,
            )
