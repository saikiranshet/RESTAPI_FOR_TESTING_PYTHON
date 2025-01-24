# All imports below are part of python built packages no need to install any exras

# smtplib provides functionality to send emails using SMTP.
import smtplib
# MIMEMultipart send emails with both text content and attachments.
from email.mime.multipart import MIMEMultipart
# MIMEText for creating body of the email message.
from email.mime.text import MIMEText
# MIMEApplication attaching application-specific data (like CSV files) to email messages.
from email.mime.application import MIMEApplication

subject = "Automation Report"
body = "Please find your test result of your automation"
sender_email = "saikiran.shet@gmail.com"
recipient_email ="saikiran.shet@gmail.com"
sender_password = "Valid password here"
smtp_server = 'smtp.gmail.com'
smtp_port = 465
path_to_file = '/workspaces/RESTAPI_FOR_TESTING_PYTHON/reports'

# MIMEMultipart() creates a container for an email message that can hold
# different parts, like text and attachments and in next line we are
# attaching different parts to email container like subject and others.
message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender_email
message['To'] = recipient_email
body_part = MIMEText(body)
message.attach(body_part)

# section 1 to attach file
with open(path_to_file,'rb') as file:
    # Attach the file with filename to the email
    message.attach(MIMEApplication(file.read(), Name='reports'))

# secction 2 for sending email
with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
   server.login(sender_email, sender_password)
   server.sendmail(sender_email, recipient_email, message.as_string())