import os
from dotenv import load_dotenv

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import datetime

load_dotenv()

def get_json_file():
    SHEETY_URL = os.getenv(SHEETY_URL)    
    response = requests.get(SHEETY_URL)
    return response.json()


def send_email(receiver_email, subject, body):
    sender_email = "lesedidakile@gmail.com"
    password = os.getenv("EMAIL_PASSWORD")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    data = get_json_file()
    today = datetime.now().strftime("%d-%m")

    for person in data["Sheet1"]:
        if person["Birthday"] == today:
            send_email(person["Email"], "Happy Birthday Bighead", "HBD if you want")