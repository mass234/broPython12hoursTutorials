import smtplib

sender = "pyfchannel@gmail.com"
receiver = "mass23yp@gmail.com"
# sender = "sender@gmail.com"
# receiver = "receiver@gmail.com"
password = "yeshin181818"
subject = "Python email test2"
body = "YEJI!!!!"

message = f"""From: PYF{sender}
To: Mass{receiver} 
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
