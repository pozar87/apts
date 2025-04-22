import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Import the config object initialized in apts/__init__.py
from . import config
from .utils import Utils


class Notify:
    """
    Handles sending email notifications with observation details and plots.

    This class requires SMTP server details to be passed during initialization.
    It reads these settings (host, port, user, password, TLS preference) and
    uses them to connect to the specified SMTP server for sending emails.

    Example Usage:
        # Assuming 'config' is loaded elsewhere or using apts's default loading
        # recipient = config.get("notification", "recipient_email") # Or get from args
        notifier = Notify(recipient_email="user@example.com")
        # Assuming 'observation_data' is an Observation object
        notifier.send(observation_data)
    """
    def __init__(self, recipient_email):
        self.recipient_email = recipient_email

        # Read SMTP settings directly from the config object
        try:
            self.smtp_host = config.get("notification", "smtp_host")
            # Use getint for port, provide fallback or let it raise error if missing
            self.smtp_port = config.getint("notification", "smtp_port", fallback=587)
            self.smtp_user = config.get("notification", "smtp_user", fallback=None)
            self.smtp_password = config.get("notification", "smtp_password", fallback=None)
            # Use getboolean for TLS flag
            self.smtp_use_tls = config.getboolean("notification", "smtp_use_tls", fallback=True)
        except Exception as e:
            # Handle missing configuration gracefully or re-raise
            # For now, let's log a warning and potentially fail later if needed
            print(f"Warning: Could not load all SMTP settings from config: {e}")
            # Set defaults or None to indicate missing config
            self.smtp_host = getattr(self, 'smtp_host', None) # Keep if already set
            self.smtp_port = getattr(self, 'smtp_port', 587)
            self.smtp_user = getattr(self, 'smtp_user', None)
            self.smtp_password = getattr(self, 'smtp_password', None)
            self.smtp_use_tls = getattr(self, 'smtp_use_tls', True)


    def send(self, observations):
        message = MIMEMultipart("mixed")
        message["Subject"] = f"Good weather in {observations.place.name}"
        # Use the configured SMTP user as the 'From' address
        message["From"] = self.smtp_user
        message["To"] = self.recipient_email

        text = "This is fallback message"

        # Add html message content
        html_message = MIMEText(observations.to_html(), 'html')
        message.attach(html_message)

        # Add fallback msessage
        text_message = MIMEText(text, 'plain')
        message.attach(text_message)

        # Add weather image
        Notify.attach_image(message, observations._generate_plot_weather())

        # Add messier image
        Notify.attach_image(message, observations._generate_plot_messier())

        try:
            server = smtplib.SMTP(self.smtp_host, self.smtp_port)
            server.ehlo()
            if self.smtp_use_tls:
                server.starttls()
                server.ehlo()  # Re-identify after starting TLS
            # Only login if user/password are provided
            if self.smtp_user and self.smtp_password:
                server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.smtp_user, self.recipient_email, message.as_string())
        finally:
            # Ensure server connection is closed
            try:
                server.quit()
            except Exception:
                # Ignore errors during quit if connection failed earlier
                pass

    @staticmethod
    def attach_image(message, plot):
        plot_bytes = Utils.plot_to_bytes(plot)
        image = MIMEImage(plot_bytes.read())
        message.attach(image)
