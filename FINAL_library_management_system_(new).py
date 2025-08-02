from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
from tkinter import messagebox
import webbrowser

mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
mycursor=mydb.cursor()

#1st window:LOGIN Pg -----------------------------------------------------------------------------------------------
root=Tk()
root.title("Login to the Library Management system")
root.geometry('680x250')

# Adding a background image
background_image=Image.open("lib1.jpg")   
background_image=background_image.resize((680,250),Image.ANTIALIAS)
img=ImageTk.PhotoImage(background_image)
Canvas1=Canvas(root)
Canvas1.configure(bg='black')
Canvas1.create_image(680,250,image=img,anchor=SE)
Canvas1.pack(expand=True,fill=BOTH)

#Login pg details
#mycursor.execute('create table login(username varchar(10) primary key,password varchar(10))')
headingFrame1=Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel=Label(headingFrame1,text='WELCOME TO LOGIN PAGE',bg='black',fg='white',font=('Courier',15))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

label1=Label(root,text='Login:',bg='black',fg='white',font=('Courier',15)).place(relx=0.01,rely=0.3)

label2=Label(root,text="Enter username:",bg='black',fg='white',font=('Courier',15)).place(relx=0.01,rely=0.45)
u=Entry(root,width=15,textvariable=StringVar(),font='bold')
u.place(relx=0.3,rely=0.45)

label3=Label(root,text='Enter password:',bg='black',fg='white',font=('Courier',15)).place(relx=0.01,rely=0.6)
p=Entry(root,width=15,textvariable=StringVar(),show='*',font='bold')
p.place(relx=0.3,rely=0.6)

def click():
    a=u.get()
    b=p.get()
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
    mycursor=mydb.cursor()
    mycursor.execute('select * from login')
    for i in mycursor:
        if(a==i[0] and b==i[1]):
            response=messagebox.showinfo('LOGIN STATUS','Login Successful')
            openmenu()
            break
        elif(a==i[0] and b!=i[1]):
            response=messagebox.showinfo('LOGIN STATUS','Invalid Password')
        elif(a!=i[0] and b==i[1]):
            response=messagebox.showinfo('LOGIN STATUS','Invalid Username')
        elif(a!=i[0] and b!=i[1]):
            response=messagebox.showinfo('LOGIN STATUS','Login Unsuccessful')
            
loginbutton=Button(root,text='LOGIN',bg='black',fg='white',font=('Courier',15),command=click).place(relx=0.65,rely=0.7)

label4=Label(root,text='By Maahira Begum CSE B',bg='black',fg='white',font=('Courier',12)).place(relx=0.65,rely=0.87)
#-----------------------------------------------------------

#2nd Window

def openmenu():
    top=Toplevel(root)
    top.title("Library management sysytem")
    top.geometry('1630x500')
    top.configure(bg='#a06c5f')
    
    headingFrame1=Frame(top,bg="#811112",bd=5)
    headingFrame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.16)
    MenuLabel=Label(headingFrame1,text='Select your choice from the given Menu',bg='black',fg='white',font=('Courier',20))
    MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
