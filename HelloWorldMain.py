from tkinter import *           # Importing the Tkinter (tool box) library


def Pressed():
    print ("Hello World")


root = Tk()  # main window

button = Button(root, text='Print in Console', command=Pressed)
button.pack(pady=150, padx=150)

#runs program
root.mainloop()