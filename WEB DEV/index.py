import random
import pyqrcode
import png
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
import time
import random
from tkinter import *

student_number = random.randint(100,100000)

student_lname = 0
student_number = 0
student_fname = 0
course = 0

def main():
    print("Hello Welcome to Student Management System")
    print("/*************************************************/")
    print("1. Register a New Student")
    print("2. Get QR Code for Student")
    print("3. Delete Student")
    print("4. Attendance Sheet for Student")
    print("/*************************************************/")
    
    userInputMain = input(str("Enter Here: "))
    
def regNewStudent():
    print("Hello Welcome to Student Management System")
    print("/*************************************************/")
    print("Register New Student")
    student_lname = input(str("Lastname: "))
    student_fname = input(str("Firstname: "))
    course = input(str("Course: "))
    print("/*************************************************/")

# Generate QRCode
def StudentCreateQR():
    url = pyqrcode.create(student_number)
    url.png("Student QRCode\ " + student_lname + ".png", scale = 6)

