from Tkinter import*
import time
from  tkMessageBox import *
import random
q1=Tk()
def pay():
    r=random.randint(45454,54652)
    showinfo('Time','wait for some time')
    time.sleep(3)
    showinfo('YOUR OTP',r)
    h(r)
Label(q1,text='Debit Card',font='Times 21 bold').grid(row=0,column=0)
Label(q1,text='Card Number',font='Times 15 bold').grid(row=1,column=0)
e=Entry(q1)
e.grid(row=1,column=1)
Label(q1,text='CVV',font='Times 15 bold').grid(row=2,column=0)
e1=Entry(q1,show='X')
e1.grid(row=2,column=1)
Button(q1,text='Generate OTP',font='Times 15 bold',command=pay).grid(row=3,column=1)

def h(x):
    a1=Tk()
    Label(a1,text='Enter OTP',font='Times 15 bold').grid(row=0,column=0,columnspan=3)
    e3=Entry(a1)
    e3.grid(row=1,column=0)
    def u():
        t=e3.get()
        if int(t)==x:
            showinfo('Information','payment Processing')
            time.sleep(3)
            showinfo('Information','Payment Sucessfull')
            q1.destroy()
            a1.destroy()
        else:
            showinfo('Information','payment Processing')
            time.sleep(3)
            showerror('Error','WRONG OTP')

    Button(a1,text='Pay',command=u).grid(row=2,column=0)
    a1.mainloop()        
q1.mainloop()

    
