from tkinter import *
from tkinter import messagebox
import tkinter

def ButtonPress():
    print("button Pressed")
    
#set up window
root = Tk()
root.title("Tkinter test")
root.geometry("910x540")
root.resizable(False, False)

Widget1 = tkinter.Label(root, text="Hello World")
Widget1.pack(ipadx=10, ipady=10)

Widget2 = tkinter.Button(root, text="Button", command=ButtonPress())
Widget2.pack(ipadx=20, ipady=20, anchor=N) 

Widget3 = tkinter.Label(root, text="This is supposed to display button presses")
Widget3.pack(ipadx=10,ipady=10)

#run the window
root.mainloop()