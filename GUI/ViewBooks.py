from tkinter import *
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Sahil@2001"
mydatabase="bookmybook"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books" 
    
def View(): 
    
    root = Tk()
    root.title("BookMyBook")
    root.minsize(width=500,height=500)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="maroon")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="VIEW BOOKS", bg='black', fg='white', font=('Times New Roman',40))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-10s"%('BID'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="%-40s"%('Title'),bg='black',fg='white').place(relx=0.17,rely=0.1)
    Label(labelFrame, text="%-30s"%('Author'),bg='black',fg='white').place(relx=0.37,rely=0.1)
    Label(labelFrame, text="%-20s"%('Status'),bg='black',fg='white').place(relx=0.67,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s"%(i[0]),bg='black',fg='white').place(relx=0.07,rely=y)
            Label(labelFrame, text="%-40s"%(i[1]),bg='black',fg='white').place(relx=0.17,rely=y)
            Label(labelFrame, text="%-30s"%(i[2]),bg='black',fg='white').place(relx=0.37,rely=y)
            Label(labelFrame, text="%-20s"%(i[3]),bg='black',fg='white').place(relx=0.67,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='yellow', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()