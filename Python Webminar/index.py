from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode
import cv2
from pyzbar.pyzbar import decode
import time
import random

print("/************************/")
print("1. For QRCode Generator")
print("2. For QRCode Scanner")
print("/************************/")
user_select = input(str("Option: "))
if user_select == "1":
    root = Tk()
    root.title("QR Code Creator")
    width = 400
    height = 280
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)


    #==============================VARIABLES======================================
    qrname = StringVar()

    #==============================FUNCTIONS======================================

    def generate(event=None):
        s = qrname.get()
        url = pyqrcode.create(s)
        r = s[0:-4]
        url.png("Generated QR Codes\{}.png".format(r), scale = 8)
        

    #==============================FRAMES=========================================
    Top = Frame(root, bd=2,  relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)


    #==============================LABELS=========================================
    lbl_title = Label(Top, text = "NEUST Attendance QR Code Generator", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_qrurl = Label(Form, text = "Enter Student Number:", font=('arial', 14), bd=15)
    lbl_qrurl.grid(row=0, sticky="e")

     
    #==============================ENTRY WIDGETS==================================
    qrurl = Entry(Form, textvariable=qrname, font=(14))
    qrurl.grid(row=0, column=1)


    #==============================BUTTON WIDGETS=================================
    btn_generate = Button(Form, text="Generate QR", width=45, command=generate)
    btn_generate.grid(pady=25, row=2, columnspan=2)
    btn_generate.bind('<Return>', generate)

      

    #==============================INITIALIATION==================================
    if __name__ == '__main__':
        root.mainloop()
elif user_select == "2":
    cap = cv2.VideoCapture(3)
    cap.set(3,640)
    cap.set(4,480)
    used_codes = []


    camera = True
    while camera == True:
        sucess, frame = cap.read()

        for code in decode(frame):
            if code.data.decode('utf-8') not in used_codes:
                print("Authenticated!")
                print(code.data.decode('utf-8'))
                used_codes.append(code.data.decode('utf-8'))
                time.sleep(5)
            elif code.data.decode('utf-8') in used_codes:
                print("Already exsited! Try Again")
                time.sleep(5)

        cv2.imshow('Testing-code=scan', frame)
        cv2.waitKey(1) 
else:
    print("Try Again!")
    
