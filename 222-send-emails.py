import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'sec@arknet.uk'
email['to'] = 'accounts@arknet.uk'
email['subject'] = 'COP'

email.set_content('Email sent')

with smtplib.SMTP_SSL(host='smtp.ampro3.fcomet.com', port=465) as smtp:
    smtp.ehlo()
    smtp.login('sec@arknet.uk', '{uZrMlG[HHGR1l5e#AA')
    smtp.send_message(email)
    print('all good')
