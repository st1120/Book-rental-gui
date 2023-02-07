from tkinter import *
from tkinter import messagebox
from datetime import *
from datetime import timedelta
from datetime import datetime
import pymysql
import time

mypass = "Sahil@2001"
mydatabase="bookmybook"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
issueTable = "books_issued" 
bookTable = "books"
stud="student"

allBid = [] 
def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1
    global status,inf3
    bid=inf1.get()
    issueto=inf2.get()
    sid=inf3.get()
    sname=issueto
    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    inf3.destroy()
    cur.execute("select title from books where bid ='"+ bid+"'")
    con.commit()
    for i in cur:
        bname=i[0]
    cur.execute("select bid from "+bookTable)
    con.commit()
    for i in cur:
        allBid.append(i[0])
    
    if bid in allBid:
        cur.execute("select status from "+bookTable+" where bid = '"+bid+"'")
        con.commit()
        for i in cur:
            check = i[0]
        if check == 'issued':
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
        else:
            status = True
    else:
        messagebox.showinfo("Error","Book ID not present")
    if status==True:
            cur.execute("update books set status = 'issued' where bid = '"+bid+"'")
            con.commit()
            cur.execute("insert into books_issued values ('"+bid+"','"+issueto+"')")
            con.commit()
            cur.execute("select author from books  where bid = '"+bid+"'")
            for i in cur:
                author = i[0]
            print(author)
            con.commit()
            cur.execute("insert into student values ('"+sid+"','"+sname+"','"+bid+"','"+bname+"','"+author+"')")
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
    cur.execute("select * from "+issueTable)
    con.commit()
    allBid.clear()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,inf3,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("BookMyBook")
    root.minsize(width=500,height=500)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="RENT BOOK", bg='black', fg='white', font=('Times New Roman',40))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='navy blue')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=(10))
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white',font=(10))
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    lb3 = Label(labelFrame,text="Student ID : ", bg='black', fg='white',font=(10))
    lb3.place(relx=0.05,rely=0.6)
        
    inf3 = Entry(labelFrame)
    inf3.place(relx=0.3,rely=0.6, relwidth=0.62)
    
    issueBtn = Button(root,text="Issue",bg='yellow', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='yellow', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()