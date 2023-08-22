import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('web.html').read_text())
email = EmailMessage()
email['from'] = 'zero mastery'
email['to'] = 'ztmDummy2@gmail.com'
email['subject'] = 'you have won 1,000,000 dollars!'



email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ztmDummy1@gmail.com', 'hdjzkasuhemmzwqj')
    smtp.send_message(email)
    print('all good boss')