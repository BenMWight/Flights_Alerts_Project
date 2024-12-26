import os
import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()  # if you're using a .env for credentials
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_ADDRESS_TO_SEND_TO = os.getenv("EMAIL_ADDRESS_TO_SEND_TO")

LAST_RUN_FILE = "last_run.txt"

def get_last_run_time():
    """
    Reads the last run time from a text file.
    Returns a string with the timestamp or None if file not found.
    """
    if os.path.isfile(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, "r") as f:
            return f.read().strip()  # e.g. "2024-12-25 18:00:00"
    return None

def update_last_run_time():
    """
    Updates the last_run.txt file with the current datetime.
    """
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LAST_RUN_FILE, "w") as f:
        f.write(now_str)

def send_alert_email(subject, body, to_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

def main():
    # 1. Get the last run time (if any)
    last_run = get_last_run_time()
    if last_run:
        last_run_message = f"Last email was sent at: {last_run}"
    else:
        last_run_message = "No previous run found."

    # 2. Construct your email body
    email_body = (
        f"Hello! This is the daily flight price check.\n"
        f"{last_run_message}\n\n"
        f"Regards,\nYour Flight Alert Script"
    )

    # 3. Send the email
    send_alert_email(
        subject="Daily Flight Price Check",
        body=email_body,
        to_email= EMAIL_ADDRESS_TO_SEND_TO  # or wherever you want
    )
    print("Email sent successfully!")

    # 4. Update the last run time file
    update_last_run_time()

if __name__ == "__main__":
    main()
