# -*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "xoxo@gmail.com"
password = "*****"
from_email = "xoxo@gmail.com"
to_list = ["xoxo@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)

msg = MIMEMultipart("alternative")
msg["Subject"] = "Test mail"
msg["From"] = "xoxo@gmail.com"
msg["To"] = "xoxo@gmail.com"
html_txt = """\
<html>
    <head></head>
    <body>
        <h4 style="text-align: center">By T S Eliot</h4>
        <div style="width: 100%">
            <img src="https://www.dropbox.com/s/chm4726pq2rca2r/img2.jpg?dl=1" style="margin: 0 auto; display: block">
        </div>
        <p style="text-align: center">
            <blockquote>
                Time and the bell have buried the day,
                the black cloud carries the sun away.
                Will the sunflower turn to us, will the clematis
                Stray down, bend to us; tendril and spray
                Clutch and cling?
                Chill
                Fingers of yew be curled
                Down on us? After the kingfisher's wing
                Has answered light to light, and is silent, the light is still
                At the still point of the turning world.
            </blockquote>
        </p>
    </body>
</html>
"""

mail_text = MIMEText(html_txt, "html")
msg.attach(mail_text)
email_conn.sendmail(from_email, to_list, msg.as_string())
email_conn.quit()
