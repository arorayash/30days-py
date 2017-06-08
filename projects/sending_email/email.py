# -*- coding: utf-8 -*-

from smtplib import SMTP, SMTPAuthenticationError

host = "smtp.gmail.com"
port = 587
username = "xoxo@gmail.com"
password = "*****"
from_email = username
to_list = ["xoxo@gmail.com"]

email_conn = SMTP(host, port)
email_conn.starttls()
try:
    email_conn.login(username, password)
    email_conn.sendmail(from_email, to_list, "Check mail using py script")
    print("Mails sent!")
except SMTPAuthenticationError:
    print("Invalid login")
except:
    print("Error")


