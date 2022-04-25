from twilio.rest import Client
import smtplib

TWILIO_SID= ""
TWILIO_AUTH_TOKEN = ""
TWILIO_VIRTUAL_NUMBER = 12345
TWILIO_VERIFIED_NUMBER = 12345

MY_EMAIL = "@gmail.com"
MY_PASSWORD = ""
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com" #if your email is gmail



class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # send message to your phone from twilio
    def send_sms(self, message):
        message = self.client.messages.create(
            body = message,
            from_= TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        # print if successfully sent
        print(message.sid)

    # send information via emails from your email
    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )