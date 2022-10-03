import tkinter as tk
import linecache
import smtplib,ssl
import random
import os

win=tk.Tk()
win.configure(bg='black')
win.geometry('450x500')
win.title('CRYPTOGYAAN')
line=tk.PhotoImage(file='bg4.png')
ln=tk.Label(win,image=line,bd=0)
ln.pack()
win.resizable(0,0)
fine=tk.PhotoImage(file='logbg.png')
tp=tk.PhotoImage(file='otp.png')

#complete the function to login
# def login():
    
# complete the function to create account(cacc)
# def cacc():

def guestLogin():
    win.destroy()
    import guestUser    
     

# but1=tk.Button(win,text='LOGIN ',bg='#dbcdab',fg='#1B263B',command=login)
but1=tk.Button(win,text='LOGIN ',bg='#dbcdab',fg='#1B263B') #pass the command parameter to the button after defining the login function
but1.configure(bd=0,font=('fixedsys',20))
but1.place(x=0,y=300,width=450,height=35)

# but2=tk.Button(win,text='CREATE AN ACCOUNT',bg='#dbcdab',fg='#1B263B',command=cacc)
but2=tk.Button(win,text='CREATE AN ACCOUNT',bg='#dbcdab',fg='#1B263B')#pass the command parameter to the button after defining the cacc function
but2.configure(bd=0,font=('fixedsys',20))
but2.place(x=0,y=360,width=450,height=35)

but3=tk.Button(win,text='ENTER AS GUEST',bg='#dbcdab',fg='#1B263B',command=guestLogin)
but3.configure(bd=0,font=('fixedsys',20))
but3.place(x=0,y=420,width=450,height=35)



win.mainloop()
    