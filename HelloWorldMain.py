print("hello world")
print("Hi Matt")
print("Boo")

from tkinter import *           # Importing the Tkinter (tool box) library


def Pressed():  # function
    print ("buttons are cool")


root = Tk()  # main window
button = Button(root, text='Print in Console', command=Pressed)
button.pack(pady=50, padx=50)
Pressed()
root.mainloop()