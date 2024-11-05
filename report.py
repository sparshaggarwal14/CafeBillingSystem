from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog,messagebox
import random
import mysql.connector as m1


root=Tk()
root.title("BILLING SYSTEM")
root.geometry('1520x780+0+0')

notebook=ttk.Notebook(root)

tab1=Frame(notebook)
tab2=Frame(notebook)
tab3=Frame(notebook)

notebook.add(tab1,text='Filecolor')
notebook.add(tab2,text='Transaction')
notebook.add(tab3,text='Report')

#code for tab1
notebook.pack(fill=X)
def selector():
     color=colorchooser.askcolor()
     c1=color[1]
     print(color)
     txt1_configure(fg=c1)
def openfile():
     ff=filedialog.askopenfilename(initialdir="d:\\tkinter11",title='select the file',filetype=(("text files",".txt"),("all files",",*")))
     file=open(ff,'r')
     n=file.read()
     txtarea.insert("1.0",n)
lblname=Label(tab1,text='Enter Name',font=('ARIAL',10),padx=10,pady=10)
txt1=Entry(tab1)
btn1=Button(tab1,text='SHOW',relief='raised',bd=12,command=selector)
btn2=Button(tab1,text='SHOW FILE',relief='raised',bd=12,command=openfile)
txtarea=Text(tab1,font=('ARIAL',10),padx=10,pady=10)

lblname.grid(row=0,column=0,padx=10,pady=10)
txt1.grid(row=0,column=1,padx=10,pady=10)
btn1.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
btn2.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
txtarea.grid(row=3,column=0,columnspan=2,padx=10,pady=10)


def totalcoldrink():
     a=coke_cd.get()
     b=sprite_cd.get()
     c=frooti_cd.get()
     d=fainta_cd.get()
     if coke_cd=='':
          a=0
     if sprite_cd=='':
          b=0
     if frooti_cd=='':
          c=0
     if fainta_cd=='':
          d=0
     global totalcd
     totalcd =((20*a)+(20*b)+(10*c)+(20*d))
     print('total coldrinks',totalcd)
     tcdp.set(totalcd)
     global t1
     t1 = totalcd*0.18
     tax1.set(t1)

def totalcoffee():
     e=hot_c.get()
     f=cold_c.get()
     g=ice_c.get()
     h=black_c.get()
     if hot_c=='':
          e=0
     if cold_c=='':
          f=0
     if ice_c=='':
          g=0
     if black_c=='':
          h=0
     global totalc
     totalc=((50*e)+(f*75)+(60*g)+(100*h))
     print('total coffee',totalc)
     tcp.set(totalc)
     global t2
     t2 = totalc*0.25
     tax2.set(t2)

def totalsnacks():
     i=pizza_s.get()
     j=burger_s.get()
     k=momos_s.get()
     l=spring_s.get()
     if pizza_s=='':
          i=0
     if burger_s=='':
          j=0
     if momos_s=='':
          k=0
     if spring_s=='':
          l=0
     global totals
     totals=((99*i)+(55*j)+(60*k)+(60*l))
     print('total snacks',totals)
     tsp.set(totals)
     global t3
     t3 = totals*0.05
     tax3.set(t3)

def invoice():
     totalcoldrink()
     totalcoffee()
     totalsnacks()
     ta.set(totalcd+t1+totalc+t2+totals+t3)
     
def invoice_number():
     w=random.randint(1,9)
     x=random.randint(1,9)
     y=random.randint(1,9)
     z=random.randint(1,9)
     i1=str(w)+str(x)+str(y)+str(z)
     return i1

inv=StringVar()
billno = invoice_number()
print(billno)
inv.set(billno)


