from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='19i346@psgtech.ac.in',
    to_emails='sathishbvb@gmail.com',
    subject='Expense Limit Reminder',
        html_content='<strong>Dear User, You have exceeded your specified monthl expense limit</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))