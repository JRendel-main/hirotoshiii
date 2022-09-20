from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,9)
root.title("Youtube Downloader")

Label(root,text = 'Youtube Downloader', font='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Paste Link here: ', font= 'arial 15 bold'.place(x= 160 , y = 60))
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

