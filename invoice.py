#import statements here
from tkinter import *
import tkinter.ttk
from mailmerge import MailMerge
import inflect
from datetime import date
def invoice():
    def send():
        template="invoice1.docx"#to take  reference file
        f=open('count.txt','r')
        content=f.read()
        f.close()
        o=" "
        a=[0 for x in range(5)]
        d=[" " for x in range(5)]
        s=[" " for x in range(5)]
        flag=1

        
        if OrgName.get():
            o=OrgName.get()
        else:
            print("Organistaion is not provided")
            wam1=Label(data,text="Organisation name is compulsory",fg="red",font=('helvetica',8,'italic'),bg="white")
            wam1.place(x=500,y=220)
            flag=0


            

            
        if detail1.get() and amount1.get():
            try:
                a[0]=int(amount1.get())
            except ValueError:
                print("Enter Integer")
                wam2=Label(data,text="Please Enter a number",fg="red",font=('helvetica',8,'italic'),bg="white")
                wam2.place(x=700,y=420)
                flag=0
            d[0]=detail1.get()
            s[0]="1"
        else:
            print("Details are incomplete")
            wam3=Label(data,text="Please enter both the detail and amount",fg="red",font=('helvetica',8,'italic'),bg="white")
            wam3.place(x=350,y=420)
            flag=0


            

            

        if detail2.get() and amount2.get():
            try:
                a[1]=int(amount2.get())
            except ValueError:
                print("Enter Integer")
                wam4=Label(data,text="Please Enter a number",fg="red",font=('helvetica',8,'italic'),bg="white")
                wam4.place(x=700,y=470)
                flag=0
            d[1]=detail2.get()
            s[1]="2"
        elif detail2.get() or amount2.get():
            print("Details are incomplete")
            wam5=Label(data,text="Please enter both the detail and amount",fg="red",font=('helvetica',8,'italic'),bg="white")
            wam5.place(x=350,y=470)
            flag=0

            



        if detail3.get() and amount3.get():
            try:
                a[2]=int(amount3.get())
            except ValueError:
                print("Enter Integer")
                wam6=Label(data,text="Please Enter a number",fg="red",font=('helvetica',8,'italic'),bg="white")
                wam6.place(x=700,y=520)
                flag=0
            d[2]=detail3.get()
            s[2]="3"
        elif detail3.get() or amount3.get():
            print("Details are incomplete")
            wam7=Label(data,text="Please Enter both the detail and amount",fg="red",font=('helvetica',8,'italic'),bg="white")
            wam7.place(x=350,y=520)
            flag=0

            


        if detail4.get() and amount4.get():
            try:
                a[3]=int(amount4.get())
            except ValueError:
                print("Enter Integer")
                wam8=Label(data,text="Please Enter a number",fg="red",font=('helvetica',8,'italic'),bg="white")
                wam8.place(x=700,y=570)
                flag=0
            d[3]=detail4.get()
            s[3]="4"
        elif detail4.get() or amount4.get():
            print("Details are incomplete")
            wam9=Label(data,text="Please Enter both the detail and amount",fg="red",font=('helvetica',8,'italic'),bg="white")
            wam9.place(x=350,y=570)
            flag=0



        if detail5.get() and amount5.get():
            try:
                a[4]=int(amount5.get())
            except ValueError:
                print("Enter Integer")
                wam10=Label(data,text="Please Enter a number",fg="red",font=('helvetica',8,'italic'),bg="white")
                wam10.place(x=700,y=620)
                flag=0
            d[4]=detail5.get()
            s[4]="5"
        elif detail5.get() or amount5.get():
            print("Details are incomplete")
            wam11=Label(data,text="Please Enter both the detail and amount",fg="red",font=('helvetica',8,'italic'),bg="white")
            wam11.place(x=350,y=620)
            flag=0


        sumfig=a[0]+a[1]+a[2]+a[3]+a[4]
        b=inflect.engine().number_to_words(sumfig)
        for x in range(5):
            if a[x]==0:
              a[x]=" "
            
        
             


        if flag:# flag is a marker variable    
            document=MailMerge(template)
            document.merge(
            ino="00"+str(content),
            Dated='{:%d-%b-%y}'.format(date.today()),
            OrgName=o,
            GSTIN=Gst.get(),
            PANNO=Pan.get(),
            Addr=Address.get(),
            S1=s[0],
            S2=s[1],
            S3=s[2],
            S4=s[3],
            S5=s[4],
            Detail1=d[0],
            Detail2=d[1],
            Detail3=d[2],
            Detail4=d[3],
            Detail5=d[4],
            Amt1=str(a[0]),
            Amt2=str(a[1]),
            Amt3=str(a[2]),
            Amt4=str(a[3]),
            Amt5=str(a[4]),
            SumInFig=str(sumfig),
            AmtWords=b,)
            a="Inv_"+"00"+(content)+"_"+OrgName.get()+".docx"
            document.write(a)
            f=open('count.txt','w')
            f.write(str(int(content.strip())+1))
            f.close()
            ig=Label(data,text="Invoice Generated",font=14,fg='green')
            ig.place(x=410,y=700)

