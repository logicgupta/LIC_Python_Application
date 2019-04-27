from Tkinter import*
import os
start=Tk()
start.geometry('638x479')

def fun(event):
    
    start.destroy()
    os.startfile("test.py")
icon1=PhotoImage(file="s1.gif")
l=Label(start,image=icon1)
l.bind("<Motion>",fun)
l.place(relx=0.0,rely=0.001)
Label(start,text="").grid(row=0,column=0)
Label(start,bg="White").grid(row=1,column=0)
Label(start,text="",bg="White").grid(row=2,column=0)
Label(start,text="",bg="White").grid(row=3,column=0)
Label(start,text="Name             :           LOGIC GUPTA",font="Papyrus 20 bold",bg='White').grid(row=4,sticky=W)
Label(start,text="Enroll            :           161B114",font="Papyrus 20 bold",bg='White').grid(row=5,sticky=W)
Label(start,text="Batch             :           B4(BY)",font="Papyrus 20 bold",bg='White').grid(row=6,sticky=W)
Label(start,text="Submited To :           Dr.Mahesh Kumar",font="Papyrus 20 bold",bg='White').grid(row=7,sticky=W)
Label(start,text="Topic             :               L.I.C",font="Papyrus 20 bold",bg='White').grid(row=8,sticky=W)

start.mainloop()
