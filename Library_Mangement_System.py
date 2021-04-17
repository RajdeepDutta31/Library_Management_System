#Library Management System
from tkinter import *
import os

my_root = Tk()
my_root.title("Library Management System")
my_root.geometry("500x550")
my_root.config(bg="Black")

l1 = Label(text = "Library Management System", bg = "Black", fg= "Yellow", relief = SUNKEN, borderwidth = 3)
l1.config(font=("Arial",20,"bold"))
l1.pack(pady= 15)

l2 = Label(text = "Welcome to the Library Management System of Havard University", bg = "Black", fg= "Yellow")
l2.config(font=("Arial",10,"bold italic"))
l2.pack()

def abook():
    os.system("add_book.py")
    
b1 = Button(text="Add Book",command = abook, fg = "Black", bg= "Yellow",relief = SUNKEN, borderwidth = 3)
b1.config(width = 20, font = ("Arial",10,"bold"))
b1.pack(pady = 40)

def sbook():
    os.system("search_book.py")
    
b2 = Button(text="Search a Book",command = sbook, fg = "Black", bg= "Yellow",relief = SUNKEN, borderwidth = 3)
b2.config(width = 20, font = ("Arial",10,"bold"))
b2.pack(pady = 4)

def b_list():
    os.system("book_list.py")

b3 = Button(text="Book List",command = b_list, fg = "Black", bg= "Yellow",relief = SUNKEN, borderwidth = 3)
b3.config(width = 20, font = ("Arial",10,"bold"))
b3.pack(pady = 40)

def issuebook():
    os.system("issue_a_book.py")

b4 = Button(text="Issue a Book",command = issuebook, fg = "Black", bg= "Yellow",relief = SUNKEN, borderwidth = 3)
b4.config(width = 20, font = ("Arial",10,"bold"))
b4.pack(pady = 10)

def returnbook():
    os.system("return_a_book.py")

b5 = Button(text="Return a Book",command = returnbook, fg = "Black", bg= "Yellow",relief = SUNKEN, borderwidth = 3)
b5.config(width = 20, font = ("Arial",10,"bold"))
b5.pack(pady = 40)


my_root.mainloop()
