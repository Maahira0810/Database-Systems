from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#1st window:LOGIN Pg -----------------------------------------------------------------------------------------------
root=Tk()
root.title("Login Page")
root.geometry('680x250')

# Adding a background image
background_image=Image.open("loginpaper1.png")#Canva bg
background_image=background_image.resize((680,250),Image.ANTIALIAS)
img=ImageTk.PhotoImage(background_image)
Canvas1=Canvas(root)
Canvas1.configure(bg='white')
Canvas1.create_image(680,250,image=img,anchor=SE)
Canvas1.pack(expand=True,fill=BOTH)

mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
mycursor=mydb.cursor()
#Login pg details
#mycursor.execute('create table login(username varchar(10) primary key,password varchar(10))')
headingFrame1=Frame(root,bg="white",bd=5)
headingFrame1.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.16)
headingLabel=Label(headingFrame1,text='WELCOME TO LOGIN PAGE',bg='white',fg='black',font=('Courier',15))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

label1=Label(root,text='Login:',bg='white',fg='black',font=('Courier',15)).place(relx=0.015,rely=0.25)

label2=Label(root,text="Enter username:",bg='white',fg='black',font=('Courier',15)).place(relx=0.015,rely=0.4)
u=Entry(root,width=15,textvariable=StringVar(),font='bold')
u.place(relx=0.3,rely=0.4)

label3=Label(root,text='Enter password:',bg='white',fg='black',font=('Courier',15)).place(relx=0.015,rely=0.54)
p=Entry(root,width=15,textvariable=StringVar(),show='*',font='bold')
p.place(relx=0.3,rely=0.54)

def click():
    a=u.get()
    b=p.get()
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
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
            
loginbutton=Button(root,text='LOGIN',bg='white',fg='black',font=('Courier',15),command=click).place(relx=0.01,rely=0.7)

label4=Label(root,text='By Maahira Begum and Joshitha N of CSE B',bg='white',fg='black',font=('Courier',12)).place(relx=0.01,rely=0.87)

#-----------------------------------------------------------------------------------------------------------------------2nd Window
    
