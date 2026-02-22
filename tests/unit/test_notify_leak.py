import pytest
import logging
from unittest.mock import patch, MagicMock
from apts.notify import Notify
import smtplib

def test_notify_leak_on_login_error(caplog):
    smtp_password = "SUPER_SECRET_PASSWORD"
    recipient = "test@example.com"

    # Better way to mock config
    with patch("apts.notify.config") as mock_config:
        mock_config.get.side_effect = lambda section, option, fallback=None: {
            ("notification", "smtp_host"): "smtp.example.com",
            ("notification", "smtp_user"): "user@example.com",
            ("notification", "smtp_password"): smtp_password,
            ("notification", "sender_email"): "sender@example.com",
        }.get((section, option), fallback)
        mock_config.getint.return_value = 587
        mock_config.getboolean.return_value = True

        notify = Notify(recipient)

        with patch("smtplib.SMTP") as mock_smtp:
            instance = mock_smtp.return_value
            # Make sure ehlo and starttls don't fail
            instance.ehlo.return_value = (250, b"ok")
            instance.starttls.return_value = (220, b"ready")

            instance.login.side_effect = smtplib.SMTPAuthenticationError(535, f"Authentication failed for password {smtp_password}")

            with caplog.at_level(logging.ERROR):
                notify.send_simple_email("subject", "body")

                # Check that the secret password is NOT in the logs
                assert smtp_password not in caplog.text
                # Check that it IS masked
                assert "SUPE...WORD" in caplog.text
