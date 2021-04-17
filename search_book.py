from tkinter import *
import pandas as pd

path = "C:/Users/LENOVO/Desktop/Notes&Codes/Python_Projects/Library Management System/Library_info.csv"
df = pd.read_csv(path)

my_root = Tk()
my_root.title("Search a Book")
my_root.geometry("400x400")
my_root.config(bg="Black")

l1 = Label(text = "Search a Book", bg = "Black", fg= "Yellow")
l1.config(font=("Arial",20,"bold italic"))
l1.pack(pady= 15)

l2 = Label(text = "Enter the Book id", bg = "Black", fg= "Yellow")
l2.config(font=("Arial",10,"bold italic"))
l2.pack(pady= 15)

e1 = Entry()
e1.pack()

def search():
    book = df.loc[df["Book id"]==e1.get()]
    blvl = Label(text=book, fg = "yellow", bg="black")
    blvl.pack(pady=20)

def back():
    my_root.destroy()

b1 = Button(text = "Back",command=back, fg ="Black", bg= "Yellow")
b1.pack(side=BOTTOM, pady = 10)

b2 = Button(text = "Search",command=search, fg ="Black", bg= "Yellow")
b2.pack(side=BOTTOM, pady = 10)

my_root.mainloop()





