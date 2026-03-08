import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

sender = os.environ.get('SMTP_SENDER', 'otajulia@gmail.com')
recipient = os.environ.get('SMTP_RECIPIENT', 'otajulia@gmail.com')
password = os.environ.get('GMAIL_APP_PASSWORD')

files = [
    Path('CPF_HEALTHCARE_TOPJOURNAL_STRATEGY_DETAILED_AUTOPILOT_20260308.docx'),
    Path('CPF_HEALTHCARE_JOURNAL_STYLE_AUTOPILOT_20260308.docx'),
]

if not password:
    raise SystemExit('ERROR: GMAIL_APP_PASSWORD is not set')

for f in files:
    if not f.exists():
        raise SystemExit(f'ERROR: missing file: {f}')

msg = EmailMessage()
msg['Subject'] = 'CPF Healthcare documents (autopilot)'
msg['From'] = sender
msg['To'] = recipient
msg.set_content('Attached are the two requested documents.')

for f in files:
    data = f.read_bytes()
    msg.add_attachment(
        data,
        maintype='application',
        subtype='vnd.openxmlformats-officedocument.wordprocessingml.document',
        filename=f.name,
    )

with smtplib.SMTP('smtp.gmail.com', 587, timeout=30) as s:
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(sender, password)
    s.send_message(msg)

print('MAIL_SENT_OK')
