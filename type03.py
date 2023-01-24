# send mail with attachment(pdf,photo)

import os
import smtplib
from email.message import EmailMessage

email_id = 'sender01@gmail.com'
email_pass = '455xyadb233444'

slist = ['recevier01@gmail.com', 'recevier02@gmail.com']

sms = EmailMessage()
sms['Subject'] = 'Your mail'
sms['From'] = 'email_id'
sms['To'] = slist
sms.set_content('Hi\nplease tell me your name')

for each_file in os.listdir():
    if each_file == 'type03.py':
        continue
    with open(each_file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        sms.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(sms)
    
    
# Documents will be sent only if they are available in similar folder otherwise documents like img, pdf, etc will not be send with mail.
