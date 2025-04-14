#rawF.ezio
#Emroz Sardar
#XII Sc Computer Science Investigatory(Python X Mysql)

from tkinter import *
from tkinter import Tk,StringVar, ttk
import tkinter.messagebox
import random
import datetime
import time;
from tkinter import messagebox
import mysql.connector 

root= Tk()
root.geometry("1350x750+0+0")
root.title("Hotel Managment System")
root.configure(background='white')

topframe= Frame(root, width=1350,height=100,bg='royal blue', bd=14,relief='sunken')
topframe.pack(side=TOP)

bottomframe= Frame(root, width=1350,height=200,bg='cyan2', bd=20,relief='raise')
bottomframe.pack(side=BOTTOM)

leftmidframe= Frame(bottomframe, width=600,height=1000,bg='white', bd=14,relief='sunken')
leftmidframe.pack(side=LEFT)

rightmidframe= Frame(bottomframe, width=750,height=1000,bg='white', bd=14,relief='sunken')
rightmidframe.pack(side=RIGHT)

ibltitle=Label(topframe,font=('Forte',40,'bold'),text='Hotel Managment System',bg='azure',bd=12,width=41,justify='center')
ibltitle.grid(row=0,column=0)

ibltitle=Label(topframe,font=('Forte',20,'bold'),text='Created by Emroz Sardar !',bg='azure',bd=12,width=41,justify='center')
ibltitle.grid(row=1,column=0)
#====================================================Variables || function Defination=========================================================================================================
idproof=StringVar()
noofdays=IntVar()

tax=StringVar()
date1=StringVar()
roomno=IntVar()

subtotal=IntVar()
total=IntVar()
roomtype=StringVar()

meal1=StringVar()

paym=StringVar()

cname=StringVar()
mobile=StringVar()
bedtype=StringVar()
idno=StringVar()

address=StringVar()

txt8=StringVar()
txt9=StringVar()
txt4=StringVar()
txt6=StringVar()
txt7=StringVar()
txt5=StringVar()
txt10=StringVar()
txt11=StringVar()
txt12=StringVar()

txt1=StringVar()
txt2=StringVar()
txt3=StringVar()

person=IntVar()

txt5.set('')
txt10.set('')
txt11.set('')
txt8.set('')
txt9.set('')
txt4.set('')
txt6.set('')
txt7.set('')
txt12.set('')

address.set('')
cname.set('')
bedtype.set('')

paym.set('')

idproof.set('')
meal1.set('')
roomtype.set('')
noofdays.set('0')

tax.set('0.0')

roomno.set('0')

total.set('0.0')
subtotal.set('0.0')
date1.set(time.strftime('%d/%m/%y'))
txt1.set('')
txt2.set('')
txt3.set('')



