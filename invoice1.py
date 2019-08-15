from tkinter import *
import tkinter.ttk

from invoice import * # to imprt the other window



def LoginAuth():
    d={"Anchal sharma":"16789","Shikha yadav":"16788"}
    name=UName.get()
    password=Pwd.get()
    for x in d:
      if(x==name):
          if(d[x]==password):
             print("correct password \n  you are logged in")
             login.destroy()
             invoice()
             break
    else:
          Invalid=Label(login,text="Incorrect username or password",bg='saddlebrown',font=6,fg='white')
          Invalid.place(x=96,y=350)


login=Tk()# to make the window
login.title("Invoice Generator")
login.geometry('500x600')
login.configure(background='lavender')
pic=PhotoImage(file="logo.png")
img=Label(login,image=pic)
img.place(x=10,y=12)

LoginTitle=Label(login,text="USER LOGIN",font=('times',20,'bold'),bg='black',fg='white')
LoginTitle.pack()
LoginTitle.place(x=165,y=100)


UserName=Label(login,text="User Name",font=7,bg='white',fg='black')
UserName.place(x=110,y=190)

Password=Label(login,text="Password",bg='white',font=7,fg='black')
Password.place(x=110,y=240)

UName=Entry(login,text="Enter your name here",bg='white')
UName.place(x=250,y=190)

Pwd=Entry(login,text="password",bg='white')
Pwd.place(x=250,y=240)

LSubmit=Button(login,text="SUBMIT",font=('times',14,'bold'),bg='black',command=LoginAuth,activebackground="red",fg='white')
LSubmit.place(x=180,y=299)# to make a window
login.mainloop()






