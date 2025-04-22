import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Import the config object from the new config module
from .config import config
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

        # Read SMTP settings directly from the imported config object
        # Use fallback values to avoid errors if keys are missing
        self.smtp_host = config.get("notification", "smtp_host", fallback=None)
        self.smtp_port = config.getint("notification", "smtp_port", fallback=587)
        self.smtp_user = config.get("notification", "smtp_user", fallback=None)
        self.smtp_password = config.get("notification", "smtp_password", fallback=None)
        self.smtp_use_tls = config.getboolean("notification", "smtp_use_tls", fallback=True)

        # Basic check if essential settings are missing
        if not self.smtp_host or not self.smtp_user:
             # TODO: Use proper logging here instead of print
             print(f"Warning: SMTP host ('{self.smtp_host}') or user ('{self.smtp_user}') not configured. Email notifications may fail.")


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
