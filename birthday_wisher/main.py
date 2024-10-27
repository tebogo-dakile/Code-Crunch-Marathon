import os
from dotenv import load_dotenv

import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SHEETY_URL = "https://api.sheety.co/c90c96dcbd6020873fe1c8eace10cb0e/birthdays/sheet1"
response = requests.get(SHEETY_URL)
data = response.json()
print(data)

sender_email = "lesedidakile@gmail.com"
receiver_email = ""
password = os.getenv("EMAIL_PASSWORD")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Happy Birthday BigHead"

body = MIMEText("HBD if you want ke sana.")
message.attach(body)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
