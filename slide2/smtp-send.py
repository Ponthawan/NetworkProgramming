import smtplib

message = """"From: From Joe <joe@blow.com>
To: To Henry <pornthawan@ubuntu.org>
MIME-Version: 1.0
Content-type: text/html
Subject: Test HTML Email

This is an email message sent as HTML.

<b>This is a test HTML Message.</b>
<h1>This is headling</h1>
"""

try:
    smtp = smtplib.SMTP("192.168.1.124")
    smtp.sendmail("pornthawan@ubuntu.org", "pornthawan@ubuntu.org", message)
    print("Email sent successfully")
except Exception as err:
    print(str(err))
    