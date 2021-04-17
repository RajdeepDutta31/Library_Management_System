from tkinter import *
import pandas as pd
#import os

path = "C:/Users/LENOVO/Desktop/Notes&Codes/Python_Projects/Library Management System/Issuedbookinfo.csv"
df = pd.read_csv(path)

my_root = Tk()
my_root.title("Return a Book")
my_root.geometry("400x400")
my_root.config(bg="Black")

l1 = Label(text = "Return Book", bg = "Black", fg= "Yellow")
l1.config(font=("Arial",20,"bold italic"))
l1.pack(pady= 15)

l2 = Label(text = "Book id", bg = "Black", fg= "Yellow")
l2.config(font=("Arial",10,"bold italic"))
l2.pack(pady= 1)

e1 = Entry()
e1.pack()

l3 = Label(text = "Student id", bg = "Black", fg= "Yellow")
l3.config(font=("Arial",10,"bold italic"))
l3.pack(pady= 15)

e2 = Entry()
e2.pack()

l4 = Label(text = "Return Date", bg = "Black", fg= "Yellow")
l4.config(font=("Arial",10,"bold italic"))
l4.pack(pady= 15)

e3 = Entry()
e3.pack()


def submit():
    df.drop(df[(df["Book id"] == e1.get()) & (df["Student's id"] == e2.get())].index, inplace = True)
    df.to_csv(path,index=False)
    sl = Label(text = "Returned Successfully", fg ="cyan", bg = "black")
    sl.pack(pady=1)

def back():
    my_root.destroy()

b1 = Button(text = "Back",command = back, fg ="Black", bg= "Yellow")
b1.pack(side = BOTTOM, pady = 5)

b1 = Button(text = "Submit",command = submit, fg ="Black", bg= "Yellow")
b1.pack(side = BOTTOM,pady = 5)

my_root.mainloop()
