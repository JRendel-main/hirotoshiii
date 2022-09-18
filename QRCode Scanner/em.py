import smtplib
import imghdr
from email.message import EmailMessage

Sender_Email = "hirotoshitest@gmail.com"
Password = 'nhqdiwtariodmlxy'

Reciever_Email = input('Enter recepient email here: ')
headMsg = input('Enter header Here: ')
bodyMsg = input('Enter body message here: ')


newMessage = EmailMessage()                         
newMessage['Subject'] = headMsg 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content(bodyMsg) 

files = ['testing.png']

for file in files:
    with open(file, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage)
    print('Email Successfully sent')                   