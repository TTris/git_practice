
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk


window = Tk()
window.config(padx=100, pady=100)
window.title("Hello! How are you today?")


def plus():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    print(num1 + num2)
    label_hi = Label(text="Hello World! 🐥")
    label_hi.grid(row=1, columnspan=4)
    entry1.delete(0,"end")
    entry2.delete(0,"end")


entry1 = Entry(width=5)
entry1.grid(row=0, column=0)

label1 = Label(text="+")
label1.grid(row=0, column=1)

entry2 = Entry(width=5)
entry2.grid(row=0, column=2)

b = Button(text="=", command=plus)
b.grid(row=0, column=3)





window.mainloop()


