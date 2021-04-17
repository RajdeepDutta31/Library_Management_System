from tkinter import *
import pandas as pd

path = "C:/Users/LENOVO/Desktop/Notes&Codes/Python_Projects/Library Management System/Library_info.csv"
df = pd.read_csv(path)

my_root = Tk()
my_root.title("Book List")
my_root.geometry("600x600")
my_root.config(bg="Black")

l1 = Label(text = "Book List", relief = SUNKEN, bg = "Black", fg= "Yellow")
l1.config(font=("Arial",20,"bold italic"))
l1.pack(pady= 15)

dl = Label(text = df, bg = "Black", fg= "Yellow")
dl.pack()

def back():
    my_root.destroy()

b1 = Button(text = "Back", width = 10, command = back, fg = "black", bg = "yellow")
b1.pack(side = BOTTOM, pady =10)

my_root.mainloop()
