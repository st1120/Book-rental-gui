from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from Student import *
mypass = "Sahil@2001"
mydatabase="bookmybook"

con = pymysql.connect(host="localhost",user="root",password="Sahil@2001",database="bookmybook")
cur = con.cursor()

root= Tk()
root.title("BookMyBook")
root.minsize(width=600,height=600)
root.geometry("1100x600")

img = ImageTk.PhotoImage(file="bg-1.jpg")

Canvas1 = Canvas(root)
Canvas1.create_image(700,340,image = img)      
Canvas1.config(bg="white")
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bd=0.5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="BookMyBook",bg='black',fg='cyan', font=('Times New Roman',60,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="ADD BOOK",bg='black', fg='yellow', command=addBook)
btn1.place(relx=0.1,rely=0.4, relwidth=0.2,relheight=0.1)
    
btn2 = Button(root,text="DELETE BOOK",bg='black', fg='yellow', command=delete)
btn2.place(relx=0.1,rely=0.6, relwidth=0.2,relheight=0.1)
    
btn3 = Button(root,text="VIEW BOOKS",bg='black', fg='yellow', command=View)
btn3.place(relx=0.1,rely=0.8, relwidth=0.2,relheight=0.1)
    
btn4 = Button(root,text="RENT BOOK",bg='black', fg='yellow', command = issueBook)
btn4.place(relx=0.7,rely=0.4, relwidth=0.2,relheight=0.1)
    
btn5 = Button(root,text="RETURN BOOK",bg='black', fg='yellow', command = returnBook)
btn5.place(relx=0.7,rely=0.6, relwidth=0.2,relheight=0.1)

btn6 = Button(root,text="VIEW RENTALS",bg='black', fg='yellow', command = viewStud)
btn6.place(relx=0.7,rely=0.8, relwidth=0.2,relheight=0.1)

root.mainloop()