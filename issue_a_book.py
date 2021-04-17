from tkinter import *
import pandas as pd
import os

path = "C:/Users/LENOVO/Desktop/Notes&Codes/Python_Projects/Library Management System/Issuedbookinfo.csv"
df = pd.read_csv(path)

my_root = Tk()
my_root.title("Issue a Book")
my_root.geometry("400x550")
my_root.config(bg="Black")

l1 = Label(text = "Issue Book to Student", bg = "Black", fg= "Yellow")
l1.config(font=("Arial",20,"bold italic"))
l1.pack(pady= 15)

l2 = Label(text = "Book id", bg = "Black", fg= "Yellow")
l2.config(font=("Arial",10,"bold italic"))
l2.pack(pady= 1)

e1 = Entry()
e1.pack()

l3 = Label(text = "Student Name", bg = "Black", fg= "Yellow")
l3.config(font=("Arial",10,"bold italic"))
l3.pack(pady= 15)

e2 = Entry()
e2.pack()

l4 = Label(text = "Student id", bg = "Black", fg= "Yellow")
l4.config(font=("Arial",10,"bold italic"))
l4.pack(pady= 15)

e3 = Entry()
e3.pack()

l5 = Label(text = "Date of issue", bg = "Black", fg= "Yellow")
l5.config(font=("Arial",10,"bold italic"))
l5.pack(pady= 15)

e4 = Entry()
e4.pack()

l6 = Label(text ="Due Date", bg = "Black", fg= "Yellow")
l6.config(font=("Arial",10,"bold italic"))
l6.pack(pady= 15)

e5 = Entry()
e5.pack()

def submit():
    row = [pd.Series([e1.get(), e2.get(), e3.get(), e4.get(),e5.get()], index=df.columns)]
    n_df = df.append(row)
    n_df.to_csv(path, index=False)
    sl = Label(text = "Submitted Successfully", fg ="cyan", bg = "black")
    sl.pack(pady=1)

def ilist():
    os.system("issue_list.py")

def back():
    my_root.destroy()

b1 = Button(text = "Back",command = back, fg ="Black", bg= "Yellow")
b1.pack(side = BOTTOM, pady = 5)

b2 = Button(text = "Issued List",command = ilist, fg ="Black", bg= "Yellow")
b2.pack(side = BOTTOM,pady = 5)

b1 = Button(text = "Submit",command = submit, fg ="Black", bg= "Yellow")
b1.pack(side = BOTTOM,pady = 5)

my_root.mainloop()
