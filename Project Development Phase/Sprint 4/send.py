import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='19i346@psgtech.ac.in',
    to_emails='19i307@psgtech.ac.in',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))