def addd():
    con=m1.connect(host='localhost',database='mydata',user='root',password='101199')
    if con.is_connected():
        cursor=con.cursor()
        name=txt10.get()
        lname=txt11.get()
        contact=txt12.get()
        invoiceno=txt13.get()
        q=tcdtxt.get()
        t=tx1txt.get()
        u=tctxt.get()
        o=tx2txt.get()
        h=tstxt.get()
        j=tx3txt.get()
        colddrinks=(q+t)
        coffee=(u+o)
        snacks=(h+j)
        amount=tbilltxt.get()
        print('coldrink',colddrinks)
        print('coffee',coffee)
        print('snacks',snacks)
        qry = "insert into invoice values('{}','{}',{},{},{},{},{},{})".format(name,lname,contact,invoiceno,colddrinks,coffee,snacks,amount)
        cursor.execute(qry)
        con.commit()
        #con.close()
        
        txtarea4.insert(END,'WELCOME')
        txtarea4.insert(END,'\nCustomer Name : '+name)
        txtarea4.insert(END,'\nCustomer Last Name: '+lname)
        txtarea4.insert(END,'\nCustomer Contact: '+contact)
        txtarea4.insert(END,'\nInvoice Number: '+invoiceno+'\n')
        txtarea4.insert(END,'='*60)
        txtarea4.insert(END,'\nProduct\t\t\tPrice\t\tTax')
        txtarea4.insert(END,'\nColdrinks\t :\t\t'+q+'\t\t'+t)
        txtarea4.insert(END,'\nCoffee\t :\t\t'+u+'\t\t'+o)
        txtarea4.insert(END,'\nSnacks\t :\t\t'+h+'\t\t'+j+'\n')
        txtarea4.insert(END,'='*60)
        txtarea4.insert(END,'\nTOTAL\tBILL\t:\tRs.'+amount)
        
        
        

        
        messagebox.showinfo(title='Invoice',message='Data is added to database.')
    

        

        
        
lbl1=Label(tab2,text = "RETAIL BILL",font = ('Elephant',15),bg='pink')
lbl1.pack(fill = X)

frame1 = LabelFrame(tab2,text='PERSONAL DETAILS',bg='lightblue',font=('Freestyle Script Regular',10),width = 1000,height= 5,pady = 5)
frame1.pack(fill = X)


lbl10=Label(frame1,text='First Name',font=('Freestyle Script Regular',10),bg='lightgreen',padx=10,pady=10)
lbl10.grid(row=0,column=0,padx=40,pady=10)

#f1=stingvar()
txt10=Entry(frame1,bg='lightgreen')
txt10.grid(row=0,column=1,padx=20,pady=10)

lbl11=Label(frame1,text='Last Name',font=('Freestyle Script Regular',10),bg='lightgreen',padx=10,pady=10)
lbl11.grid(row=0,column=3,padx=40,pady=10)

txt11=Entry(frame1,bg='lightgreen')
txt11.grid(row=0,column=4,padx=20,pady=10)

lbl12=Label(frame1,text='Contact',font=('Freestyle Script Regular',10),bg='lightgreen',padx=10,pady=10)
lbl12.grid(row=0,column=5,padx=40,pady=10)

txt12=Entry(frame1,bg='lightgreen')
txt12.grid(row=0,column=6,padx=20,pady=10)
lbl13=Label(frame1,text='Invoice Number',font=('Freestyle Script Regular',10),bg='lightgreen',padx=10,pady=10)
lbl13.grid(row=0,column=7,padx=40,pady=10)

txt13=Entry(frame1,bg='lightgreen',textvariable=inv)
txt13.grid(row=0,column=8,padx=20,pady=10)

btn10=Button(frame1,text='Search',font = ('elephant',10),bg='lightgreen')
btn10.grid(row=0,column=9,padx=40)

frame2 = Frame(tab2,bg='pink',width = 1000,height= 370)
frame2.pack(fill = X)

frame3 = LabelFrame(frame2,text='COLD DRINKS',bg='white',font=('Freestyle Script Regular',10),width = 300,height= 300)
frame3.place(x=30,y = 35,width= 300,height = 300)

lbl20=Label(frame3,text='Items',font=('Freestyle Script Regular',10),bg='lightpink',padx=10,pady=10)
lbl20.grid(row=0,column=0,padx=40,pady=10)

coke_cd=IntVar()
sprite_cd=IntVar()
frooti_cd=IntVar()
fainta_cd=IntVar()

