# send_email.py

import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the environment variables
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_alert_email(subject, body, to_email):
    """
    Sends an email using your Gmail account and SMTP.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    # Construct the email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    # Connect and send
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

if __name__ == "__main__":
    subject_line = "Test Email from Python"
    message_body = "Hello! This is a test."
    recipient_email = "ben.m.wight@gmail.com"  # Change as needed

    send_alert_email(subject_line, message_body, recipient_email)
    print("Email sent successfully!")
