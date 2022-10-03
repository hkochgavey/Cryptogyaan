import tkinter as tk
from tkinter import filedialog
import linecache
from PIL import Image, ImageTk
from lxml import html
import requests
import cryptocompare
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
from gnewsclient import gnewsclient 
import PyPDF2 
import pyttsx3
import tkdocviewer as tdv
import os
global z
z=90
mainwin=tk.Tk()
mainwin.geometry('900x600')
mainbg=tk.PhotoImage(file='mainWinBg.png')
mbg=tk.Label(mainwin,image=mainbg,bd=0)
mbg.pack()
mainwin.resizable(0,0)

def crypto():


    def chat():
        pl=tk.Toplevel()
        pl.geometry('310x80')
        lo=tk.Label(pl,text='PLEASE LOGIN TO USE\nTHIS FEATURE!',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B')
        lo.place(x=0,y=0)
        
    def graph(coin):
        plt.style.use('seaborn')

        x_vals1 = []
        y_vals1 = []
        
            
        def get_crypto_price(coin):
            return cryptocompare.get_price(coin,'USD')[coin]['USD']
        def animate(i):
            x_vals1.append(datetime.now())
            y_vals1.append(get_crypto_price(coin))
            plt.cla()
            plt.gcf().canvas.set_window_title('Live Plotting Cryptocurrency')
                
            plt.xlabel('Time')
            plt.ylabel('Price($)')
            plt.plot(x_vals1,y_vals1,ms=0,label=coin)
            plt.legend()
                
               
        ani = FuncAnimation(plt.gcf(), animate, interval=1000)
        plt.show()
    def graphcom():
        plt.style.use('seaborn')
        coini=coin1.get()
        coinf=coin2.get()
        coin1.delete(0,'end')
        coin2.delete(0,'end')
        x_vals1 = []
        y_vals1 = []
        x_vals2 = []
        y_vals2 = []
            
        def get_crypto_price(coin):
            return cryptocompare.get_price(coin,'USD')[coin]['USD']
        def animate(i):
            x_vals1.append(datetime.now())
            y_vals1.append(get_crypto_price(coini))
            x_vals2.append(datetime.now())
            y_vals2.append(get_crypto_price(coinf))
            plt.yscale('log')
            plt.cla()
            plt.gcf().canvas.set_window_title(coini+' V/S '+coinf)
                
            plt.xlabel('Date')
            plt.ylabel('Price($)')
            plt.plot(x_vals1,y_vals1,ms=0,label=coini)
            plt.plot(x_vals2,y_vals2,ms=0,label=coinf)
            plt.legend()
                
               
        ani = FuncAnimation(plt.gcf(), animate, interval=1000)
        plt.show()

    client = gnewsclient.NewsClient(language='english',location='World',topic='Business',max_results=5) 

    news_list = client.get_news() 
    news=''
    for item in news_list: 
            news=news+item['title']

    def shift():
        x1,y1,x2,y2 = canvas.bbox("marquee")
        if(x2<0 or y1<0): #reset the coordinates
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee",x1,y1)
        else:
            canvas.move("marquee", -1, 0)
        canvas.after(1000//fps,shift)
    canvas=tk.Canvas(mainwin,bg='#dbcdab')
    canvas.place(x=0,y=570)
    text=canvas.create_text(0,-900,text=news,font=('fixedsys',16),fill='#1B263B',tags=("marquee",),anchor='w')
    x1,y1,x2,y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width']=900
    canvas['height']=height
    fps=80    #Change the fps to make the animation faster/slower
    shift()

    def btc():
        graph('BTC')
    def eth():
        graph('ETH')
    def ada():
        graph('ADA')
    def xmr():
        graph('XMR')
    def ltc():
        graph('LTC')
    def xlm():
        graph('XLM')
    def doge():
        graph('DOGE')
    def usdt():
        graph('USDT')
    def xrp():
        graph('XRP')
    def sol():
        graph('SOL')
    def xtz():
        graph('XTZ')
    def link():
        graph('LINK')
    def neo():
        graph('NEO')
        
    crypcan1=tk.Button(mainwin,text='BITCOIN',font=('fixedsys',17),bg='#dbcdab',fg='#1B263B',command=btc)
    crypcan1.place(x=700,y=80,height=30,width=150)
    crypcan2=tk.Button(mainwin,text='ETHEREUM',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=eth)
    crypcan2.place(x=700,y=130,height=30,width=150)
    crypcan3=tk.Button(mainwin,text='CARDANO',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=ada)
    crypcan3.place(x=700,y=180,height=30,width=150)
    crypcan4=tk.Button(mainwin,text='MONERO',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=xmr)
    crypcan4.place(x=700,y=230,height=30,width=150)
    crypcan5=tk.Button(mainwin,text='LITECOIN',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=ltc)
    crypcan5.place(x=700,y=280,height=30,width=150)
    crypcan6=tk.Button(mainwin,text='STELLAR',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=xlm)
    crypcan6.place(x=700,y=330,height=30,width=150)
    crypcan7=tk.Button(mainwin,text='DOGECOIN',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=doge)
    crypcan7.place(x=700,y=380,height=30,width=150)
    crypcan8=tk.Button(mainwin,text='TETHER',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=usdt)
    crypcan8.place(x=700,y=430,height=30,width=150)
    crypcan9=tk.Button(mainwin,text='XRP',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=xrp)
    crypcan9.place(x=700,y=480,height=30,width=150)
    crypcan10=tk.Button(mainwin,text='SOLANA',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=sol)
    crypcan10.place(x=700,y=530,height=30,width=150)
    

    coinl1=tk.Label(mainwin,text='COIN1:',font=('fixedsys',16),bg='#dbcdab',fg='#1B263B')
    coinl1.place(x=385,y=35)
    coinl2=tk.Label(mainwin,text='COIN2:',font=('fixedsys',16),bg='#dbcdab',fg='#1B263B')
    coinl2.place(x=535,y=35)

    coin1=tk.Entry(mainwin,font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',bd=0)
    coin1.place(x=445,y=30,height=30,width=80)
    coin2=tk.Entry(mainwin,font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',bd=0)
    coin2.place(x=595,y=30,height=30,width=80)
    
    compare=tk.Button(mainwin,text='COMPARE',font=('fixedsys',18),bg='#dbcdab',fg='#1B263B',command=graphcom)
    compare.place(x=700,y=30,height=30)

    chatb=tk.Button(mainwin,text='CHAT WITH US!',font=('fixedsys',18),bd=0,bg='#dbcdab',fg='#1B263B',command=chat)
    chatb.place(x=30,y=520,height=30)
    def read(y,x):
        
            path = open(y+'.pdf', 'rb') 

            # creating a PdfFileReader object 
            pdfReader = PyPDF2.PdfFileReader(path) 

            # the page with which you want to start 
            # this will read the page of 25th page. 
            from_page = pdfReader.getPage(x) 

            # extracting the text from the PDF 
            text = from_page.extractText() 

            # reading the text 
            speak = pyttsx3.init() 
            speak.say(text) 
            speak.runAndWait()


    def read(y):
      # Create a root window
      root = tk.Toplevel()
      root.geometry('800x1000')
      # Create a DocViewer widget
      v = tdv.DocViewer(root)
      v.pack(side="top", expand=1, fill="both")

      # Display some document
      v.display_file(y+".pdf")

      # Start Tk's event loop
      root.mainloop()
    def rbook1():
        read('book1')

    def rbook2():
        read('book2')

    def rbook3():
        read('book3')

    def rbook4():
        read('book4')

    def on_configure(event):
        booklst.configure(scrollregion=booklst.bbox('all'))
    booklst = tk.Canvas(mainwin)
    booklst.place(x=30, y=120, height=380, width=200)
    img=tk.PhotoImage(file='img.png')
    lab=tk.Label(booklst,image=img,bd=0)
    lab.place(x=0,y=0,height=500,width=200)
    frame = tk.Frame(booklst)
        # resize the canvas scrollregion each time the size of the frame changes
    frame.bind('<Configure>', on_configure)
        # display frame inside the canvas
    booklst.create_window(0, 0, window=frame)

    scrolly = tk.Scrollbar(booklst, command=booklst.yview)
    scrolly.place(relx=1, rely=0, relheight=1, anchor='ne')
    booklst.configure(yscrollcommand=scrolly.set)


    book1=tk.PhotoImage(file='book1.png')
    book1b=tk.Button(frame,image=book1,command=rbook1)
    book1b.pack(padx=0,pady=0)

    book2=tk.PhotoImage(file='book2.png')
    book2b=tk.Button(frame,image=book2,command=rbook2)
    book2b.pack(padx=0,pady=10)

    book3=tk.PhotoImage(file='book3.png')
    book3b=tk.Button(frame,image=book3,command=rbook3)
    book3b.pack(padx=0,pady=10)

    book4=tk.PhotoImage(file='book4.png')
    book4b=tk.Button(frame,image=book4,command=rbook4)
    book4b.pack(padx=0,pady=10)
    

    mainwin.mainloop()
    
crypto()