def Display():

    pr=person.get()
    
    n=cname.get()
    txt1.set(n)
    
    p=mobile.get()
    txt2.set(p)

    a=address.get()
    txt3.set(a)

    if idproof.get()=='AADHAR':
        txt4.set('AADHAR Card')
    elif idproof.get()=='PAN':
        txt4.set('PAN Card')
    elif idproof.get()=='Voter ID':
        txt4.set('Voter ID Card')
    else:
        txt4.set('Choose any option ')

    ed=idno.get()
    txt5.set(ed)

    if roomtype.get()=='AC':
        txt6.set('AC Room')
        ac1=500
    elif roomtype.get()=='NON AC':
        txt6.set('Non AC Room')
        ac1=0
    else:
        txt6.set('Choose any option ')



    if bedtype.get()=='Double Bed':
        txt7.set('Double Bed')
        bd=2500
    elif bedtype.get()=='Single Bed':
        txt7.set('Single Bed')
        bd=2000
    elif bedtype.get()=='Honeymoon suite':
        txt7.set('Honeymoon suite')
        bd=4000
    elif bedtype.get()=='King':
        txt7.set('King Size Bed')
        bd=3000
    else:
        txt7.set('Choose any option ')

    day=noofdays.get()
    txt8.set('Days:'+str(day))
        

    
    if meal1.get()=='Veg':
        txt9.set('Vegetarian')
        m1=500*pr
    elif meal1.get()=='Non-Veg':
        txt9.set('Non Vegtarian')
        m1=700*pr
    else:
        txt9.set('Choose any option ')




    room1=roomno.get()
    txt10.set(room1)
    


    if paym.get()=='Master Card':
        txt11.set('Master Card')
        
    elif paym.get()=='Cash':
        txt11.set('Cash')
        
    elif paym.get()=='Visa Card':
        txt11.set('Visa Card')
        
    elif paym.get()=='Debit Card':
        txt11.set('Debit Card')
        
    else:
        txt11.set('Choose any option ')
        

    
    txt12.set('Total no. of person checked in :'+str(pr))
    

        

    sum1 = (ac1+ bd + m1)*day
    subtotal.set(sum1)

    taxx=sum1*0.18
    tax.set(taxx)

    total1=sum1+taxx
    total.set(total1) 

    import mysql.connector as w
    mydb=w.connect(host='localhost',user='root',passwd='root')
    y=mydb.cursor()
    y.execute('use emroz')
    x=w.connect(host='localhost',user='root',passwd='root',database='emroz')
    
    a=x.cursor()
    
    a1=txt1.get() #cname    Ezio.emroz
    b1=txt2.get() #mobile   9804226160
    add=txt3.get() #address
    c1=txt4.get() #idtype
    d1=txt5.get() #Idno
    e1=noofdays.get() #date
    f1=txt10.get() #roomNo
    g1=person.get() #person
    h1=total.get() #net amt
    i1= date1.get() #check in varies
    
    a.execute("insert into Reg(Customer_Name,Address,Mobile,IdType,IdNo,Indate,NoOfDays,Room,Person,TotalPaid)values('{}','{}','{}','{}','{}','{}',{},{},{},'{}')".format(a1,add,b1,c1,d1,i1,e1,f1,g1,h1))
   
    x.commit()
   

def database():
    import mysql.connector as w
    mydb=w.connect(host='localhost',user='root',passwd='root')
    y=mydb.cursor()
    y.execute('create database emroz')
    x=w.connect(host='localhost',user='root',passwd='root',database='emroz')
   
    a=x.cursor()
   
    a.execute('create table Reg(Customer_Name varchar(25),Address varchar(100),Mobile varchar(11),IdType varchar(11),IdNo varchar(25),Indate varchar(10),NoOfDays int(5),Room int(5),Person varchar(3),TotalPaid varchar(20))')
   
    x.commit()
    
def reset():
    txt8.set('')
    txt9.set('')
    txt4.set('')
    txt6.set('')
    txt7.set('')
    txt5.set('')
    
    txt1.set('')
    txt2.set('')
    txt10.set('')
    txt11.set('')
    txt12.set('')
    txt3.set('')
    mobile.set('')
    address.set('')
    cname.set('')
    bedtype.set('Choose Option')
    address.set('')
    paym.set('Choose')
    
    meal1.set('')
    roomtype.set('')
    noofdays.set('')
    roomtype.set('Choose Option')
    idproof.set('Choose Option')
    idno.set('')
    noofdays.set('')
    tax.set('0.0')
    roomno.set('')
    person.set('')
    total.set('0.0')
    subtotal.set('0.0')
    
    date1.set(time.strftime('%d/%m/%y'))

    
def iexit():
    i=tkinter.messagebox.askyesno('Hotel Management System','confirm if you want to exit')
    if i==1:
        root.destroy()
        print('YOU HAVE CLOSED THE PAGE ')
        

'''def ezio.emroz//db '''

#=============================================Display detail===========================================================================================================

iblcname=Label(leftmidframe,font=('arial',14,'bold'),text='Customer Name',bd=10,width=20,anchor='w')
iblcname.grid(row=0,column=0)
ibladdress2=Entry(leftmidframe,font=('arial',14,'bold'),textvariable=cname,bd=10,width=12,relief='sunken')
ibladdress2.grid(row=0,column=1)

iblmobile1=Label(leftmidframe,font=('arial',14,'bold'),text='Mobile No.',bd=10,width=20,anchor='w')
iblmobile1.grid(row=1,column=0)
iblmobile2=Entry(leftmidframe,font=('arial',14,'bold'),textvariable=mobile,bd=10,width=12,relief='sunken')
iblmobile2.grid(row=1,column=1)

