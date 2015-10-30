import smtplib
from email.mime.text import MIMEText


sender_163 = 'youknow@163.com'
password_163 = 'Iwouldnottellyou'
server_domain_163 = 'smtp.163.com'
server_port_163 = 25

sender_google = 'youknow@gmail.com'
password_google = 'Iwouldnottellyou'
server_domain_google = 'smtp.gmail.com'
server_port_gmail = 587


sender = sender_google
password = password_google
server_domain = server_domain_google
server_port = server_port_gmail
receivers = ['youknow@cse.cuhk.edu.hk']
# the receiver can be multiple

message = """
From: From %s <%s>
To: To %s <%s>
Subject: SMTP e-mail test

Hi Jiacheng,

I am learning how to use python smtp lib.
This is a test e-mail message.
Hopefully it could arrive :-)

Best,
Carlson
""" % ('Jiacheng', sender, 'tester', ', '.join(receivers))

message = MIMEText(message)
message['From'] = sender
message['To'] = ', '.join(receivers)
message['Subject'] = 'SMTP e-mail test'
# if not using MIMEText,
# the definition of subject and to field may fail
print message
print message.as_string()

try:
    server = smtplib.SMTP(server_domain, server_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, receivers, message.as_string())
    server.quit()
    print "Successfully sent email"
except Exception as e:
    print "Error: unable to send email - " + str(e)
