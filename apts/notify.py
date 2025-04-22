import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .utils import Utils


class Notify:
    """
    Handles sending email notifications with observation details and plots.

    This class requires SMTP server details to be passed during initialization.
    It reads these settings (host, port, user, password, TLS preference) and
    uses them to connect to the specified SMTP server for sending emails.

    Example Usage:
        config = configparser.ConfigParser()
        config.read('path/to/your/apts.ini')

        notifier = Notify(
            recipient_email=config.get("notification", "recipient_email"),
            smtp_host=config.get("notification", "smtp_host"),
            smtp_port=config.getint("notification", "smtp_port"),
            smtp_user=config.get("notification", "smtp_user"),
            smtp_password=config.get("notification", "smtp_password"),
            smtp_use_tls=config.getboolean("notification", "smtp_use_tls")
        )
        # Assuming 'observation_data' is an Observation object
        notifier.send(observation_data)
    """
    def __init__(
        self,
        recipient_email,
        smtp_host,
        smtp_port,
        smtp_user,
        smtp_password,
        smtp_use_tls=True,
    ):
        self.recipient_email = recipient_email
        self.smtp_host = smtp_host
        self.smtp_port = int(smtp_port)  # Ensure port is integer
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.smtp_use_tls = smtp_use_tls

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
