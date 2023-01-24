# email send by using excel file.
import pandas as p
import smtplib
from email.message import EmailMessage

email_name = 'send0001@gmail.com'
email_pass = 'qwertyu3456'

data = p.read_excel("Book1.xlsx")  # add excel file
email_column = data.get("email_id")
elist = list(email_column)

msg = EmailMessage()
msg['Subject'] = 'Mail Using Python'
msg['From'] = 'email_name'
msg['To'] = elist
msg.set_content("Hi where are you?")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_name, email_pass)
    smtp.send_message(msg)
