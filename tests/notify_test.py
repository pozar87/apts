import unittest
from unittest.mock import patch, MagicMock, call
from apts.notify import Notify
from tests import setup_observation


class TestNotify(unittest.TestCase):
    def setUp(self):
        self.observation = setup_observation()
        # Create a mock observation with needed attributes
        self.mock_observation = MagicMock()
        self.mock_observation.place.name = "Test Location"
        # Add mock methods for plotting
        self.mock_observation.plot_weather = MagicMock()
        self.mock_observation.plot_messier = MagicMock()

        # Setup the notify object
        self.notify = Notify("test@example.com")
        self.notify.sender_email = "test_sender@example.com"  # Set a sender email

    @patch("apts.notify.smtplib.SMTP")
    @patch.object(
        Notify, "_send_email"
    )  # Mock _send_email to capture the Message object
    @patch.object(Notify, "attach_image", autospec=True)  # Spy on attach_image
    def test_send_with_default_template(
        self, mock_attach_image_spy, mock_send_email_internal, mock_smtp_constructor
    ):
        """Test send default template, plot attachment, and email structure."""

        html_body_content = "<html><body>Test Default Template</body></html>"
        self.mock_observation.to_html.return_value = html_body_content

        mock_weather_plot = MagicMock(name="WeatherPlot")
        mock_planets_plot = MagicMock(name="WeatherPlot")
        mock_messier_plot = MagicMock(name="MessierPlot")
        self.mock_observation.plot_weather.return_value = mock_weather_plot
        self.mock_observation.plot_planets.return_value = mock_planets_plot
        self.mock_observation.plot_messier.return_value = mock_messier_plot

        # Call send with default parameters
        self.notify.send(self.mock_observation)

        # Verify to_html was called without custom template or CSS
        self.mock_observation.to_html.assert_called_once_with(
            custom_template=None, css=None
        )

        # Verify _send_email was called and capture the message object
        mock_send_email_internal.assert_called_once()
        sent_message_object = mock_send_email_internal.call_args[0][0]

        # 1. Verify that the main message is multipart/alternative.
        self.assertTrue(sent_message_object.is_multipart())
        self.assertEqual(
            sent_message_object.get_content_type(), "multipart/alternative"
        )

        # 2. Verify that a multipart/related part is attached.
        related_part = None
        for part in sent_message_object.get_payload():
            if part.get_content_type() == "multipart/related":
                related_part = part
                break
        self.assertIsNotNone(related_part, "multipart/related part not found")

        # 3. Inside multipart/related, check for HTML MIMEText part.
        html_mime_part = None
        if related_part:
            for sub_part in related_part.get_payload():
                if sub_part.get_content_type() == "text/html":
                    html_mime_part = sub_part
                    break
        self.assertIsNotNone(
            html_mime_part, "HTML MIMEText part not found in multipart/related"
        )

        # 4. Check HTML content.
        if html_mime_part:
            self.assertEqual(
                html_mime_part.get_payload(decode=True).decode(), html_body_content
            )

        # 5. Verify attach_image calls
        if related_part:  # Ensure related_part was found before using it in assertions
            mock_attach_image_spy.assert_has_calls(
                [
                    call(related_part, mock_weather_plot, filename="weather_plot.png"),
                    call(related_part, mock_planets_plot, filename="planets_plot.png"),
                    call(related_part, mock_messier_plot, filename="messier_plot.png"),
                ],
                any_order=False,
            )
            self.assertEqual(mock_attach_image_spy.call_count, 3)

        # Verify _send_email was called (which implies sendmail would be called if not for this mock)
        # self.assertTrue(mock_smtp_instance.sendmail.called) # This is no longer valid as _send_email is mocked
        mock_send_email_internal.assert_called_once()  # This is the correct check now

    @patch("apts.notify.smtplib.SMTP")
    @patch.object(Notify, "attach_image", autospec=True)
    def test_send_with_custom_template(self, mock_attach_image, mock_smtp):
        """Test that send passes custom template to to_html"""
        mock_smtp_instance = mock_smtp.return_value
        self.mock_observation.to_html.return_value = (
            "<html><body>Custom Template</body></html>"
        )
        self.mock_observation.plot_weather.return_value = MagicMock(name="WeatherPlot")
        self.mock_observation.plot_messier.return_value = MagicMock(name="MessierPlot")

        custom_template = "/path/to/custom/template.html"

        self.notify.send(self.mock_observation, custom_template=custom_template)

        self.mock_observation.to_html.assert_called_once_with(
            custom_template=custom_template, css=None
        )
        self.assertTrue(mock_smtp_instance.sendmail.called)
        # mock_attach_image is spied upon, detailed checks in test_send_with_default_template

    @patch("apts.notify.smtplib.SMTP")
    @patch.object(Notify, "attach_image", autospec=True)
    def test_send_with_custom_css(self, mock_attach_image, mock_smtp):
        """Test that send passes custom CSS to to_html"""
        mock_smtp_instance = mock_smtp.return_value
        self.mock_observation.to_html.return_value = "<html><head><style>body{} h1{color:blue}</style></head><body>Custom CSS</body></html>"
        self.mock_observation.plot_weather.return_value = MagicMock(name="WeatherPlot")
        self.mock_observation.plot_messier.return_value = MagicMock(name="MessierPlot")

        custom_css = "h1 { color: blue; }"

        self.notify.send(self.mock_observation, css=custom_css)

        self.mock_observation.to_html.assert_called_once_with(
            custom_template=None, css=custom_css
        )
        self.assertTrue(mock_smtp_instance.sendmail.called)
        # mock_attach_image is spied upon

    @patch("apts.notify.smtplib.SMTP")
    @patch.object(Notify, "attach_image", autospec=True)
    def test_send_with_custom_template_and_css(self, mock_attach_image, mock_smtp):
        """Test that send passes both custom template and CSS to to_html"""
        mock_smtp_instance = mock_smtp.return_value
        self.mock_observation.to_html.return_value = "<html><head><style>body{} h1{color:blue}</style></head><body>Custom Template and CSS</body></html>"
        self.mock_observation.plot_weather.return_value = MagicMock(name="WeatherPlot")
        self.mock_observation.plot_messier.return_value = MagicMock(name="MessierPlot")

        custom_template = "/path/to/custom/template.html"
        custom_css = "h1 { color: blue; }"

        self.notify.send(
            self.mock_observation, custom_template=custom_template, css=custom_css
        )

        self.mock_observation.to_html.assert_called_once_with(
            custom_template=custom_template, css=custom_css
        )
        self.assertTrue(mock_smtp_instance.sendmail.called)
        # mock_attach_image is spied upon

    @patch("apts.notify.smtplib.SMTP")
    @patch.object(Notify, "_send_email")  # Mock _send_email as it's called by send()
    @patch.object(Notify, "attach_image", autospec=True)  # Spy on attach_image
    def test_send_no_plots_if_plotting_fails(
        self, mock_attach_image_spy, mock_send_email_internal, mock_smtp_constructor
    ):
        """Test that attach_image is not called if plot methods return None."""
        mock_smtp_constructor.return_value  # mock_smtp_instance

        self.mock_observation.to_html.return_value = (
            "<html><body>No Plots</body></html>"
        )

        # Scenario 1: Weather plot fails, Messier and Planets plot succeeds
        self.mock_observation.plot_weather.return_value = None
        mock_messier_plot = MagicMock(name="MessierPlotOnly")
        mock_planets_plot = MagicMock(name="PlanetPlotOnly")
        self.mock_observation.plot_messier.return_value = mock_messier_plot
        self.mock_observation.plot_planets.return_value = mock_planets_plot

        self.notify.send(self.mock_observation)

        mock_send_email_internal.assert_called_once()  # Ensure email is still sent
        sent_message_object = mock_send_email_internal.call_args[0][0]
        related_part = None
        for part in (
            sent_message_object.get_payload()
        ):  # Find the multipart/related part to pass to assert_called_once_with
            if part.get_content_type() == "multipart/related":
                related_part = part
                break
        self.assertIsNotNone(
            related_part, "multipart/related part not found in scenario 1"
        )

        mock_attach_image_spy.assert_has_calls(
            [
                call(related_part, mock_messier_plot, filename="messier_plot.png"),
                call(related_part, mock_planets_plot, filename="planets_plot.png"),
            ],
            any_order=True,
        )
        self.assertEqual(mock_attach_image_spy.call_count, 2)

        # Reset mocks for the next scenario
        mock_send_email_internal.reset_mock()
        mock_attach_image_spy.reset_mock()
        # Re-configure plot_weather as it's part of self.mock_observation shared across scenarios if not reset properly
        self.mock_observation.plot_weather = MagicMock()
        self.mock_observation.plot_messier = MagicMock()

        # Scenario 2: Messier plot fails, Weather and Planets plot succeeds
        mock_weather_plot_only = MagicMock(name="WeatherPlotOnly")
        mock_planets_plot_only = MagicMock(name="PlanetsPlotOnly")
        self.mock_observation.plot_weather.return_value = mock_weather_plot_only
        self.mock_observation.plot_planets.return_value = mock_planets_plot_only
        self.mock_observation.plot_messier.return_value = None

        self.notify.send(self.mock_observation)

        mock_send_email_internal.assert_called_once()
        sent_message_object_2 = mock_send_email_internal.call_args[0][0]
        related_part_2 = None
        for part in sent_message_object_2.get_payload():
            if part.get_content_type() == "multipart/related":
                related_part_2 = part
                break
        self.assertIsNotNone(
            related_part_2, "multipart/related part not found in scenario 2"
        )

        mock_attach_image_spy.assert_has_calls(
            [
                call(
                    related_part_2, mock_weather_plot_only, filename="weather_plot.png"
                ),
                call(
                    related_part_2, mock_planets_plot_only, filename="planets_plot.png"
                ),
            ],
            any_order=True,
        )

        # Reset mocks for the next scenario
        mock_send_email_internal.reset_mock()
        mock_attach_image_spy.reset_mock()
        self.mock_observation.plot_weather = MagicMock()
        self.mock_observation.plot_messier = MagicMock()

        # Scenario 3: Both plots fail
        self.mock_observation.plot_weather.return_value = None
        self.mock_observation.plot_messier.return_value = None
        self.mock_observation.plot_planets.return_value = None

        self.notify.send(self.mock_observation)

        mock_send_email_internal.assert_called_once()
        mock_attach_image_spy.assert_not_called()


if __name__ == "__main__":
    unittest.main()
