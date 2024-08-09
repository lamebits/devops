import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from constants import SMTP_SERVER,SMTP_PORT,SENDER_EMAIL,RECEIPENT_EMAIL,OUTPUT_FILE_PATH,EMAIL_SUBJECT,EMAIL_BODY
from dotenv import load_dotenv
load_dotenv()

def mailsending_main():
    # Define email parameters
    smtp_server = SMTP_SERVER  # Replace with your SMTP server
    smtp_port = SMTP_PORT  # Common port for TLS
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    sender_email = SENDER_EMAIL
    recipient_email = RECEIPENT_EMAIL
    subject = EMAIL_SUBJECT
    body = EMAIL_BODY
    attachment_path = OUTPUT_FILE_PATH

    # Create the MIMEMultipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    if os.path.isfile(attachment_path):
        with open(attachment_path,'rb') as attachment:
            # Add file as application/octet-stream
            # Email client will try to open it in binary
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)
            
            # Add header with file name
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {os.path.basename(attachment_path)}',
            )
            
            # Attach the file to the email
            msg.attach(part)
    else:
        print(f"Attachment file {attachment_path} does not exist.")

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(username, password)
            server.send_message(msg)
            print('Email sent successfully!')
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    mailsending_main()