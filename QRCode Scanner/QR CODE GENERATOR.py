import qrcode
import mysql.connector as mysql
import tkinter as tk
import tkinter.font as tkFont
import smtplib, ssl
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#connect to database
#db = mysql.connect(host='localhost',
                   #user='root',
                   #password='',
                   #db='qrcodestudent')
#command_handler = db.cursor(buffered=True)

#GUI for App
import tkinter as tk
import tkinter.font as tkFont

#setting title
root = tk.Tk()
root.title("QR Code Generator")
#setting window size
width=438
height=199
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

mainLbl=tk.Label(root)
ft = tkFont.Font(family='Times',size=18)
mainLbl["font"] = ft
mainLbl["fg"] = "#333333"
mainLbl["justify"] = "center"
mainLbl["text"] = "Student QRCode Generator"
mainLbl.place(x=90,y=30,width=273,height=30)

student_number = tk.StringVar()
entry = tk.Entry(root, textvariable = student_number)
entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
entry["font"] = ft
entry["fg"] = "#333333"
entry["justify"] = "center"
entry["relief"] = "groove"
entry.place(x=140,y=80,width=175,height=30)

def gen_qrcode():
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(student_number.get())
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save('{}.png'.format(student_number.get()))

email_address = tk.StringVar()
entryEmail = tk.Entry(root, textvariable= email_address)
entryEmail["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
entryEmail["font"] = ft
entryEmail["fg"] = "#333333"
entryEmail["justify"] = "center"
entryEmail["relief"] = "groove"
entryEmail.place(x=140,y=120,width=175,height=30)
        
def command_val():
    gen_qrcode()
    entry.delete(0, 'end')

# def GmailSend():
#     port = 465  # For SSL
#     smtp_server = "smtp.gmail.com"
#     sender_email = "hirotoshitest@gmail.com"  # Enter your address
#     message = 'Here is your QR Code {}'.format(student_number.get())
#     password = 'nhqdiwtariodmlxy'
#     message = """\
#     Subject: Hi there

#     Hello {} this is a test!
#     """.format(student_number.get())
#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, email_address.get(), message)
          
GButton_503=tk.Button(root, command = command_val)
GButton_503["bg"] = "#f9f9f9"
ft = tkFont.Font(family='Times',size=10)
GButton_503["font"] = ft
GButton_503["fg"] = "#4f5663"
GButton_503["justify"] = "center"
GButton_503["text"] = "Generate!"
GButton_503.place(x=190,y=170,width=70,height=25)

root.mainloop()
