# send mail to multiple user

import smtplib
from email.message import EmailMessage

email_id = 'sender@gmail.com'
email_password = 'yk123fthghg'

rlist = ['receiver01@gmail.com','recevier02.@iim.edu.in']

msg = EmailMessage()
msg['Subject'] = 'Mail Using Python'
msg['From'] = 'email_id'
msg['To'] = rlist
msg.set_content("Hi where are you?")

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_id,email_password)
    smtp.send_message(msg)
