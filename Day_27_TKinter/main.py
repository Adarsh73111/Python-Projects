# import tkinter
from tkinter import *
# window = tkinter.Tk()

def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
# my_label = tkinter.Label(text = "I am a Label", font=("Times New Roman",20))
my_label = Label(text = "I am a Label", font=("Times New Roman",20))
my_label.config(text="New Text")
# my_label.place(x=190, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Buttons
button = Button(text="Click", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)



window.mainloop()