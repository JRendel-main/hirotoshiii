import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "hirotoshitest@gmail.com"  # Enter your address
# Enter receiver address
password = 'nhqdiwtariodmlxy'

receiver_email = input('Enter Recipeint gmail here: ')
message = input('Enter your message here: ')
message = """\
Subject: Hi there

{}""".format(message)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)