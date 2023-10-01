import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'sec@arknet.uk'
email['to'] = 'accounts@arknet.uk'
email['subject'] = 'COP'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP_SSL(host='smtp.ampro3.fcomet.com', port=465) as smtp:
    smtp.ehlo()
    smtp.login('sec@arknet.uk', '{uZrMlG[HHGR1l5e#AA')
    smtp.send_message(email)
    print('all good')