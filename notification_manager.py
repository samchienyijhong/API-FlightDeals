from flight_data import FlightData
from twilio.rest import Client
import os
import dotenv

dotenv.load_dotenv()
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = os.environ["TWILIO_PHONE_NUMBER"]
MY_PHONE_NUMBER = os.environ["MY_PHONE_NUMBER"]


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, flight_data: FlightData):
        flight_message = flight_data.flight_message
        message = self.client.messages.create(
                    body=flight_message,
                    from_=TWILIO_PHONE_NUMBER,
                    to="+886983667633"
        )
        # Prints if successfully sent.
        print(message.sid)