cd1=Label(frame3,text='Coke',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
cd1.grid(row=1,column=0,padx=30,pady=5)
cd2=Label(frame3,text='Sprite',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
cd2.grid(row=2,column=0,padx=30,pady=5)
cd3=Label(frame3,text='Frooti',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
cd3.grid(row=3,column=0,padx=30,pady=5)
cd4=Label(frame3,text='Fainta',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
cd4.grid(row=4,column=0,padx=30,pady=5)

cdtxt1=Entry(frame3,bg='cyan',textvariable=coke_cd)
cdtxt1.grid(row=1,column=1,padx=20,pady=10)
cdtxt2=Entry(frame3,bg='cyan',textvariable=sprite_cd)
cdtxt2.grid(row=2,column=1,padx=20,pady=10)
cdtxt3=Entry(frame3,bg='cyan',textvariable=frooti_cd)
cdtxt3.grid(row=3,column=1,padx=20,pady=10)
cdtxt4=Entry(frame3,bg='cyan',textvariable=fainta_cd)
cdtxt4.grid(row=4,column=1,padx=20,pady=10)

lbl12=Label(frame3,text='Quantity',font=('Freestyle Script Regular',10),bg='lightpink',padx=10,pady=10)
lbl12.grid(row=0,column=1,padx=30,pady=10)

frame4 = LabelFrame(frame2,text='COFFEE',bg='white',font=('Freestyle Script Regular',10),width =300,height= 300)
frame4.place(x=340,y = 35,width= 300,height = 300)

lbl21=Label(frame4,text='Items',font=('Freestyle Script Regular',10),bg='lightpink',padx=10,pady=10)
lbl21.grid(row=0,column=0,padx=40,pady=10)

hot_c=IntVar()
cold_c=IntVar()
ice_c=IntVar()
black_c=IntVar()
c1=Label(frame4,text='Hot Coffee',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
c1.grid(row=1,column=0,padx=20,pady=5)
c2=Label(frame4,text='Cold Coffee',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
c2.grid(row=2,column=0,padx=20,pady=5)
c3=Label(frame4,text='Ice Tea',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
c3.grid(row=3,column=0,padx=20,pady=5)
c4=Label(frame4,text='Black Coffee',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
c4.grid(row=4,column=0,padx=20,pady=5)

ctxt1=Entry(frame4,bg='cyan',textvariable=hot_c)
ctxt1.grid(row=1,column=1,padx=5,pady=10)
ctxt2=Entry(frame4,bg='cyan',textvariable=cold_c)
ctxt2.grid(row=2,column=1,padx=5,pady=10)
ctxt3=Entry(frame4,bg='cyan',textvariable=ice_c)
ctxt3.grid(row=3,column=1,padx=10,pady=10)
ctxt4=Entry(frame4,bg='cyan',textvariable=black_c)
ctxt4.grid(row=4,column=1,padx=10,pady=10)

lbl12=Label(frame4,text='Quantity',font=('Freestyle Script Regular',10),bg='lightpink',padx=10,pady=10)
lbl12.grid(row=0,column=1,padx=20,pady=10)

frame5 = LabelFrame(frame2,text='SNACKS',bg='white',font=('Freestyle Script Regular',10),width =300,height= 300)
frame5.place(x=650,y = 35,width= 300,height = 300)

lbl22=Label(frame5,text='Items',font=('Freestyle Script Regular',10),bg='lightpink',padx=10,pady=10)
lbl22.grid(row=0,column=0,padx=40,pady=10)

pizza_s=IntVar()
burger_s=IntVar()
momos_s=IntVar()
spring_s=IntVar()
s1=Label(frame5,text='Pizza',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
s1.grid(row=1,column=0,padx=30,pady=5)
s2=Label(frame5,text='Burger',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
s2.grid(row=2,column=0,padx=30,pady=5)
s3=Label(frame5,text='Momos',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
s3.grid(row=3,column=0,padx=30,pady=5)
s4=Label(frame5,text='Spring Roll',font=('Freestyle Script Regular',10),bg='cyan',padx=10,pady=10)
s4.grid(row=4,column=0,padx=30,pady=5)

stxt1=Entry(frame5,bg='cyan',textvariable=pizza_s)
stxt1.grid(row=1,column=1,padx=5,pady=10)
stxt2=Entry(frame5,bg='cyan',textvariable=burger_s)
stxt2.grid(row=2,column=1,padx=5,pady=10)
stxt3=Entry(frame5,bg='cyan',textvariable=momos_s)
stxt3.grid(row=3,column=1,padx=5,pady=10)
stxt4=Entry(frame5,bg='cyan',textvariable=spring_s)
stxt4.grid(row=4,column=1,padx=5,pady=10)

lbl12=Label(frame5,text='Quantity',font=('Freestyle Script Regular',10),bg='lightpink',padx=10,pady=10)
lbl12.grid(row=0,column=1,padx=40,pady=10)

frame6 = Frame(frame2,bg='grey',width =400,height= 500)
frame6.place(x=960,y = 10,width= 530,height = 350)

lbl15=Label(frame6,text='Tax Invoice',relief='raised',bd=5,font=('Freestyle Script Regular',10),bg='lightgrey',width = 65)
lbl15.grid(row=0,column=0,sticky=W)

txtarea4=Text(frame6,font=('Freestyle Script Regular',10),relief='groove',bg='white',width=450,height=500)
txtarea4.grid(row=1,column=0,sticky=W)

frame7 = Frame(tab2,bg='lightblue',width = 1000,height= 330)
frame7.pack(fill = X)

frame8 = Frame(frame7,bg='lightgreen',width =300,height=320)
frame8.place(x=75,y = 10,width= 400,height = 240)


tcdp=IntVar()
tcp=IntVar()
tsp=IntVar()

tcd=Label(frame8,text='Total Cold Drinks Price',font=('Freestyle Script Regular',10),bg='hot pink',padx=10,pady=10)
tcd.grid(row=1,column=0,padx=40,pady=20)
tcdtxt=Entry(frame8,bg='hot pink',textvariable=tcdp)
tcdtxt.grid(row=1,column=1,padx=20,pady=20)

tc=Label(frame8,text='Total COffee Price',font=('Freestyle Script Regular',10),bg='hot pink',padx=10,pady=10)
tc.grid(row=2,column=0,padx=40,pady=20)
tctxt=Entry(frame8,bg='hot pink',textvariable=tcp)
tctxt.grid(row=2,column=1,padx=20,pady=20)

ts=Label(frame8,text='Total Snacks Price',font=('Freestyle Script Regular',10),bg='hot pink',padx=10,pady=10)
ts.grid(row=3,column=0,padx=40,pady=20)
tstxt=Entry(frame8,bg='hot pink',textvariable=tsp)
tstxt.grid(row=3,column=1,padx=20,pady=20)


frame9 = Frame(frame7,bg='lightgreen',width =300,height=200)
frame9.place(x=550,y = 10,width= 400,height = 240)

tax1=IntVar()
tax2=IntVar()
tax3=IntVar()

tx1=Label(frame9,text='TAX',font=('Freestyle Script Regular',10),bg='hot pink',padx=10,pady=10)
tx1.grid(row=1,column=0,padx=70,pady=20)
tx1txt=Entry(frame9,bg='hot pink',textvariable=tax1)
tx1txt.grid(row=1,column=1,padx=20,pady=20)

tx2=Label(frame9,text='TAX',font=('Freestyle Script Regular',10),bg='hot pink',padx=10,pady=10)
tx2.grid(row=2,column=0,padx=70,pady=20)
tx2txt=Entry(frame9,bg='hot pink',textvariable=tax2)
tx2txt.grid(row=2,column=1,padx=20,pady=20)

tx3=Label(frame9,text='TAX',font=('Freestyle Script Regular',10),bg='hot pink',padx=10,pady=10)
tx3.grid(row=3,column=0,padx=70,pady=20)
tx3txt=Entry(frame9,bg='hot pink',textvariable=tax3)
tx3txt.grid(row=3,column=1,padx=20,pady=20)


frame10 = Frame(frame7,bg='lightgreen',width =200,height=200)
frame10.place(x=1025,y = 10,width= 400,height = 240)

ta=IntVar()
tbill=Label(frame10,text='Total Amount',font=('Freestyle Script Regular',10),bg='hot pink',padx=10,pady=10)
tbill.grid(row=1,column=0,padx=50,pady=20)
tbilltxt=Entry(frame10,bg='hot pink',textvariable=ta)
tbilltxt.grid(row=1,column=1,padx=20,pady=20)

btnI=Button(frame10,text='INVOICE',relief='raised',bd=5,padx=30,command=invoice)
btnI.place(x=55,y=80,height=50,width=100)
btnP=Button(frame10,text='PRINT',relief='raised',bd=5,padx=30,command=addd)
btnP.place(x=240,y=80,height=50,width=100)
btnE=Button(frame10,text='EXIT',relief='raised',bd=5,padx=30,command=root.destroy)
btnE.place(x=150,y=155,height=50,width=100)

root.mainloop()


