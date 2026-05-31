import logging
import smtplib
from contextlib import contextmanager

from ..config import config
from ..secrets import mask_secret, mask_text
from .composer import NotificationComposer

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
            masked_user = mask_secret(self.smtp_user)
            logger.warning(
                f"SMTP host ('{self.smtp_host}') or user ('{masked_user}') not configured. Email notifications may fail."
            )

    @contextmanager
    def _get_smtp_session(self):
        """Context manager for SMTP session with automatic login and cleanup."""
        if not self.smtp_host:
            raise RuntimeError("SMTP host is not configured.")

        server = None
        try:
            server = smtplib.SMTP(self.smtp_host, self.smtp_port, timeout=30)
            server.ehlo()
            if self.smtp_use_tls:
                server.starttls()
                server.ehlo()

            if self.smtp_user and self.smtp_password:
                try:
                    server.login(self.smtp_user, self.smtp_password)
                except smtplib.SMTPAuthenticationError as e:
                    # Specific handling for authentication error to avoid leaking credentials in logs
                    secrets = [self.smtp_password, self.smtp_user]
                    error_msg = mask_text(str(e), [s for s in secrets if s])
                    logger.error(f"Failed to login to SMTP server: {error_msg}")
                    raise

            yield server
        finally:
            if server:
                try:
                    server.quit()
                except Exception:
                    pass

    def _send_email(self, msg):
        """Internal helper to send a MIME message using configured SMTP."""
        try:
            with self._get_smtp_session() as server:
                logger.info(
                    f"Sending email to {msg['To']} via {self.smtp_host}:{self.smtp_port}"
                )
                server.sendmail(msg["From"], msg["To"], msg.as_string())
                logger.info("Email sent successfully")
                return True
        except Exception as e:
            if not isinstance(e, smtplib.SMTPAuthenticationError):
                secrets = [self.smtp_password, self.smtp_user]
                error_msg = mask_text(str(e), [s for s in secrets if s])
                logger.error(f"Failed to send email: {error_msg}", exc_info=False)
            return False

    def send_simple_email(self, subject, body, html_body=None):
        """Sends a simple email with optional HTML content."""
        if not self.sender_email or not self.recipient_email:
            logger.error("Sender or recipient email not configured. Cannot send email.")
            return False

        msg = NotificationComposer.compose_simple_email(
            self.sender_email, self.recipient_email, subject, body, html_body
        )
        return self._send_email(msg)

    def send(
        self,
        observations,
        custom_template=None,
        css=None,
        plain_text_fallback=None,
        language: str | None = None,
        dark_mode: bool | None = None,
    ):
        """Sends a complex email notification with observation details and plots."""
        if not self.sender_email or not self.recipient_email:
            logger.error("Sender or recipient email not configured. Cannot send email.")
            return False

        msg = NotificationComposer.compose_observation_email(
            self.sender_email,
            self.recipient_email,
            observations,
            custom_template,
            css,
            plain_text_fallback,
            language,
            dark_mode,
        )
        return self._send_email(msg)

    @staticmethod
    def attach_image(message, plot, filename=None):
        """
        Attaches a plot image to the email message for inline display.
        Maintained for backward compatibility and testability.
        """
        NotificationComposer.attach_image(message, plot, filename)

    def __str__(self) -> str:
        masked_user = mask_secret(self.smtp_user)
        return (
            f"Notify(recipient_email='{self.recipient_email}', "
            f"smtp_host='{self.smtp_host}',"
            f"smtp_port={self.smtp_port}, "
            f"smtp_user='{masked_user}', "
            f"sender_email='{self.sender_email}')"
        )