ibladdress1=Label(leftmidframe,font=('arial',14,'bold'),text='Address',bd=10,width=20,anchor='w')
ibladdress1.grid(row=2,column=0)
ibladdress2=Entry(leftmidframe,font=('arial',14,'bold'),textvariable=address,bd=10,width=12,relief='sunken')
ibladdress2.grid(row=2,column=1)


iblidproof1=Label(leftmidframe,font=('arial',14,'bold'),text='ID proof',bd=10,width=20,anchor='w')
iblidproof1.grid(row=3,column=0)

iblidproof2=ttk.Combobox(leftmidframe,textvariable=idproof,state='readonly',font=('arial',14,'bold'),width=12)
iblidproof2['value']=('Choose ID','AADHAR','PAN','Voter ID')
iblidproof2.current(0)
iblidproof2.grid(row=3,column=1)


iblidno1=Label(leftmidframe,font=('arial',14,'bold'),text='Id no.',bd=10,width=20,anchor='w')
iblidno1.grid(row=4,column=0)
iblidno2=Entry(leftmidframe,font=('arial',14,'bold'),textvariable=idno,bd=10,width=12,relief='sunken')
iblidno2.grid(row=4,column=1)



iblroomtype1=Label(leftmidframe,font=('arial',14,'bold'),text='Room Type',bd=10,width=20,anchor='w')
iblroomtype1.grid(row=5,column=0)

iblroomtype2=ttk.Combobox(leftmidframe,textvariable=roomtype,state='readonly',font=('arial',14,'bold'),width=12)
iblroomtype2['value']=('Choose AC/NON AC','AC','NON AC')
iblroomtype2.current(0)
iblroomtype2.grid(row=5,column=1)



iblbedtype1=Label(leftmidframe,font=('arial',14,'bold'),text='Bed Type',bd=10,width=20,anchor='w')
iblbedtype1.grid(row=6,column=0)

cmbbedtype=ttk.Combobox(leftmidframe,textvariable=bedtype,state='readonly',font=('arial',14,'bold'),width=12)
cmbbedtype['value']=('Choose Bed','Double Bed','Single Bed','Honeymoon suite','King')
cmbbedtype.current(0)
cmbbedtype.grid(row=6,column=1)



iblnoofday1=Label(leftmidframe,font=('arial',14,'bold'),text='No Of Days',bd=10,width=20,anchor='w')
iblnoofday1.grid(row=7,column=0)
txtiblnoofday12=Entry(leftmidframe,textvariable=noofdays,font=('arial',14,'bold'),bd=10,width=14)
txtiblnoofday12.grid(row=7,column=1)



iblfood1=Label(leftmidframe,font=('arial',14,'bold'),text='Meal',bd=10,width=20,anchor='w')
iblfood1.grid(row=9,column=0)

iblfood2=ttk.Combobox(leftmidframe,textvariable=meal1,state='readonly',font=('arial',14,'bold'),width=12)
iblfood2['value']=('Choose meal','Veg','Non-Veg')
iblfood2.current(0)
iblfood2.grid(row=9,column=1)

iblroomno1=Label(leftmidframe,font=('arial',14,'bold'),text='Room No.',bd=10,width=20,anchor='w')
iblroomno1.grid(row=10,column=0)
txtroomno2=Entry(leftmidframe,textvariable=roomno,font=('arial',14,'bold'),bd=10,width=14)
txtroomno2.grid(row=10,column=1)


iblperson1=Label(leftmidframe,font=('arial',14,'bold'),text='No. of Person ',bd=10,width=20,anchor='w')
iblperson1.grid(row=11,column=0)
txtiblperson2=Entry(leftmidframe,textvariable=person,font=('arial',14,'bold'),bd=10,width=14)
txtiblperson2.grid(row=11,column=1)



#=============================================right middle frame======================================================================================================


iblcheckin1=Label(rightmidframe,font=('arial',14,'bold'),text='Check in Date',bd=10,width=16,anchor='w')
iblcheckin1.grid(row=0,column=0)
iblcheckin2=Label(rightmidframe,font=('arial',14,'bold'),textvariable=date1,bd=10,width=14,relief='sunken')
iblcheckin2.grid(row=0,column=1)

iblpayment1=Label(rightmidframe,font=('arial',14,'bold'),text='PAYMENT METHOD',bd=10,width=16,anchor='w')
iblpayment1.grid(row=0,column=2)

