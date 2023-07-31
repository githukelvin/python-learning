import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv  import load_dotenv

port = 587
emailSmtp= 'smtp.gmail.com'

# load the .env fil

cDir = Path(__file__).resolve().parent if  '__file__' in locals() else Path.cwd()
envars = cDir/'.env'
load_dotenv(envars)

# get the email and password from the .env file
fromEmail = os.getenv('from_email')
passwd = os.getenv('password')

def sendEmail(subject,receiver_email,name,dDate,invoice_no,amount):
    # create email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = formataddr(("kelvin@wehackit",f'{fromEmail}'))
    msg["To"] = receiver_email
    msg['BCC'] = fromEmail
    
    msg.add_alternative(
        f'''\
        <!DOCTYPE html>
        <html>
            <body>
                <p>Hi {name},</p>
                <p>I hope you are well </p>
                <p>I just to drop tou a quick note you that <strong>{amount}USD</strong> in respect of our invoice 
                {invoice_no} is due for payment on <strong>{dDate}<strong></p>
                <p>Kindly let me know if you have confirmed that everything is on track for payment</p>
                <p> Best regards,</p>
                <p>Kelvin</p>
            </body>
        </html>
            ''',
            subtype="html",
    )

    with smtplib.SMTP(emailSmtp,port) as server:
        server.ehlo()
        server.starttls()
        server.login(fromEmail,passwd)
        server.sendmail(fromEmail,receiver_email, msg.as_string())
        print('Email sent successfully')

if __name__ == "__main__":
    sendEmail(
        subject="Invoice Reminder",
        name="Kelvin githu",
        receiver_email="githukelvin254@gmail.com",
        dDate="2021-09-30",
        invoice_no="INV-21-12-009",
        amount="6",
    )