#this function creates all the data with the help of window

    data=Tk() # to make the window
    data.title("Invoice Generator")
    data.geometry('1000x1000') # to set the window size
    data.configure(background='pink') # to set the window colour
    pic=PhotoImage(file="logo.png")
    img=Label(data,image=pic)
    img.place(x=10,y=20)

    Data=Label(data,text="ENTER THE DATA",font=('times',24,'bold'),fg='white',bg='black')
    Data.pack()
    Data.place(x=350,y=100)


    Org=Label(data,text="Organisation name",bg='white',font=('times',18),fg='black')
    Org.place(x=250,y=190)

    GST=Label(data,text="GSTIN",bg='white',font=('times',18),fg='black')
    GST.place(x=250,y=240)

    PAN=Label(data,text="PAN number",bg='white',font=('times',18),fg='black')
    PAN.place(x=250,y=290)

    Addr=Label(data,text="Address",bg='white',font=('times',18),fg='black')
    Addr.place(x=250,y=340)

    OrgName=Entry(data,text="enter organisation name",bg='white',font=(10))
    OrgName.place(x=500,y=190)

    Gst=Entry(data,text="Gstin",bg='white',font=10)
    Gst.place(x=500,y=240)

    Pan=Entry(data,text="Pan no.",bg='white',font=10)
    Pan.place(x=500,y=290)

    Address=Entry(data,text="Adress",bg='white',font=10)
    Address.place(x=500,y=340)

    scrollbar=Scrollbar(data) # to make the scrollbar working
    scrollbar.pack(side=RIGHT,fill=Y)

    Detail1=Label(data,text="Detail 1",bg='white',font=('times',18),fg='black')
    Detail1.place(x=200,y=390)

    Detail2=Label(data,text="Detail 2",bg='white',font=('times',18),fg='black')
    Detail2.place(x=200,y=440)

    Detail3=Label(data,text="Detail 3",bg='white',fg='black',font=('times',18))
    Detail3.place(x=200,y=490)

    Detail4=Label(data,text="Detail 4",bg='white',fg='black',font=('times',18))
    Detail4.place(x=200,y=540)

    Detail5=Label(data,text="Detail 5",bg='white',fg='black',font=('times',18))
    Detail5.place(x=200,y=590)

    detail1=Entry(data,text="detail1",bg='white',)
    detail1.place(x=350,y=390)

    detail2=Entry(data,text="detail2",bg='white')
    detail2.place(x=350,y=440)

    detail3=Entry(data,text="detail3",bg='white')
    detail3.place(x=350,y=490)

    detail4=Entry(data,text="detail4",bg='white')
    detail4.place(x=350,y=540)

    detail5=Entry(data,text="detail5",bg='white')
    detail5.place(x=350,y=590)

    Amount1=Label(data,text="Amount 1",bg='white',fg='black',font=('times',18)) # writing any data
    Amount1.place(x=550,y=390)

    Amount2=Label(data,text="Amount 2",bg='white',fg='black',font=('times',18))
    Amount2.place(x=550,y=440)

    Amount3=Label(data,text="Amount 3",bg='white',fg='black',font=('times',18))
    Amount3.place(x=550,y=490)

    Amount4=Label(data,text="Amount 4",bg='white',fg='black',font=('times',18))
    Amount4.place(x=550,y=540)

    Amount5=Label(data,text="Amount 5",bg='white',fg='black',font=('times',18))
    Amount5.place(x=550,y=590)

    amount1=Entry(data,text="amount1",bg='white') # blank space for entering a data
    amount1.place(x=700,y=390)

    amount2=Entry(data,text="amount2",bg='white')
    amount2.place(x=700,y=440)

    amount3=Entry(data,text="amount3",bg='white')
    amount3.place(x=700,y=490)

    amount4=Entry(data,text="amount4",bg='white')
    amount4.place(x=700,y=540)

    amount5=Entry(data,text="amount5",bg='white')
    amount5.place(x=700,y=590)



    LSubmit=Button(data,text="SUBMIT",font=('times',14,'bold'),fg='white',bg='black',command=send,activebackground="red") # to make the button
    LSubmit.place(x=450,y=650)
    data.mainloop()# to open the window with double click
#invoice()


# for normal code to open the window with double click
#import time(at beggining)
#time(16)(at end)