#------------------------------------------Book details
    
    def addbook():
        book1=Toplevel(top)
        book1.title('Add Book Detail')
        book1.geometry('1550x500')
        book1.configure(bg='#be9e85')

        headingFrame1=Frame(book1,bg='#6e5946',bd=5)
        headingFrame1.place(relx=0.26,rely=0.1,relwidth=0.465,relheight=0.154)
        MenuLabel=Label(headingFrame1,text='Add Book Detail',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        labelFrame=Frame(book1,bg='black')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
            
        #book details
        Book_no=Label(labelFrame,text="Book ID:",bg='black',fg='white',font='bold')
        Book_no.place(relx=0.05,rely=0.2,relheight=0.08)
            
        bi=Entry(labelFrame)
        bi.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)

        Book_name=Label(labelFrame,text="Book name:",bg='black',fg='white',font='bold')
        Book_name.place(relx=0.05,rely=0.35,relheight=0.08)
            
        bn=Entry(labelFrame)
        bn.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

        Author_name=Label(labelFrame,text="Author name:",bg='black',fg='white',font='bold')
        Author_name.place(relx=0.05,rely=0.50, relheight=0.08)
            
        an=Entry(labelFrame)
        an.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
            
        NB=Label(labelFrame,text="Number of books available:",bg='black',fg='white',font='bold')
        NB.place(relx=0.05,rely=0.65, relheight=0.08)
        nb=Entry(labelFrame)
        nb.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
        def addb():
            L=[]
            if(bn.get()==''):
                L.append((bi.get(),None,an.get(),nb.get()))
            elif(an.get()==''):
                L.append((bi.get(),bn.get(),None,nb.get()))
            elif(nb.get()==''):
                L.append((bi.get(),bn.get(),an.get(),None))
            else:
                L.append((bi.get(),bn.get(),an.get(),nb.get()))

            mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
            mycursor=mydb.cursor()
            #mycursor.execute('create table book_list(book_no int(3) primary key,book_name varchar(20),author_name varchar(20),no_of_books int(3))')
            sql='insert into book_list values(%s,%s,%s,%s)'
            mycursor.executemany(sql,L)
            mydb.commit()
            response=messagebox.showinfo('Add book detail','Successfully added')

            bi.delete(0,'end')
            bn.delete(0,'end')
            an.delete(0,'end')
            nb.delete(0,'end')
          
        b_add=Button(book1,text='Add',bg='black',fg='white',width=10,command=addb)
        b_add.place(relx=0.3,rely=0.85,relwidth=0.18,relheight=0.08)
        b_quit=Button(book1,text='Quit',bg='black',fg='white',width=10,command=book1.destroy)
        b_quit.place(relx=0.55,rely=0.85,relwidth=0.18,relheight=0.08)

    def showbook():
        book2=Toplevel(top)
        book2.title('Show Full Book Details')
        book2.geometry('1550x500')

        Canvas1 = Canvas(book2) 
        Canvas1.config(bg="#4c837a")
        Canvas1.pack(expand=True,fill=BOTH)

        headingFrame1 = Frame(book2,bg="#e1ddbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text="Book Details",bg='black',fg='white',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        labelFrame = Frame(book2,bg='black')
        labelFrame.place(relx=0.15,rely=0.3,relwidth=0.75,relheight=0.5)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        y=0.5
        try:
            mycursor.execute('select * from book_list')
            L=Label(book2,text="%-47s%-62s%-50s%-10s"%('Book ID','Book name','Author name','Number of books'),bg='black',fg='white',font='bold')
            L.place(relx=0.18,rely=0.35)
            row1=Label(book2,text='-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
            row1.place(relx=0.18,rely=0.45)
            for i in mycursor:
                C=Label(book2,text="%-70s%-90s%-75s%-10s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white')
                C.place(relx=0.18,rely=y)
                y+= 0.055
            row2=Label(book2,text='-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
            row2.place(relx=0.18,rely=y)
        except:
            messagebox.showinfo('Error','No Info Found')
        mydb.commit()
        b_quit=Button(book2,text='Quit',bg='black',fg='white',command=book2.destroy)
        b_quit.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    def updatebook():
        book3=Toplevel(top)
        book3.title('Update Book Detail')
        book3.geometry('600x400')
        book3.configure(bg='#c79f6c')

        headingFrame1=Frame(book3,bg='#dacab1',bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.65,relheight=0.2)
        MenuLabel=Label(headingFrame1,text='Update number of Books',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        Book_no=Label(book3,text='Enter Book name:',bg='#c79f6c',font=('Courier',15,'bold'))
        Book_no.place(relx=0.1,rely=0.35)
        bn=Entry(book3,width=35,font='bold')
        bn.place(relx=0.43,rely=0.35)

        NB=Label(book3,text='Enter Number of Books to add:',bg='#c79f6c',font=('Courier',15,'bold'))
        NB.place(relx=0.1,rely=0.5)
        nb=Entry(book3,width=5,font='bold')
        nb.place(relx=0.69,rely=0.5)

        def updateb():
            a=bn.get()
            b=nb.get()
            data=mycursor.execute("select no_of_books from book_list where book_name='"+a+"'")
            mydata=mycursor.fetchone()
            mydb.commit()
            if(b==''):
                messagebox.showinfo('Update book detail','No info updated')
            elif(b!=None):
                c=0
                for i in mydata:
                    c+=int(i)
                sum=int(c)+int(b)
                data=mycursor.execute("update book_list set no_of_books=%s where book_name=%s",(str(sum),str(a),))
                response=messagebox.showinfo('Update book detail','Successfully updated')
                mydb.commit()
            bn.delete(0,'end')
            nb.delete(0,'end')

        b_update=Button(book3,text='Update',bg='black',fg='white',font='bold',command=updateb)
        b_update.place(relx=0.2,rely=0.6,relwidth=0.18,relheight=0.08)
        b_quit=Button(book3,text='Quit',bg='black',fg='white',font='bold',command=book3.destroy)
        b_quit.place(relx=0.65,rely=0.6,relwidth=0.18,relheight=0.08)

    def delbook():
        book4=Toplevel(top)
        book4.title('Delete Book Detail')
        book4.geometry('500x400')
        book4.configure(bg='#163f3a')

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        headingFrame1=Frame(book4,bg='#f3eded',bd=5)
        headingFrame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.25)
        MenuLabel=Label(headingFrame1,text='Delete Book Detail',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        Book_name=Label(book4,text='Enter Book name:',bg='#163f3a',font=('Courier',15,'bold'))
        Book_name.place(relx=0.01,rely=0.45)
        bn=Entry(book4,width=30,font='bold')
        bn.place(relx=0.43,rely=0.45)
                
        def delb():
            mycursor.execute("delete from book_list where book_name='"+bn.get()+"'")
            mydb.commit()
            response=messagebox.showinfo('Delete book detail','Successfully deleted')
            bn.delete(0,'end')
            
        b_update=Button(book4,text='Delete',bg='black',fg='white',font='bold',command=delb)
        b_update.place(relx=0.25,rely=0.6,relwidth=0.18,relheight=0.08)
        b_quit=Button(book4,text='Quit',bg='black',fg='white',font='bold',command=book4.destroy)
        b_quit.place(relx=0.55,rely=0.6,relwidth=0.18,relheight=0.08)
            
    def searchbook():
        book5=Toplevel(top)
        book5.title('Search Book Detail')
        book5.geometry('1500x500')

        Canvas2=Canvas(book5) 
        Canvas2.config(bg="#e5771e")
        Canvas2.pack(expand=True,fill=BOTH)

        headingFrame1=Frame(book5,bg="#5a3d2b",bd=5)
        headingFrame1.place(relx=0.255,rely=0.1,relwidth=0.45,relheight=0.13)
        headingLabel=Label(headingFrame1,text="Search Book Details",bg='black',fg='white',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
                
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        Book_name=Label(book5,text='Enter Book name:',bg='#e5771e',font=('Courier',15,'bold'))
        Book_name.place(relx=0.27,rely=0.3)
        bn=Entry(book5,width=35,font='bold')
        bn.place(relx=0.43,rely=0.3)

        def searchb():
            labelFrame=Frame(book5,bg='black')
            labelFrame.place(relx=0.21,rely=0.5,relwidth=0.55,relheight=0.3)
            mycursor.execute("select * from book_list where book_name=%s",(str(bn.get()),))
            try:
                L=Label(book5,text="%-20s%-40s%-40s%-10s"%('Book ID','Name of the book','Author name','Number of books'),bg='black',fg='white',font='bold')
                L.place(relx=0.22,rely=0.55)
                row1=Label(book5,text='---------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
                row1.place(relx=0.22,rely=0.6)
                for i in mycursor:
                    L=Label(book5,text="%-25s%-47s%-45s%-10s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white',font='bold')
                    L.place(relx=0.22,rely=0.65)
                row2=Label(book5,text='---------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
                row2.place(relx=0.22,rely=0.7)
                mydb.commit()
            except:
                response=messagebox.showinfo("Error","No info found")
            bn.delete(0,'end') 
        b_search=Button(book5,text='Search',bg='black',fg='white',command=searchb)
        b_search.place(relx=0.3,rely=0.4,relwidth=0.18,relheight=0.08)
        b_quit=Button(book5,text='Quit',bg='black',fg='white',command=book5.destroy)
        b_quit.place(relx=0.49,rely=0.4,relwidth=0.18,relheight=0.08)

#-----------------------------------------------------------------------------------
        
    def webb():
        webbrowser.open_new('goodreads.com')

    def newsb():
        webbrowser.open_new('https://www.familysearch.org/wiki/en/Category:Newspapers')

#----------------------For New entry details:
        
    def addentry():
        entry1=Toplevel(top)
        entry1.title('Add Entry Detail')
        entry1.geometry('1700x600')
        entry1.configure(bg='#567570')

        headingFrame1=Frame(entry1,bg='#0c2925',bd=5)
        headingFrame1.place(relx=0.26,rely=0.1,relwidth=0.465,relheight=0.154)
        MenuLabel=Label(headingFrame1,text='Add Entry Detail',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        labelFrame=Frame(entry1,bg='black')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        #entry details
        entry_id=Label(labelFrame,text="Entry ID:",bg='black',fg='white',font='bold')
        entry_id.place(relx=0.02,rely=0.15,relheight=0.08)
        ei=Entry(labelFrame)
        ei.place(relx=0.3,rely=0.15,relwidth=0.62,relheight=0.08)

        entry_name=Label(labelFrame,text="Entry name:",bg='black',fg='white',font='bold')
        entry_name.place(relx=0.02,rely=0.3,relheight=0.08)
        en=Entry(labelFrame)
        en.place(relx=0.3,rely=0.3,relwidth=0.62,relheight=0.08)

        book_name=Label(labelFrame,text="Book name:",bg='black',fg='white',font='bold')
        book_name.place(relx=0.02,rely=0.45,relheight=0.08)
        bn=Entry(labelFrame)
        bn.place(relx=0.3,rely=0.45,relwidth=0.62,relheight=0.08)

        date_issue=Label(labelFrame,text='Date of issue (yyyy-mm-dd):',bg='black',fg='white',font='bold')
        date_issue.place(relx=0.02,rely=0.6,relheight=0.08)
        di=Entry(labelFrame)
        di.place(relx=0.3,rely=0.6,relwidth=0.62,relheight=0.08)

        date_return=Label(labelFrame,text='Date of return (yyyy-mm-dd):',bg='black',fg='white',font='bold')
        date_return.place(relx=0.02,rely=0.75,relheight=0.08)
        dr=Entry(labelFrame)
        dr.place(relx=0.3,rely=0.75,relwidth=0.62,relheight=0.08)

        def adde():
            L=[]
            if(en.get()==''):
                L.append((ei.get(),None,bn.get(),di.get(),dr.get()))
            elif(bn.get()==''):
                L.append((ei.get(),en.get(),None,di.get(),dr.get()))
            elif(dr.get()==''):
                L.append((ei.get(),en.get(),bn.get(),di.get(),None))
            else:
                 L.append((ei.get(),en.get(),bn.get(),di.get(),dr.get()))

            #mycursor.execute('create table entries(Sno int(3) primary key,Person_name varchar(20),Book_name varchar(20),Issue_date date,Return_date date)')
            sql='insert into entries values(%s,%s,%s,%s,%s)'
            mycursor.executemany(sql,L)
            mydb.commit()
            response=messagebox.showinfo('Add Entry detail','Successfully added')
            ei.delete(0,'end')
            en.delete(0,'end')
            bn.delete(0,'end')
            di.delete(0,'end')
            dr.delete(0,'end')
         
        e_add=Button(entry1,text='Add',bg='black',fg='white',width=10,command=adde)
        e_add.place(relx=0.26,rely=0.85,relwidth=0.18,relheight=0.08)
        e_quit=Button(entry1,text='Quit',bg='black',fg='white',width=10,command=entry1.destroy)
        e_quit.place(relx=0.55,rely=0.85,relwidth=0.18,relheight=0.08)

    def showentry():
        entry2=Toplevel(top)
        entry2.title('Show Full Entry Details')
        entry2.geometry('1500x500')

        Canvas1 = Canvas(entry2) 
        Canvas1.config(bg="#ac3834")
        Canvas1.pack(expand=True,fill=BOTH)

        headingFrame1 = Frame(entry2,bg="#610000",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text="Entry Details",bg='black',fg='white',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        labelFrame = Frame(entry2,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()
        y=0.45
        try:
            mycursor.execute('select * from entries')
            L=Label(entry2,text="%-23s%-39s%-60s%-55s%-20s"%('Sno.','Name','Book name','Issue date','Return date'),bg='black',fg='white',font='bold')
            L.place(relx=0.15,rely=0.33)
            row1=Label(entry2,text='------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
            row1.place(relx=0.15,rely=0.37)
            for i in mycursor:
                L = Label(entry2,text="%-35s%-55s%-83s%-75s%-20s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white')
                L.place(relx=0.15,rely=y)
                y+=0.045
            row2=Label(entry2,text='-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
            row2.place(relx=0.15,rely=y)
        except:
            # Need to insert if null statement
            messagebox.showinfo('Error','No Info Found')
        mydb.commit()
        e_quit=Button(entry2,text='Quit',bg='black',fg='white',command=entry2.destroy)
        e_quit.place(relx=0.4,rely=0.9,relwidth=0.18,relheight=0.08)
                
    def updateentry():
        entry3=Toplevel(top)
        entry3.title('Update Entry Detail')
        entry3.geometry('700x400')
        entry3.configure(bg='#b17c5c')

        headingFrame1=Frame(entry3,bg='#6e5946',bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.65,relheight=0.2)
        MenuLabel=Label(headingFrame1,text='Update Entry Details',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()
                
        entry_name=Label(entry3,text='Enter entry name:',bg='#b17c5c',font=('Courier',15,'bold'))
        entry_name.place(relx=0.15,rely=0.4)
        en=Entry(entry3,width=20,font='bold')
        en.place(relx=0.45,rely=0.4)

        DR=Label(entry3,text='Enter date of return(yyyy-mm-dd):',bg='#b17c5c',font=('Courier',15,'bold'))
        DR.place(relx=0.15,rely=0.5)
        dr=Entry(entry3,width=10,font='bold')
        dr.place(relx=0.72,rely=0.5)

        def updatee():
            a=en.get()
            b=dr.get()
            sql="update entries set Return_date=%s where person_name=%s"
            info=(str(b),str(a))
            mycursor.execute(sql,info)
            mydb.commit()
            response=messagebox.showinfo('Update entry detail','Successfully updated')
            en.delete(0,'end')
            dr.delete(0,'end')
             
        e_update=Button(entry3,text='Update',bg='black',fg='white',font='bold',command=updatee)
        e_update.place(relx=0.25,rely=0.65,relwidth=0.18,relheight=0.09)
        e_quit=Button(entry3,text='Quit',bg='black',fg='white',font='bold',command=entry3.destroy)
        e_quit.place(relx=0.6,rely=0.65,relwidth=0.18,relheight=0.09)
                
    def delentry():
        entry4=Toplevel(top)
        entry4.title('Delete Entry Detail')
        entry4.geometry('425x350')
        entry4.configure(bg='#073b5b')

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        headingFrame1=Frame(entry4,bg='#f3eded',bd=5)
        headingFrame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.25)
        MenuLabel=Label(headingFrame1,text='Delete Entry Detail',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        Entry_name=Label(entry4,text='Enter Entry name:',bg='#073b5b',font=('Courier',15,'bold'))
        Entry_name.place(relx=0.015,rely=0.45)
        en=Entry(entry4,width=16,font='bold')
        en.place(relx=0.51,rely=0.45)
                
        def dele():    
            mycursor.execute("delete from entries where person_name='"+en.get()+"'")
            mydb.commit()
            response=messagebox.showinfo('Delete entry detail','Successfully deleted')
            en.delete(0,'end')
            
        e_del=Button(entry4,text='Delete',bg='black',fg='white',font='bold',command=dele)
        e_del.place(relx=0.25,rely=0.6,relwidth=0.2,relheight=0.095)
        e_quit=Button(entry4,text='Quit',bg='black',fg='white',font='bold',command=entry4.destroy)
        e_quit.place(relx=0.5,rely=0.6,relwidth=0.2,relheight=0.095)

    def searchentry():
        entry5=Toplevel(top)
        entry5.title('Search Entry Detail')
        entry5.geometry('1300x500')

        Canvas2=Canvas(entry5) 
        Canvas2.config(bg="#e5771e")
        Canvas2.pack(expand=True,fill=BOTH)

        headingFrame1=Frame(entry5,bg="#f4a127",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.13)
        headingLabel=Label(headingFrame1,text="Search Entry Details",bg='black',fg='white',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
                
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        entry_name=Label(entry5,text='Enter entry name:',bg='#e5771e',font=('Courier',15,'bold'))
        entry_name.place(relx=0.3,rely=0.3)
        en=Entry(entry5,width=28,font='bold')
        en.place(relx=0.47,rely=0.3)

        def searche():
            labelFrame=Frame(entry5,bg='black')
            labelFrame.place(relx=0.2,rely=0.5,relwidth=0.6,relheight=0.3)
            mycursor.execute('select * from entries where person_name=%s',(str(en.get()),))
            try:
                L=Label(entry5,text="%-20s%-30s%-33s%-32s%-10s"%('Entry id','Entry name','Book name','Issue date','Return date'),bg='black',fg='white',font='bold')
                L.place(relx=0.23,rely=0.55)
                row1=Label(entry5,text='-----------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
                row1.place(relx=0.23,rely=0.6)
                for i in mycursor:
                    L=Label(entry5,text="%-24s%-32s%-32s%-30s%-10s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white',font='bold')
                    L.place(relx=0.23,rely=0.65)
                row2=Label(entry5,text='-----------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
                row2.place(relx=0.23,rely=0.7)
                mydb.commit()
            except:
                response=messagebox.showinfo("Error","No info found")
            en.delete(0,'end')
            
        e_search=Button(entry5,text='Search',bg='black',fg='white',command=searche)
        e_search.place(relx=0.3,rely=0.4,relwidth=0.18,relheight=0.08)
        e_quit=Button(entry5,text='Quit',bg='black',fg='white',command=entry5.destroy)
        e_quit.place(relx=0.49,rely=0.4,relwidth=0.18,relheight=0.08)

    def entrybkno():
        entry6=Toplevel(top)
        entry6.title('Show Full Entry Details')
        entry6.geometry('1500x500')

        Canvas1=Canvas(entry6) 
        Canvas1.config(bg="#b29576")
        Canvas1.pack(expand=True,fill=BOTH)

        headingFrame1 = Frame(entry6,bg="#5a3d2b",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text="Books Not Returned",bg='black',fg='white',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        labelFrame = Frame(entry6,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()
        y=0.45
        try:
            mycursor.execute('select * from entries where return_date is null')
            L=Label(entry6,text="%-10s%-50s%-60s%-30s%-20s"%('Sno.','Name','Book name','Issue date','Return date'),bg='black',fg='white',font='bold')
            L.place(relx=0.2,rely=0.35)
            row1=Label(entry6,text='---------------------------------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
            row1.place(relx=0.2,rely=0.4)
            for i in mycursor:
                L = Label(entry6,text="%-20s%-65s%-85s%-45s%-20s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white')
                L.place(relx=0.2,rely=y)
                y+=0.055
            row2=Label(entry6,text='----------------------------------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
            row2.place(relx=0.2,rely=y)
        except:
            messagebox.showinfo('Error','No Info Found')
        mydb.commit()
        e_quit=Button(entry6,text='Quit',bg='black',fg='white',command=entry6.destroy)
        e_quit.place(relx=0.4,rely=0.9,relwidth=0.18,relheight=0.08)

#------------------For membership details
        
    def addmembership():
        mem1=Toplevel(top)
        mem1.title('Add Membership Detail')
        mem1.geometry('1550x550')
        mem1.configure(bg='#04253a')

        headingFrame1=Frame(mem1,bg='#e1ddbf',bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        MenuLabel=Label(headingFrame1,text='Add Membership Detail',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        labelFrame=Frame(mem1,bg='black')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

        #membership details
        mem_id=Label(labelFrame,text="Membership ID:",bg='black',fg='white',font='bold')
        mem_id.place(relx=0.02,rely=0.2,relheight=0.08)
        mi=Entry(labelFrame)
        mi.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)

        mem_name=Label(labelFrame,text="Member name:",bg='black',fg='white',font='bold')
        mem_name.place(relx=0.02,rely=0.35,relheight=0.08)
        mn=Entry(labelFrame)
        mn.place(relx=0.3,rely=0.35,relwidth=0.62,relheight=0.08)

        mem_ph=Label(labelFrame,text="Member phone number:",bg='black',fg='white',font='bold')
        mem_ph.place(relx=0.02,rely=0.5,relheight=0.08)
        mp=Entry(labelFrame)
        mp.place(relx=0.3,rely=0.5,relwidth=0.62,relheight=0.08)

        date_join=Label(labelFrame,text='Date of join(yyyy-mm-dd):',bg='black',fg='white',font='bold')
        date_join.place(relx=0.02,rely=0.65,relheight=0.08)
        dj=Entry(labelFrame)
        dj.place(relx=0.3,rely=0.65,relwidth=0.62,relheight=0.08)

        def addm():
            L=[]
            if(mn.get()==''):
                L.append((mi.get(),None,mp.get(),dj.get()))
            elif(mp.get()==''):
                L.append((mi.get(),mn.get(),None,dj.get()))
            elif(dj.get()==''):
                L.append((mi.get(),mn.get(),mp.get(),None))
            elif(mn.get()==''and mp.get()==''):
                L.append((mi.get(),None,None,dj.get()))
            elif(mn.get()=='' and dj.get()==''):
                L.append((mi.get(),None,mp.get(),None))
            elif(mp.get()=='' and dj.get()==''):
                L.append((mi.get(),mn.get(),None,None))
            elif(mn.get()=='' and mp.get()=='' and dj.get()==''):
                L.append((mi.get(),None,None,None))
            else:
                L.append((mi.get(),mn.get(),mp.get(),dj.get()))
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
            mycursor=mydb.cursor()
            #mycursor.execute('create table entries(Name_id int(5) primary key,Name varchar(20),Phone int(12),Date_of_join date)')
            sql='insert into membership values(%s,%s,%s,%s)'
            mycursor.executemany(sql,L)
            mydb.commit()
            response=messagebox.showinfo('Add Membership detail','Successfully added')

            mi.delete(0,'end')
            mn.delete(0,'end')
            mp.delete(0,'end')
            dj.delete(0,'end')
            
        m_add=Button(mem1,text='Add',bg='black',fg='white',width=10,command=addm)
        m_add.place(relx=0.3,rely=0.85,relwidth=0.18,relheight=0.08)
        m_quit=Button(mem1,text='Quit',bg='black',fg='white',width=10,command=mem1.destroy)
        m_quit.place(relx=0.55,rely=0.85,relwidth=0.18,relheight=0.08)

    def showmembership():
        mem2=Toplevel(top)
        mem2.title('Show Full Membership Details')
        mem2.geometry('1500x500')

        Canvas1 = Canvas(mem2)
        Canvas1.config(bg="#3a6289")
        Canvas1.pack(expand=True,fill=BOTH)

        headingFrame1 = Frame(mem2,bg="#adc5ce",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text="Membership Details",bg='black',fg='white',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        labelFrame = Frame(mem2,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()
        y=0.45
        try:
            mycursor.execute('select * from membership')
            L=Label(mem2,text="%-35s%-50s%-55s%-20s"%('Sno.','Member name','Phone number','Date of join'),bg='black',fg='white',font='bold')
            L.place(relx=0.2,rely=0.35)
            row1=Label(mem2,text='---------------------------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
            row1.place(relx=0.2,rely=0.4)
            for i in mycursor:
                L = Label(mem2,text="%-50s%-79s%-83s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white')
                L.place(relx=0.2,rely=y)
                y+=0.055
            row2=Label(mem2,text='----------------------------------------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
            row2.place(relx=0.2,rely=y)
        except:
            messagebox.showinfo('Error','No Info Found')
        mydb.commit()
        e_quit=Button(mem2,text='Quit',bg='black',fg='white',command=mem2.destroy)
        e_quit.place(relx=0.4,rely=0.9,relwidth=0.18,relheight=0.08)
        
    def updatemembership():
        mem3=Toplevel(top)
        mem3.title('Update Membership Detail')
        mem3.geometry('650x400')
        mem3.configure(bg='#dcc4a2')

        headingFrame1=Frame(mem3,bg='#6e5946',bd=5)
        headingFrame1.place(relx=0.18,rely=0.1,relwidth=0.7,relheight=0.2)
        MenuLabel=Label(headingFrame1,text='Update Membership Details',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()
                       
        mem_no=Label(mem3,text='Enter member number:',bg='#dcc4a2',font=('Courier',15,'bold'))
        mem_no.place(relx=0.15,rely=0.35)
        mi=Entry(mem3,width=10,font='bold')
        mi.place(relx=0.54,rely=0.35)

        MN=Label(mem3,text='Enter member phone number:',bg='#dcc4a2',font=('Courier',15,'bold'))
        MN.place(relx=0.15,rely=0.5)
        mn=Entry(mem3,width=15,font='bold')
        mn.place(relx=0.65,rely=0.5)

        def updatem():
            a=mi.get()
            b=mn.get()
            mycursor.execute("update membership set phone=%s where name_id=%s"%(str(b),str(a)))
            mydb.commit()
            response=messagebox.showinfo('Update Membership detail','Successfully updated')
            mi.delete(0,'end')
            mn.delete(0,'end')
             
        m_update=Button(mem3,text='Update',bg='black',fg='white',font='bold',command=updatem)
        m_update.place(relx=0.3,rely=0.6,relwidth=0.18,relheight=0.08)
        m_quit=Button(mem3,text='Quit',bg='black',fg='white',font='bold',command=mem3.destroy)
        m_quit.place(relx=0.55,rely=0.6,relwidth=0.18,relheight=0.08)

    def delmembership():
        mem4=Toplevel(top)
        mem4.title('Delete Membership Detail')
        mem4.geometry('600x400')
        mem4.configure(bg='#558981')

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        headingFrame1=Frame(mem4,bg='#f3eded',bd=5)
        headingFrame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.25)
        MenuLabel=Label(headingFrame1,text='Delete Membership Detail',bg='black',fg='white',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        Mem_no=Label(mem4,text='Enter Member no:',bg='#558981',font=('Courier',15,'bold'))
        Mem_no.place(relx=0.2,rely=0.45)
        mn=Entry(mem4,width=10,font='bold')
        mn.place(relx=0.6,rely=0.45)
                
        def delm():
            a=mn.get()
            mycursor.execute("delete from membership where name_id="+str(a))
            mydb.commit()
            response=messagebox.showinfo('Delete Membership detail','Successfully deleted')
            mn.delete(0,'end')

        e_del=Button(mem4,text='Delete',bg='black',fg='white',font='bold',command=delm)
        e_del.place(relx=0.25,rely=0.6,relwidth=0.18,relheight=0.08)
        e_quit=Button(mem4,text='Quit',bg='black',fg='white',font='bold',command=mem4.destroy)
        e_quit.place(relx=0.55,rely=0.6,relwidth=0.18,relheight=0.08)

    def searchmembership():
        mem5=Toplevel(top)
        mem5.title('Search Membership Detail')
        mem5.geometry('1300x460')

        Canvas2=Canvas(mem5) 
        Canvas2.config(bg='#4c837a')
        Canvas2.pack(expand=True,fill=BOTH)

        headingFrame1=Frame(mem5,bg="#04253a",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.13)
        headingLabel=Label(headingFrame1,text="Search Membership Details",bg='black',fg='white',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='LMSdb')
        mycursor=mydb.cursor()

        mem_no=Label(mem5,text='Enter member number:',bg='#4c837a',font=('Courier',15,'bold'))
        mem_no.place(relx=0.35,rely=0.3)
        mn=Entry(mem5,width=8,font='bold')
        mn.place(relx=0.55,rely=0.3)

        def searchm():
            labelFrame=Frame(mem5,bg='black')
            labelFrame.place(relx=0.22,rely=0.5,relwidth=0.55,relheight=0.3)
            mycursor.execute('select * from membership where name_id=%s'%(str(mn.get())))
            try:
                L=Label(mem5,text="%-25s%-30s%-43s%-20s"%('Member id','Member name','Phone number','Date of join'),bg='black',fg='white',font='bold')
                L.place(relx=0.25,rely=0.55)
                row1=Label(mem5,text='----------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
                row1.place(relx=0.25,rely=0.6)
                for i in mycursor:
                    L=Label(mem5,text="%-30s%-40s%-43s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white',font='bold')
                    L.place(relx=0.25,rely=0.65)
                row2=Label(mem5,text='----------------------------------------------------------------------------------------------------------------------------',bg='black',fg='white',font='bold')
                row2.place(relx=0.25,rely=0.7)
                mydb.commit()
            except:
                response=messagebox.showinfo("Error","No info found")
            mn.delete(0,'end')
            
        m_search=Button(mem5,text='Search',bg='black',fg='white',command=searchm)
        m_search.place(relx=0.3,rely=0.4,relwidth=0.18,relheight=0.08)
        m_quit=Button(mem5,text='Quit',bg='black',fg='white',command=mem5.destroy)
        m_quit.place(relx=0.49,rely=0.4,relwidth=0.18,relheight=0.08)

#-----------------------------------------------------------------------------------
    
    add_book=Button(top,text="Add Book Detail",bg='black',fg='white',font='Courier',width=21,command=addbook)
    show_book=Button(top,text="Show Full Book Detail",bg='black',fg='white',font='Courier',width=21,command=showbook)
    update_book=Button(top,text="Update Book Detail",bg='black',fg='white',font='Courier',width=21,command=updatebook)
    del_book=Button(top,text="Delete Book Detail",bg='black',fg='white',font='Courier',width=21,command=delbook)
    search_book=Button(top,text="Search Book Detail",bg='black',fg='white',font='Courier',width=21,command=searchbook)
    bookr=Button(top,text="Search Books and Reviews",bg='black',fg='white',font='Courier',width=27,command=webb)
    news=Button(top,text="Search Historical Newspaper",bg='black',fg='white',font='Courier',width=27,command=newsb)
    add_entry=Button(top,text="Add Entry",bg='black',fg='white',font='Courier',width=21,command=addentry)
    show_entry=Button(top,text="Show Entry Detail",bg='black',fg='white',font='Courier',width=21,command=showentry)
    search_entry=Button(top,text="Search Entry Detail",bg='black',fg='white',font='Courier',width=21,command=searchentry)
    update_entry=Button(top,text="Update Entry Detail",bg='black',fg='white',font='Courier',width=21,command=updateentry)
    del_entry=Button(top,text="Delete Entry Detail",bg='black',fg='white',font='Courier',width=21,command=delentry)
    bkno_entry=Button(top,text="Books Not Returned",bg='black',fg='white',font='Courier',width=21,command=entrybkno)
    add_mem=Button(top,text="Add Membership Detail",bg='black',fg='white',font='Courier',width=24,command=addmembership)
    show_mem=Button(top,text="Show Membership Detail",bg='black',fg='white',font='Courier',width=24,command=showmembership)
    search_mem=Button(top,text="Search Membership Detail",bg='black',fg='white',font='Courier',width=24,command=searchmembership)
    update_mem=Button(top,text="Update Membership Detail",bg='black',fg='white',font='Courier',width=24,command=updatemembership)
    del_mem=Button(top,text="Delete Membership Detail",bg='black',fg='white',font='Courier',width=24,command=delmembership)
    quit_book=Button(top,text="Quit",bg='black',fg='white',font='Courier',command=root.destroy,width=20)
    
    BD=Label(top,text='-Book Details-',bg='black',fg='white',font=('Courier',15),width=23)
    BD.place(relx=0.002,rely=0.3)
    S=Label(top,text='-Supplements-',bg='black',fg='white',font=('Courier',15),width=29)
    S.place(relx=0.23,rely=0.3)
    ED=Label(top,text='-New Entry Details-',bg='black',fg='white',font=('Courier',15),width=23)
    ED.place(relx=0.515,rely=0.3)
    MD=Label(top,text='-Membership Details-',bg='black',fg='white',font=('Courier',15),width=26)
    MD.place(relx=0.743,rely=0.3)
    
    add_book.place(relx=0.002,rely=0.4)
    show_book.place(relx=0.002,rely=0.48)
    update_book.place(relx=0.002,rely=0.56)
    del_book.place(relx=0.002,rely=0.64)
    search_book.place(relx=0.002,rely=0.72)
    bookr.place(relx=0.23,rely=0.4)
    news.place(relx=0.23,rely=0.48)
    add_entry.place(relx=0.515,rely=0.4)
    show_entry.place(relx=0.515,rely=0.48)
    search_entry.place(relx=0.515,rely=0.56)
    update_entry.place(relx=0.515,rely=0.64)
    del_entry.place(relx=0.515,rely=0.72)
    bkno_entry.place(relx=0.515,rely=0.8)
    add_mem.place(relx=0.743,rely=0.4)
    show_mem.place(relx=0.743,rely=0.48)
    search_mem.place(relx=0.743,rely=0.56)
    update_mem.place(relx=0.743,rely=0.64)
    del_mem.place(relx=0.743,rely=0.72)
    quit_book.place(relx=0.4,rely=0.9)
        
#------------------------------------------------------------                

root.mainloop()