def openmenu():
    top = Toplevel(root)
    top.title("Sales Management System")
    top.geometry('1630x500')
    top.configure(bg='#365438')

    # Load and set background image
    background_image = Image.open(r"M:\Sales management system\loginpaper.png")
    background_image = background_image.resize((1630, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas2 = Canvas(top, width=1630, height=500)
    Canvas2.create_image(0, 0, image=img, anchor=NW)
    Canvas2.image = img  # Keep a reference!
    Canvas2.pack(expand=True, fill=BOTH)

    # Heading Frame and Label
    headingFrame1 = Frame(top, bg="#67946b", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.16)

    MenuLabel = Label(headingFrame1, text='Select your choice from the given Menu', 
                      bg='white', fg='black', font=('Courier', 20))
    MenuLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
#-----------------------------------------------------------------------------------------------------------------------menus

    def addcus():
        cus1=Toplevel(top)
        cus1.title('Add Customer Detail')
        cus1.geometry('1550x500')
        cus1.configure(bg='#00563F')

        headingFrame1=Frame(cus1,bg='#D0F0C0',bd=5)
        headingFrame1.place(relx=0.26,rely=0.1,relwidth=0.465,relheight=0.154)
        MenuLabel=Label(headingFrame1,text='Add Customer Detail',bg='white',fg='black',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        labelFrame=Frame(cus1,bg='white')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
            
        #cus details
        cus_no=Label(labelFrame,text="Customer ID:",bg='white',fg='black',font='bold')
        cus_no.place(relx=0.05,rely=0.1,relheight=0.08)    
        ci=Entry(labelFrame)
        ci.place(relx=0.3,rely=0.1,relwidth=0.62,relheight=0.08)

        cus_name=Label(labelFrame,text="Customer name:",bg='white',fg='black',font='bold')
        cus_name.place(relx=0.05,rely=0.2,relheight=0.08) 
        cn=Entry(labelFrame)
        cn.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

        cus_date=Label(labelFrame,text="Date (yyyy-mm-dd):",bg='white',fg='black',font='bold')
        cus_date.place(relx=0.05,rely=0.3, relheight=0.08)   
        cd=Entry(labelFrame)
        cd.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
            
        cus_email=Label(labelFrame,text="Email:",bg='white',fg='black',font='bold')
        cus_email.place(relx=0.05,rely=0.4, relheight=0.08)
        ce=Entry(labelFrame)
        ce.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)

        cus_phone=Label(labelFrame,text="Phone no.:",bg='white',fg='black',font='bold')
        cus_phone.place(relx=0.05,rely=0.5, relheight=0.08)
        cp=Entry(labelFrame)
        cp.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)
        
        cus_payment=Label(labelFrame,text="Payment method:",bg='white',fg='black',font='bold')
        cus_payment.place(relx=0.05,rely=0.6, relheight=0.08)
        cpa=Entry(labelFrame)
        cpa.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

        cus_amount=Label(labelFrame,text="Amount paid:",bg='white',fg='black',font='bold')
        cus_amount.place(relx=0.05,rely=0.7, relheight=0.08)
        ca=Entry(labelFrame)
        ca.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)

        cus_state=Label(labelFrame,text="State:",bg='white',fg='black',font='bold')
        cus_state.place(relx=0.05,rely=0.8, relheight=0.08)
        cs=Entry(labelFrame)
        cs.place(relx=0.3,rely=0.8, relwidth=0.62, relheight=0.08)
        
        def addc():
            L=[]
            if(cn.get()==''):
                L.append((ci.get(),cd.get(),None,ce.get(),cp.get(),cpa.get(),ca.get(),cs.get()))
            elif(cd.get()==''):
                L.append((ci.get(),None,cn.get(),ce.get(),cp.get(),cpa.get(),ca.get(),cs.get()))
            elif(ce.get()==''):
                L.append((ci.get(),cd.get(),cn.get(),None,cp.get(),cpa.get(),ca.get(),cs.get()))
            elif(cp.get()==''):
                L.append((ci.get(),cd.get(),cn.get(),ce.get(),None,cpa.get(),ca.get(),cs.get()))
            elif(cpa.get()==''):
                L.append((ci.get(),cd.get(),cn.get(),ce.get(),cp.get(),None,ca.get(),cs.get()))
            elif(ca.get()==''):
                L.append((ci.get(),cd.get(),cn.get(),ce.get(),cp.get(),cpa.get(),None,cs.get()))
            elif(cs.get()==''):
                L.append((ci.get(),cd.get(),cn.get(),ce.get(),None,cp.get(),cpa.get(),ca.get(),None))
            else:
                L.append((ci.get(),cd.get(),cn.get(),ce.get(),cp.get(),cpa.get(),ca.get(),cs.get()))

            mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
            mycursor=mydb.cursor()
            #mycursor.execute('create table Customer_details(ID INT(11) NOT NULL PRIMARY KEY,Date DATE,C_name VARCHAR(20),Email VARCHAR(20),phone INT(11),payment_method VARCHAR(10),amount_paid DECIMAL(10,2),state VARCHAR(20)')
            sql='insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.executemany(sql,L)
            mydb.commit()
            response=messagebox.showinfo('Add Customer Detail','Successfully added')

            ci.delete(0,'end')
            cn.delete(0,'end')
            cd.delete(0,'end')
            ce.delete(0,'end')
            cp.delete(0,'end')
            cpa.delete(0,'end')
            ca.delete(0,'end')
            cs.delete(0,'end')
          
        c_add=Button(cus1,text='Add',bg='white',fg='black',width=10,command=addc)
        c_add.place(relx=0.3,rely=0.85,relwidth=0.18,relheight=0.08)
        c_quit=Button(cus1,text='Quit',bg='white',fg='black',width=10,command=cus1.destroy)
        c_quit.place(relx=0.55,rely=0.85,relwidth=0.18,relheight=0.08)
            
    def showcus():
        cus2=Toplevel(top)
        cus2.title('Show Full Customer Details')
        cus2.geometry('1550x500')

        Canvas1 = Canvas(cus2) 
        Canvas1.config(bg="#4c837a")
        Canvas1.pack(expand=True,fill=BOTH)

        headingFrame1 = Frame(cus2,bg="#e1ddbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text="Customer Details",bg='white',fg='black',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        labelFrame = Frame(cus2,bg='white')
        labelFrame.place(relx=0.04,rely=0.3,relwidth=0.9,relheight=0.5)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()

        y=0.5
        try:
            mycursor.execute('select * from customer_details')
            L=Label(cus2,text="%-10s%-10s%-18s%-25s%-20s%-20s%-20s%-10s"%('ID','Date','Customer name','Email','Phone','Payment Method','Amount Paid','State'),bg='white',fg='black',font='bold')
            L.place(relx=0.04,rely=0.35)
            row1=Label(cus2,text='------------------------------------------------------------------------------------------------------------------------------------------------------------------',bg='white',fg='black',font='bold')
            row1.place(relx=0.05,rely=0.45)
            for i in mycursor:
                C=Label(cus2,text="%-20s%-20s%-50s%-35s%-50s%-55s%-40s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]),bg='white',fg='black')
                C.place(relx=0.05,rely=y)
                y+= 0.055
            row2=Label(cus2,text='------------------------------------------------------------------------------------------------------------------------------------------------------------------',bg='white',fg='black',font='bold')
            row2.place(relx=0.05,rely=y)
        except:
            messagebox.showinfo('Error','No Info Found')
        mydb.commit()
        c_quit=Button(cus2,text='Quit',bg='white',fg='black',command=cus2.destroy)
        c_quit.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    def updatecus():
        cus3=Toplevel(top)
        cus3.title('Update Customer Detail')
        cus3.geometry('600x400')
        cus3.configure(bg='#9DC183')

        headingFrame1=Frame(cus3,bg='#043927',bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.65,relheight=0.2)
        MenuLabel=Label(headingFrame1,text='Update Phone Number',bg='white',fg='black',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()

        cus_no=Label(cus3,text='Enter initial phone no.:',bg='#9DC183',font=('Courier',15,'bold'))
        cus_no.place(relx=0.1,rely=0.35)
        cn=Entry(cus3,width=15,font='bold')
        cn.place(relx=0.6,rely=0.35)

        NB=Label(cus3,text='Enter new phone no.:',bg='#9DC183',font=('Courier',15,'bold'))
        NB.place(relx=0.1,rely=0.5)
        nb=Entry(cus3,width=15,font='bold')
        nb.place(relx=0.51,rely=0.5)

        def updatec():
            a=bn.get()
            b=nb.get()
            data=mycursor.execute("select * from customer_details where phone='"+a+"'")
            mydata=mycursor.fetchone()
            mydb.commit()
            if(b==''):
                messagebox.showinfo('Update Customer Detail','No info updated')
            elif(b!=None):
                data=mycursor.execute("update customer_details set phone=%s where phone=%s",(str(b),str(a),))
                response=messagebox.showinfo('Update Customer Detail','Successfully updated')
                mydb.commit()
            bn.delete(0,'end')
            nb.delete(0,'end')

        c_update=Button(cus3,text='Update',bg='white',fg='black',font='bold',command=updatec)
        c_update.place(relx=0.2,rely=0.6,relwidth=0.18,relheight=0.08)
        c_quit=Button(cus3,text='Quit',bg='white',fg='black',font='bold',command=cus3.destroy)
        c_quit.place(relx=0.65,rely=0.6,relwidth=0.18,relheight=0.08)

    def delcus():
        cus4=Toplevel(top)
        cus4.title('Delete Customer Detail')
        cus4.geometry('700x250')
        cus4.configure(bg='#689268')

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()

        headingFrame1=Frame(cus4,bg='#3F704D',bd=5)
        headingFrame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.25)
        MenuLabel=Label(headingFrame1,text='Delete Customer Detail',bg='white',fg='black',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        cus_no=Label(cus4,text='Enter Customer Phone no.:',bg='#689268',font=('Courier',15,'bold'))
        cus_no.place(relx=0.15,rely=0.45)
        cn=Entry(cus4,width=15,font='bold')
        cn.place(relx=0.6,rely=0.45)
                
        def delc():
            mycursor.execute("delete from customer_details where phone='"+cn.get()+"'")
            mydb.commit()
            response=messagebox.showinfo('Delete Customer Detail','Successfully deleted')
            cn.delete(0,'end')
            
        c_delete=Button(cus4,text='Delete',bg='white',fg='black',font='bold',command=delc)
        c_delete.place(relx=0.25,rely=0.65,relwidth=0.18,relheight=0.08)
        c_quit=Button(cus4,text='Quit',bg='white',fg='black',font='bold',command=cus4.destroy)
        c_quit.place(relx=0.55,rely=0.65,relwidth=0.18,relheight=0.08)
        
#----------------------------------------------------------product details
    def addpro():
        product1=Toplevel(top)
        product1.title('Add Product Detail')
        product1.geometry('1550x500')
        product1.configure(bg='#00563F')

        headingFrame1=Frame(product1,bg='#D0F0C0',bd=5)
        headingFrame1.place(relx=0.26,rely=0.1,relwidth=0.465,relheight=0.154)
        MenuLabel=Label(headingFrame1,text='Add Product Detail',bg='white',fg='black',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        labelFrame=Frame(product1,bg='white')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
            
        #product details
        product_no=Label(labelFrame,text="Product ID:",bg='white',fg='black',font='bold')
        product_no.place(relx=0.05,rely=0.2,relheight=0.08)   
        pi=Entry(labelFrame)
        pi.place(relx=0.35,rely=0.2,relwidth=0.62,relheight=0.08)

        product_name=Label(labelFrame,text="Product name:",bg='white',fg='black',font='bold')
        product_name.place(relx=0.05,rely=0.35,relheight=0.08)  
        pn=Entry(labelFrame)
        pn.place(relx=0.35,rely=0.35, relwidth=0.62, relheight=0.08)

        product_price=Label(labelFrame,text="Product Price:",bg='white',fg='black',font='bold')
        product_price.place(relx=0.05,rely=0.50, relheight=0.08) 
        pp=Entry(labelFrame)
        pp.place(relx=0.35,rely=0.50, relwidth=0.62, relheight=0.08)

        product_stock=Label(labelFrame,text="Quantity of Product in Stock:",bg='white',fg='black',font='bold')
        product_stock.place(relx=0.05,rely=0.65, relheight=0.08) 
        pq=Entry(labelFrame)
        pq.place(relx=0.35,rely=0.65, relwidth=0.62, relheight=0.08)

        def addp():
            L=[]
            if(pn.get()==''):
                L.append((pi.get(),None,pp.get(),pq.get()))
            elif(pp.get()==''):
                L.append((pi.get(),pn.get(),None,pq.get()))
            elif(pq.get()==''):
                L.append((pi.get(),pn.get(),pp.get(),None))
            else:
                L.append((pi.get(),pn.get(),pp.get(),pq.get()))

            mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
            mycursor=mydb.cursor()
            #mycursor.execute('create table Product_details (ID INT(11) NOT NULL PRIMARY KEY, P_name VARCHAR(20), price DECIMAL(6,2), Quantity_In_Stock INT(11))')
            sql='insert into product_details values(%s,%s,%s,%s)'
            mycursor.executemany(sql,L)
            mydb.commit()
            response=messagebox.showinfo('Add Product Detail','Successfully added')

            pi.delete(0,'end')
            pn.delete(0,'end')
            pp.delete(0,'end')
            pq.delete(0,'end')
          
        p_add=Button(product1,text='Add',bg='white',fg='black',width=10,command=addp)
        p_add.place(relx=0.3,rely=0.85,relwidth=0.18,relheight=0.08)
        p_quit=Button(product1,text='Quit',bg='white',fg='black',width=10,command=product1.destroy)
        p_quit.place(relx=0.55,rely=0.85,relwidth=0.18,relheight=0.08)
        
    def showpro():
        product2=Toplevel(top)
        product2.title('Show Full product Details')
        product2.geometry('1550x500')

        Canvas1 = Canvas(product2) 
        Canvas1.config(bg="#4c837a")
        Canvas1.pack(expand=True,fill=BOTH)

        headingFrame1 = Frame(product2,bg="#e1ddbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text="Product Details",bg='white',fg='black',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        labelFrame = Frame(product2,bg='white')
        labelFrame.place(relx=0.15,rely=0.3,relwidth=0.75,relheight=0.55)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()

        y=0.5
        try:
            mycursor.execute('select * from product_details')
            L=Label(product2,text="%-25s%-40s%-40s%-10s"%('ID','Product name','Price','Quantity in Stock'),bg='white',fg='black',font='bold')
            L.place(relx=0.17,rely=0.315)
            row1=Label(product2,text='------------------------------------------------------------------------------------------------------------------------------------',bg='white',fg='black',font='bold')
            row1.place(relx=0.17,rely=0.37)
            y=0.45
            for i in mycursor:
                C=Label(product2,text="%-51s%-101s%-70s%-1s"%(i[0],i[1],i[2],i[3]),bg='white',fg='black')
                C.place(relx=0.17,rely=y)
                y+= 0.055
            row2=Label(product2,text='------------------------------------------------------------------------------------------------------------------------------------',bg='white',fg='black',font='bold')
            row2.place(relx=0.17,rely=y)
        except:
            messagebox.showinfo('Error','No Info Found')
        mydb.commit()
        c_quit=Button(product2,text='Quit',bg='white',fg='black',command=product2.destroy)
        c_quit.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
        
    def updatepro():
        product3=Toplevel(top)
        product3.title('Update Customer Detail')
        product3.geometry('600x300')
        product3.configure(bg='#9DC183')

        headingFrame1=Frame(product3,bg='#043927',bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.65,relheight=0.2)
        MenuLabel=Label(headingFrame1,text='Update Phone Number',bg='white',fg='black',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()

        pro_no=Label(product3,text='Enter product no.:',bg='#9DC183',font=('Courier',15,'bold'))
        pro_no.place(relx=0.2,rely=0.35)
        pn=Entry(product3,width=5,font='bold')
        pn.place(relx=0.6,rely=0.35)

        pro_pr=Label(product3,text='Enter new price.:',bg='#9DC183',font=('Courier',15,'bold'))
        pro_pr.place(relx=0.2,rely=0.5)
        pp=Entry(product3,width=5,font='bold')
        pp.place(relx=0.55,rely=0.5)

        NB=Label(product3,text='Enter updated quantity no.:',bg='#9DC183',font=('Courier',15,'bold'))
        NB.place(relx=0.2,rely=0.6)
        nb=Entry(product3,width=5,font='bold')
        nb.place(relx=0.75,rely=0.6)

        def updatep():
            a=pn.get()
            b=pp.get()
            c=nb.get()
            data=mycursor.execute("select * from product_details where id='"+a+"'")
            mydata=mycursor.fetchone()
            mydb.commit()
            if(b==''and c==''):
                messagebox.showinfo('Update Product Detail','No info updated')
            elif(b==''):
                no=int(c)
                no+=mydata[3]
                c=str(no)
                b=mydata[2]
                data=mycursor.execute("update product_details set price=%s where id=%s",(str(b),str(a),))
                data=mycursor.execute("update product_details set quantity_in_stock=%s where id=%s",(str(c),str(a),))
                response=messagebox.showinfo('Update Customer Detail','Successfully updated')
                mydb.commit()
            elif(c==''):
                no=int(b)
                no+=mydata[2]
                b=str(no)
                c=mydata[3]
                data=mycursor.execute("update product_details set price=%s where id=%s",(str(b),str(a),))
                data=mycursor.execute("update product_details set quantity_in_stock=%s where id=%s",(str(c),str(a),))
                response=messagebox.showinfo('Update Customer Detail','Successfully updated')
                mydb.commit()
            else:
                no=int(b)
                no+=mydata[2]
                b=str(no)
                nu=int(c)
                nu+=mydata[3]
                c=str(nu)
                data=mycursor.execute("update product_details set price=%s where id=%s",(str(b),str(a),))
                data=mycursor.execute("update product_details set quantity_in_stock=%s where id=%s",(str(c),str(a),))
                response=messagebox.showinfo('Update Customer Detail','Successfully updated')
                mydb.commit()
        pn.delete(0,'end')
        pp.delete(0,'end')
        nb.delete(0,'end')

        c_update=Button(product3,text='Update',bg='white',fg='black',font='bold',command=updatep)
        c_update.place(relx=0.3,rely=0.75,relwidth=0.18,relheight=0.08)
        c_quit=Button(product3,text='Quit',bg='white',fg='black',font='bold',command=product3.destroy)
        c_quit.place(relx=0.6,rely=0.75,relwidth=0.18,relheight=0.08)
    def delpro():
        product4=Toplevel(top)
        product4.title('Delete Product Detail')
        product4.geometry('700x250')
        product4.configure(bg='#689268')

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()

        headingFrame1=Frame(product4,bg='#3F704D',bd=5)
        headingFrame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.25)
        MenuLabel=Label(headingFrame1,text='Delete Product Detail',bg='white',fg='black',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        pro_no=Label(product4,text='Enter Product ID:',bg='#689268',font=('Courier',15,'bold'))
        pro_no.place(relx=0.3,rely=0.45)
        pn=Entry(product4,width=5,font='bold')
        pn.place(relx=0.6,rely=0.45)
                
        def delp():
            mycursor.execute("delete from product_details where ID='"+pn.get()+"'")
            mydb.commit()
            response=messagebox.showinfo('Delete Product Detail','Successfully deleted')
            pn.delete(0,'end')
            
        p_delete=Button(product4,text='Delete',bg='white',fg='black',font='bold',command=delp)
        p_delete.place(relx=0.25,rely=0.6,relwidth=0.18,relheight=0.08)
        p_quit=Button(product4,text='Quit',bg='white',fg='black',font='bold',command=product4.destroy)
        p_quit.place(relx=0.55,rely=0.6,relwidth=0.18,relheight=0.08)
        
#----------------------------------------------------------sales details     
    def addsales():
        sales1=Toplevel(top)
        sales1.title('Add Sales Detail')
        sales1.geometry('1550x500')
        sales1.configure(bg='#00563F')

        headingFrame1=Frame(sales1,bg='#D0F0C0',bd=5)
        headingFrame1.place(relx=0.26,rely=0.1,relwidth=0.465,relheight=0.154)
        MenuLabel=Label(headingFrame1,text='Add Sales Detail',bg='white',fg='black',font=('Courier',20))
        MenuLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

        labelFrame=Frame(sales1,bg='white')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
            
        #sales details
        product_no=Label(labelFrame,text="Product ID:",bg='white',fg='black',font='bold')
        product_no.place(relx=0.05,rely=0.2,relheight=0.08)
        pi=Entry(labelFrame)
        pi.place(relx=0.3,rely=0.2,relwidth=0.62,relheight=0.08)

        product_name=Label(labelFrame,text="Product name:",bg='white',fg='black',font='bold')
        product_name.place(relx=0.05,rely=0.35,relheight=0.08)  
        pn=Entry(labelFrame)
        pn.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

        sales_profit=Label(labelFrame,text="Sales Profit:",bg='white',fg='black',font='bold')
        sales_profit.place(relx=0.05,rely=0.50, relheight=0.08) 
        sp=Entry(labelFrame)
        sp.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

        avg_review=Label(labelFrame,text="Average Review:",bg='white',fg='black',font='bold')
        avg_review.place(relx=0.05,rely=0.65, relheight=0.08)   
        ar=Entry(labelFrame)
        ar.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

        def adds():
            L=[]
            if(pn.get()==''):
                L.append((pi.get(),None,sp.get(),pq.get()))
            elif(sp.get()==''):
                L.append((pi.get(),pn.get(),None,pq.get()))
            elif(ar.get()==''):
                L.append((pi.get(),pn.get(),sp.get(),None))
            else:
                L.append((pi.get(),pn.get(),sp.get(),ar.get()))

            mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
            mycursor=mydb.cursor()
            #mycursor.execute('create table sales_details(P_ID INT(11) NOT NULL PRIMARY KEY,P_name VARCHAR(20),Sales_Profit DECIMAL(3,2),Avg_Review CHAR(10))')
            sql='insert into sales_details values(%s,%s,%s,%s)'
            mycursor.executemany(sql,L)
            mydb.commit()
            response=messagebox.showinfo('Add Sales Detail','Successfully added')

            pi.delete(0,'end')
            pn.delete(0,'end')
            sp.delete(0,'end')
            ar.delete(0,'end')
          
        s_add=Button(sales1,text='Add',bg='white',fg='black',width=10,command=adds)
        s_add.place(relx=0.3,rely=0.85,relwidth=0.18,relheight=0.08)
        s_quit=Button(sales1,text='Quit',bg='white',fg='black',width=10,command=sales1.destroy)
        s_quit.place(relx=0.55,rely=0.85,relwidth=0.18,relheight=0.08)
                
    def showsales():
        sales2=Toplevel(top)
        sales2.title('Show Full Sales Details')
        sales2.geometry('1550x500')

        Canvas1 = Canvas(sales2) 
        Canvas1.config(bg="#4c837a")
        Canvas1.pack(expand=True,fill=BOTH)

        headingFrame1 = Frame(sales2,bg="#e1ddbf",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1,text="Sales Details",bg='white',fg='black',font =('Courier',15))
        headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        labelFrame = Frame(sales2,bg='white')
        labelFrame.place(relx=0.15,rely=0.3,relwidth=0.75,relheight=0.5)

        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()

        y=0.5
        try:
            mycursor.execute('select * from sales_details')
            L=Label(sales2,text="%-25s%-40s%-40s%-10s"%('ID','Product name','Sales Profit','Avg Review'),bg='white',fg='black',font='bold')
            L.place(relx=0.17,rely=0.315)
            row1=Label(sales2,text='------------------------------------------------------------------------------------------------------------------------------------',bg='white',fg='black',font='bold')
            row1.place(relx=0.17,rely=0.37)
            y=0.45
            for i in mycursor:
                C=Label(sales2,text="%-50s%-90s%-75s%-10s"%(i[0],i[1],i[2],i[3]),bg='white',fg='black')
                C.place(relx=0.17,rely=y)
                y+= 0.055
            row2=Label(sales2,text='------------------------------------------------------------------------------------------------------------------------------------',bg='white',fg='black',font='bold')
            row2.place(relx=0.17,rely=y)
        except:
            messagebox.showinfo('Error','No Info Found')
        mydb.commit()
        c_quit=Button(sales2,text='Quit',bg='white',fg='black',command=sales2.destroy)
        c_quit.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
        
#-------------------------------------------------Charts
    def view_charts_p():
        chart1= Toplevel(top)
        chart1.title("Chart For Product vs Price")
        chart1.geometry('600x480')
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()
        mycursor.execute("SELECT p_name, price FROM product_details")
        data = mycursor.fetchall()
        mydb.commit()
        x = [row[0] for row in data]
        y = [row[1] for row in data]

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        canvas = FigureCanvasTkAgg(fig, master=chart1)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=1, column=0, columnspan=2)

    def view_charts_s():
        chart2= Toplevel(top)
        chart2.title("Chart For Product vs Sales Profit")
        chart2.geometry('600x480')
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()
        mycursor.execute("SELECT p_name,Sales_Profit FROM sales_details")
        data = mycursor.fetchall()
        mydb.commit()
        x = [row[0] for row in data]
        y = [row[1] for row in data]

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        canvas = FigureCanvasTkAgg(fig, master=chart2)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=1, column=0, columnspan=2)
        
    def view_charts_a():
        chart2= Toplevel(top)
        chart2.title("Chart For Product vs Sales Profit")
        chart2.geometry('600x480')
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='salesdb')
        mycursor=mydb.cursor()
        mycursor.execute("SELECT p_name,Avg_review FROM sales_details")
        data = mycursor.fetchall()
        mydb.commit()
        x = [row[0] for row in data]
        y = [row[1] for row in data]

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        canvas = FigureCanvasTkAgg(fig, master=chart2)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=1, column=0, columnspan=2)
        
#-----------------------------------------------------------------------------------
    add_cus=Button(top,text="Add Customer Detail",bg='white',fg='black',font='Courier',width=22,command=addcus)
    show_cus=Button(top,text="Show Customer Detail",bg='white',fg='black',font='Courier',width=22,command=showcus)
    update_cus=Button(top,text="Update Customer Detail",bg='white',fg='black',font='Courier',width=22,command=updatecus)
    del_cus=Button(top,text="Delete Customer Detail",bg='white',fg='black',font='Courier',width=22,command=delcus)
    add_pro=Button(top,text="Add Product Detail",bg='white',fg='black',font='Courier',width=21,command=addpro)
    show_pro=Button(top,text="Show Product Detail",bg='white',fg='black',font='Courier',width=21,command=showpro)
    update_pro=Button(top,text="Update Product Detail",bg='white',fg='black',font='Courier',width=21,command=updatepro)
    del_pro=Button(top,text="Delete Product Detail",bg='white',fg='black',font='Courier',width=21,command=delpro)
    add_sales=Button(top,text="Add Sales Detail",bg='white',fg='black',font='Courier',width=21,command=addsales)
    show_sales=Button(top,text="Show Sales Detail",bg='white',fg='black',font='Courier',width=21,command=showsales)
    view_pvp=Button(top,text="Product vs Price",bg='white',fg='black',font='Courier',width=24,command=view_charts_p)
    view_pvs=Button(top,text="Product vs Sales Profit",bg='white',fg='black',font='Courier',width=24,command=view_charts_s)
    view_pva=Button(top,text="Product vs Review",bg='white',fg='black',font='Courier',width=24,command=view_charts_a)
    quit_sales=Button(top,text="Quit",bg='white',fg='black',font='Courier',command=root.destroy,width=21)

    CD=Label(top,text='-Customer Details-',bg='white',fg='black',font=('Courier',15),width=24)
    CD.place(relx=0.01,rely=0.3)
    PD=Label(top,text='-Product Details-',bg='white',fg='black',font=('Courier',15),width=23)
    PD.place(relx=0.26,rely=0.3)
    SO=Label(top,text='-Sales Order-',bg='white',fg='black',font=('Courier',15),width=23)
    SO.place(relx=0.5,rely=0.3)
    CF=Label(top,text='-Demographic View-',bg='white',fg='black',font=('Courier',15),width=26)
    CF.place(relx=0.738,rely=0.3)

    add_cus.place(relx=0.01,rely=0.4)
    show_cus.place(relx=0.01,rely=0.48)
    update_cus.place(relx=0.01,rely=0.56)
    del_cus.place(relx=0.01,rely=0.64)
    add_pro.place(relx=0.26,rely=0.4)
    show_pro.place(relx=0.26,rely=0.48)
    del_pro.place(relx=0.26,rely=0.56)
    add_sales.place(relx=0.5,rely=0.4)
    show_sales.place(relx=0.5,rely=0.48)
    view_pvp.place(relx=0.738,rely=0.4)
    view_pvs.place(relx=0.738,rely=0.48)
    view_pva.place(relx=0.738,rely=0.56)
    quit_sales.place(relx=0.38,rely=0.85)

#------------------------------------------------------------                

root.mainloop()
