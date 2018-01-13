import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import email


class Notify:

  EMAIL_ADDRESS = ''
  EMAIL_PASSWORD = ''

  def __init__(self, email):
    self.email = email

  def send(self, observations):
    message = MIMEMultipart('mixed')
    message['Subject'] = "Good weather in {}".format(observations.place.name)
    message['From'] = Notify.EMAIL_ADDRESS
    message['To'] = self.email

    text = "This is fallback message"

    # Add html message content
    html_message = MIMEText(observations.to_html(), 'html')
    message.attach(html_message)
    
    # Add fallback msessage
    text_message = MIMEText(text, 'plain')
    message.attach(text_message)
    
    # Add weather image
    weather_image = MIMEImage(observations.get_weather_plot_bytes().read())
    message.attach(weather_image)

    # Add messier image
    messier_image = MIMEImage(observations.get_messier_plot_bytes().read())
    message.attach(messier_image)

    #print(message.as_string())

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(Notify.EMAIL_ADDRESS, Notify.EMAIL_PASSWORD)
    server.sendmail(Notify.EMAIL_ADDRESS, self.email, message.as_string())
    server.quit()
