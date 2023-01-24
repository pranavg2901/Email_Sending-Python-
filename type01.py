# sending gmail using python

import smtplib
from email.message import EmailMessage

id = 'mail@gmail.com'
password = 'yk1235ffgb'

sms = EmailMessage()
sms['Subject'] = "Hiring process call"
sms['From'] = id
sms['To'] = 'reciver@gmail.com'
sms.set_content('My name is pranav and I Completed my graduation in 2022')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(id, password)
    smtp.send_message(sms)

print('Mail send')
