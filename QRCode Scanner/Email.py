import smtplib
import imghdr
from email.message import EmailMessage
import CustomGUI
from CustomGUI import receiver_email as Reciever_Email, bodyMsg

def send_Mail():
    Sender_Email = "hirotoshitest@gmail.com"
    Password = 'nhqdiwtariodmlxy'
    
    headMsg = ('Hello!')
    newMessage = EmailMessage()                         
    newMessage['Subject'] = headMsg 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email.get()                   
    newMessage.set_content(bodyMsg.get()) 

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
send_Mail()
                   