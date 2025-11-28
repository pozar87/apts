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

    @patch("apts.notify.get_plot_format")
    @patch("apts.notify.smtplib.SMTP")
    @patch.object(
        Notify, "_send_email"
    )  # Mock _send_email to capture the Message object
    @patch.object(Notify, "attach_image", autospec=True)  # Spy on attach_image
    def test_send_with_default_template(
        self,
        mock_attach_image_spy,
        mock_send_email_internal,
        mock_smtp_constructor,
        mock_get_plot_format,
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

        for plot_format in ["webp", "png"]:
            mock_get_plot_format.return_value = plot_format
            mock_attach_image_spy.reset_mock()
            mock_send_email_internal.reset_mock()
            self.mock_observation.to_html.reset_mock()

            self.notify.send(self.mock_observation)

            self.mock_observation.to_html.assert_called_once_with(
                custom_template=None, css=None, language=None
            )
            mock_send_email_internal.assert_called_once()
            sent_message_object = mock_send_email_internal.call_args[0][0]

            related_part = None
            for part in sent_message_object.get_payload():
                if part.get_content_type() == "multipart/related":
                    related_part = part
                    break
            self.assertIsNotNone(
                related_part, f"multipart/related part not found for format {plot_format}"
            )

            mock_attach_image_spy.assert_has_calls(
                [
                    call(
                        related_part,
                        mock_weather_plot,
                        filename=f"weather_plot.{plot_format}",
                    ),
                    call(
                        related_part,
                        mock_planets_plot,
                        filename=f"planets_plot.{plot_format}",
                    ),
                    call(
                        related_part,
                        mock_messier_plot,
                        filename=f"messier_plot.{plot_format}",
                    ),
                ],
                any_order=False,
            )
            self.assertEqual(mock_attach_image_spy.call_count, 3)

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
            custom_template=custom_template, css=None, language=None
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
            custom_template=None, css=custom_css, language=None
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
            custom_template=custom_template, css=custom_css, language=None
        )
        self.assertTrue(mock_smtp_instance.sendmail.called)
        # mock_attach_image is spied upon

    @patch("apts.notify.get_plot_format")
    @patch("apts.notify.smtplib.SMTP")
    @patch.object(Notify, "_send_email")  # Mock _send_email as it's called by send()
    @patch.object(Notify, "attach_image", autospec=True)  # Spy on attach_image
    def test_send_no_plots_if_plotting_fails(
        self,
        mock_attach_image_spy,
        mock_send_email_internal,
        mock_smtp_constructor,
        mock_get_plot_format,
    ):
        """Test that attach_image is not called if plot methods return None."""
        mock_smtp_constructor.return_value
        self.mock_observation.to_html.return_value = "<html><body>No Plots</body></html>"

        # Scenario 1: Weather plot fails
        self.mock_observation.plot_weather.return_value = None
        mock_messier_plot = MagicMock(name="MessierPlotOnly")
        mock_planets_plot = MagicMock(name="PlanetPlotOnly")
        self.mock_observation.plot_messier.return_value = mock_messier_plot
        self.mock_observation.plot_planets.return_value = mock_planets_plot

        mock_get_plot_format.return_value = "png"
        self.notify.send(self.mock_observation)

        mock_send_email_internal.assert_called_once()
        sent_message_object = mock_send_email_internal.call_args[0][0]
        related_part = None
        for part in sent_message_object.get_payload():
            if part.get_content_type() == "multipart/related":
                related_part = part
                break

        mock_attach_image_spy.assert_has_calls(
            [
                call(related_part, mock_planets_plot, filename="planets_plot.png"),
                call(related_part, mock_messier_plot, filename="messier_plot.png"),
            ],
            any_order=True,
        )
        self.assertEqual(mock_attach_image_spy.call_count, 2)

        # Reset mocks
        mock_send_email_internal.reset_mock()
        mock_attach_image_spy.reset_mock()
        self.mock_observation.plot_weather = MagicMock()
        self.mock_observation.plot_messier = MagicMock()

        # Scenario 2: Messier plot fails
        mock_weather_plot_only = MagicMock(name="WeatherPlotOnly")
        mock_planets_plot_only = MagicMock(name="PlanetsPlotOnly")
        self.mock_observation.plot_weather.return_value = mock_weather_plot_only
        self.mock_observation.plot_planets.return_value = mock_planets_plot_only
        self.mock_observation.plot_messier.return_value = None

        mock_get_plot_format.return_value = "webp"
        self.notify.send(self.mock_observation)

        mock_send_email_internal.assert_called_once()
        sent_message_object_2 = mock_send_email_internal.call_args[0][0]
        related_part_2 = None
        for part in sent_message_object_2.get_payload():
            if part.get_content_type() == "multipart/related":
                related_part_2 = part
                break

        mock_attach_image_spy.assert_has_calls(
            [
                call(related_part_2, mock_weather_plot_only, filename="weather_plot.webp"),
                call(related_part_2, mock_planets_plot_only, filename="planets_plot.webp"),
            ],
            any_order=True,
        )
        self.assertEqual(mock_attach_image_spy.call_count, 2)

        # Reset mocks
        mock_send_email_internal.reset_mock()
        mock_attach_image_spy.reset_mock()

        # Scenario 3: All plots fail
        self.mock_observation.plot_weather.return_value = None
        self.mock_observation.plot_messier.return_value = None
        self.mock_observation.plot_planets.return_value = None

        self.notify.send(self.mock_observation)
        mock_send_email_internal.assert_called_once()
        mock_attach_image_spy.assert_not_called()


    @patch("apts.notify.smtplib.SMTP")
    @patch.object(Notify, "_send_email")
    @patch("apts.notify.gettext_")
    def test_send_with_translation(self, mock_gettext, mock_send_email, mock_smtp):
        """Test that send uses the correct language."""

        def side_effect(arg):
            if arg == "Good weather in {}":
                return "Dobra pogoda w {}"
            elif arg == "Tonight you can see {num_planets} planets and {num_messier} Messier objects. Enable HTML to see the full content.":
                return "Dziś w nocy możesz zobaczyć {num_planets} planet i {num_messier} obiektów Messiera. Włącz HTML, aby zobaczyć pełną treść."
            return arg

        mock_gettext.side_effect = side_effect

        self.mock_observation.get_visible_planets.return_value = [1, 2, 3]
        self.mock_observation.get_visible_messier.return_value = [1, 2, 3, 4, 5]

        # Call send with Polish language
        self.notify.send(self.mock_observation, language="pl")

        # Verify that the subject and fallback text are translated
        mock_send_email.assert_called_once()
        sent_message_object = mock_send_email.call_args[0][0]
        self.assertEqual(
            sent_message_object["Subject"], "Dobra pogoda w Test Location"
        )
        self.assertIn(
            "Dziś w nocy możesz zobaczyć 3 planet i 5 obiektów Messiera.",
            sent_message_object.get_payload(0).get_payload(decode=True).decode("utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
