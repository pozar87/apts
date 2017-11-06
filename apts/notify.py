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
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Dobre warunki obserwacyjne!"
    msg['From'] = Notify.EMAIL_ADDRESS
    msg['To'] = self.email

    observations.to_html()

    weather_image = MIMEImage(observations.get_weather_plot_bytes().read())
    # Define the image's ID
    weather_image.add_header('Content-ID', 'weather')
    msg.attach(weather_image)

    # with open("/tmp/message.html",'r') as massage:
    #  msg.attach(MIMEText(massage.read(),'html'))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(Notify.EMAIL_ADDRESS, Notify.EMAIL_PASSWORD)
    server.sendmail(Notify.EMAIL_ADDRESS, self.email, msg.as_string())
    server.quit()
