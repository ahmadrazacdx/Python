# Password Generator
from tkinter import *
import random as rd

def gen_pass():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    numbers = '0123456789'
    symbols = '[]{}()*/:;.,_-'
    all_chars = lower + upper + numbers + symbols
    length = 8
    password = "".join(rd.sample(all_chars, length))
    text_field.delete("1.0", END)
    text_field.insert(END, password)

root = Tk()
root.title("Password Generator")
root.geometry('280x110')
root.resizable(False,False)

text_field = Text(root, height=1.2, width=22,bd=2, highlightthickness=1, highlightbackground='gray')
text_field.pack(padx=10,pady=10)

button = Button(root, text='Generate', padx=30, pady=5, command=gen_pass,bd=2)
button.pack(padx=20, pady=10)

root.mainloop()
