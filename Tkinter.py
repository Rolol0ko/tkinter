from tkinter import *
from tkinter import messagebox
import tkinter

#Variables
clicks = int(0)

def ButtonPress():
    global clicks
    clicks += 1
    print("button Pressed " + str(clicks) + " Times")

#set up window
root = Tk()
root.title("Clicks")
root.geometry("200x250")
root.resizable(False, False)

#Wiget set up
Widget1 = tkinter.Label(root, text="Hello World")
Widget1.pack(ipadx=10, ipady=10)

Widget2 = tkinter.Button(root, text="Button", command=ButtonPress)
Widget2.pack(ipadx=20, ipady=20, anchor=N) 

Widget3 = tkinter.Label(root, text="Button Was Clicked " + str(clicks) + " times")
Widget3.pack(ipadx=10,ipady=10)

#run the window
root.mainloop()