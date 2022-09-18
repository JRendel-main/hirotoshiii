import tkinter as tk
from tkinter import ttk
from tkinter import *
import Email
import runpy
import customtkinter


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = receiver_email.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = bodyMsg.get()
	return userInput


# this is the function called when the button is clicked
def send_Email():
	runpy.run_path(path_name='Email.py')
root = customtkinter.CTk()

# This is the section of code which creates the main window
root.geometry('660x350')
root.configure(background='#F0F8FF')
root.title('QR Code Maker')
self.grid_columnconfigure(1, weight=1)
self.grid_rowconfigure(0, weight=1)

customtkinter.CTkLabel(master=root,text="CustomTkinter",text_font=("Roboto Medium", -16))

# This is the section of code which creates the a label
Label(root, text='Enter recepient email:', bg='#F0F8FF', font=('helvetica', 12, 'normal')).place(x=75, y=103)


# This is the section of code which creates the a label
Label(root, text='Enter message:', bg='#F0F8FF', font=('helvetica', 12, 'normal')).place(x=115, y=183)


# This is the section of code which creates a text input box
receiver_email=Entry(root)
receiver_email.place(x=275, y=103)


# This is the section of code which creates a text input box
bodyMsg=Entry(root)
bodyMsg.place(x=275, y=183)


# This is the section of code which creates a button
Button = customtkinter.CTkButton(master = root, text='Send', bg='#F0F8FF', command=send_Email)
Button.place(x=295, y=243, anchor=tk.CENTER)


root.mainloop()