cmbpayment=ttk.Combobox(rightmidframe,textvariable=paym,state='readonly',font=('arial',14,'bold'),width=12)
cmbpayment['value']=('Choose','Master Card','Cash','Visa Card','Debit Card')
cmbpayment.current(0)
cmbpayment.grid(row=0,column=3)



ibltxt1=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt1,bd=10,width=32,relief='sunken')
ibltxt1.grid(row=2,column=0,columnspan=2)

ibltxt2=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt2,bd=10,width=32,relief='sunken')
ibltxt2.grid(row=2,column=2,columnspan=2)

ibltxt3=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt3,bd=10,width=68,relief='sunken')
ibltxt3.grid(row=3,column=0,columnspan=4)

ibltxt4=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt4,bd=10,width=32,relief='sunken')
ibltxt4.grid(row=4,column=0,columnspan=2)

ibltxt5=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt5,bd=10,width=32,relief='sunken')
ibltxt5.grid(row=4,column=2,columnspan=2)

ibltxt6=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt6,bd=10,width=32,relief='sunken')
ibltxt6.grid(row=5,column=0,columnspan=2)

ibltxt7=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt7,bd=10,width=32,relief='sunken')
ibltxt7.grid(row=5,column=2,columnspan=2)


iblmsg=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt8,bd=10,width=32,relief='sunken')
iblmsg.grid(row=6,column=0,columnspan=2)

iblmsg2=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt9,bd=10,width=32,relief='sunken')
iblmsg2.grid(row=6,column=2,columnspan=2)

iblmsg7=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt10,bd=10,width=32,relief='sunken')
iblmsg7.grid(row=7,column=0,columnspan=2)

iblmsg8=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt11,bd=10,width=32,relief='sunken')
iblmsg8.grid(row=7,column=2,columnspan=2)

ibltxt12=Label(rightmidframe,font=('arial',14,'bold'),textvariable=txt12,bd=10,width=68,relief='sunken')
ibltxt12.grid(row=8,column=0,columnspan=4)



iblgst1=Label(rightmidframe,font=('arial',14,'bold'),text='GST',bd=10,width=16,anchor='w')
iblgst1.grid(row=9,column=2)
iblgst1=Label(rightmidframe,font=('arial',14,'bold'),text='18%',bd=10,width=16,anchor='w')
iblgst1.grid(row=9,column=3)

ibltax1=Label(rightmidframe,font=('arial',14,'bold'),text='TAX',bd=10,width=16,anchor='w')
ibltax1.grid(row=9,column=0)
ibltax2=Label(rightmidframe,font=('arial',14,'bold'),textvariable=tax,bd=10,width=14,relief='sunken')
ibltax2.grid(row=9,column=1)

iblsubtotal1=Label(rightmidframe,font=('arial',14,'bold'),text='Total (excluding GST)',bd=10,width=16,anchor='w')
iblsubtotal1.grid(row=10,column=0)
iblsubtotal2=Label(rightmidframe,font=('arial',14,'bold'),textvariable=subtotal,bd=10,width=14,relief='sunken')
iblsubtotal2.grid(row=10,column=1)

ibltotal1=Label(rightmidframe,font=('arial',14,'bold'),text='Net Amount',bd=10,width=16,anchor='w')
ibltotal1.grid(row=10,column=2)
ibltotal2=Label(rightmidframe,font=('arial',14,'bold'),textvariable=total,bd=10,width=14,relief='sunken')
ibltotal2.grid(row=10,column=3)

btntotal=Button(rightmidframe,font=('arial',14,'bold'),text='TOTAL',bd=6,bg='DeepSkyBlue2',width=16,command=Display)
btntotal.grid(row=12,column=0)
iblreset=Button(rightmidframe,font=('arial',14,'bold'),text='RESET',bd=6,bg='SkyBlue3',width=15,command=reset)
iblreset.grid(row=12,column=1)
iblexit=Button(rightmidframe,font=('arial',14,'bold'),text='EXIT',bd=6,bg='red',width=16,command=iexit)
iblexit.grid(row=12,column=2)
creat_database=Button(rightmidframe,font=('arial',14,'bold'),text='CREATE DATABASE',bd=6,width=16,command=database)
creat_database.grid(row=12,column=3)
'''cname = ezio.emroz'''







