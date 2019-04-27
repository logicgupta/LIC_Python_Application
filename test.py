from Tkinter import*
import PIL
from PIL import ImageTk,Image
import time;
import os
import webbrowser
import random
from tkMessageBox import*
import sqlite3
con=sqlite3.Connection("Dbqwq1")
cur=con.cursor()
def fun():
    root_login=Toplevel()
    root_login.title('Admin Login')
    root_login.geometry('1700x1700')
    icon=ImageTk.PhotoImage(file='bcd3.gif')
    Label(root_login,image=icon).place(relx=-0.0001,rely=0.000000111)
    Label(root_login,text="LIFE INSURANCE CORPORATION OF INDIA",relief='ridge',font="times 32 bold",padx=340).grid(row=0,column=0,columnspan=2)
    Label(root_login,text="USER_NAME",font="times 20 bold").place(relx=.4,rely=.35,anchor=CENTER)#grid(row=3,column=0)
    l1=Entry(root_login,bg='lightpink',font="times 20 bold")
    l1.place(relx=.6,rely=.35,anchor=CENTER)#grid(row=3,column=1)
    localtime=time.asctime(time.localtime(time.time()))
    labs=Label(root_login,text=localtime,font=('times',30,'bold'),bd=5,bg="salmon",fg="white").place(relx=.78,rely=.86,anchor=CENTER)
    Label(root_login,text="PASSWORD",font="times 20 bold",bd=5).place(relx=.4,rely=.43,anchor=CENTER)#grid(row=4,column=0)
    l2=Entry(root_login,show='*',bd=5,bg='lightpink',font="times 20 bold")
    l2.place(relx=.6,rely=.43,anchor=CENTER)#grid(row=4,column=1)

    def log():
            if l2.get() == "1" and l1.get() == "1" :
                l2.delete(0,END)
                showinfo('Success','Login Successfull')
                root_login.destroy()
                root=Toplevel()
                root.title('L.I.C')
                
                #l1.delete(0,END)
                root.geometry('1700x1700')
                root.configure(bg='Powder blue')
                icon1=ImageTk.PhotoImage(file='logo.gif')
                Label(root,image=icon1).grid(row=0,column=0,sticky=W)
                def logout():
                    print "hatsh"
                    root.destroy()
                    os.startfile("test.py")
                Label(root,text="LIFE INSURANCE CORPORATION OF INDIA",font="times 35 bold",bg='Powder blue').grid(row=0,column=1,columnspan=3,sticky=W)
                Label(root,text="Select Your Choice",font="times 35 bold",bg='Powder blue',pady=15).grid(row=1,column=0)
                def callback(event):
                    webbrowser.open_new(r"https://www.licindia.in/")
                link = Label(root, text="Visit Website", fg="blue", cursor="hand2")
                link.grid(row=2,column=3,sticky=E)
                link.bind("<Button-1>", callback)
                Button(root,text="Log Out",font="times 15 bold",bg='Powder blue',command=logout,pady=5).grid(row=1,column=3,sticky=E)
                v1=IntVar()
                r1=Radiobutton(root,text="Do Insurance Of New Client",font="times 20 bold",bg='Powder blue',variable=v1,value=1)
                r1.grid(row=2,column=0,sticky='W')
                r2=Radiobutton(root,text="Fetch Information About Old Client",font="times 20 bold",bg='Powder blue',variable=v1,value=2)
                r2.grid(row=3,column=0,sticky='W')
                r3=Radiobutton(root,text="Insert Policy Details",font="times 20 bold",bg='Powder blue',variable=v1,value=3)
                r3.grid(row=5,column=0,sticky='W')
                r3=Radiobutton(root,text="List Of Policy",font="times 20 bold",bg='Powder blue',variable=v1,value=4)
                r3.grid(row=6,column=0,sticky='W')
                r4=Radiobutton(root,text="Close LIC Account",font="times 20 bold",bg='Powder blue',variable=v1,value=5)
                r4.grid(row=7,column=0,sticky='W')
                r6=Radiobutton(root,text="Pay Amount Of policy taken  ",font="times 20 bold",bg='Powder blue',variable=v1,value=6)
                r6.grid(row=8,column=0,sticky='W')
                r7=Radiobutton(root,text="Delete / Close Policy  ",font="times 20 bold",bg='Powder blue',variable=v1,value=7)
                r7.grid(row=9,column=0,sticky='W')

                def insert1():
                    root1=Toplevel()
                    root1.geometry('1700x1700')
                    root1.configure(bg='Powder blue')
                    icon=ImageTk.PhotoImage(file='logo.gif')
                    Label(root1,image=icon).grid(row=0,column=0,sticky=W)
                    Label(root1,text="LIFE INSURANCE CORPORATION OF INDIA",font="times 45 bold",bg='Powder blue').grid(row=0,column=1,columnspan=3)
                    Label(root1,text="Policy Number",font="times 20 bold",bg='Powder blue').grid(row=1,column=1,sticky=W)
                    e1=Entry(root1,font="times 20 bold")
                    e1.grid(row=1,column=2)
                    Label(root1,text="First Name",font="times 20 bold",bg='Powder blue').grid(row=3,column=1,sticky=W)
                    e2=Entry(root1,font="times 20 bold")
                    e2.grid(row=3,column=2)
                    Label(root1,text="Last Name",font="times 20 bold",bg='Powder blue').grid(row=4,column=1,sticky=W)
                    e3=Entry(root1,font="times 20 bold")
                    e3.grid(row=4,column=2)
                    Label(root1,text="Age",font="times 20 bold",bg='Powder blue').grid(row=5,column=1,sticky=W)
                    e4=Entry(root1,font="times 20 bold")
                    e4.grid(row=5,column=2)
                    Label(root1,text="Father's Name",font="times 20 bold",bg='Powder blue').grid(row=6,column=1,sticky=W)
                    e5=Entry(root1,font="times 20 bold")
                    e5.grid(row=6,column=2) 
                    Label(root1,text="Date Of Isurance (DD\MM\YYYY)",font="times 20 bold",bg='Powder blue').grid(row=7,column=1,sticky=W)
                    e6=Entry(root1,font="times 20 bold")
                    e6.grid(row=7,column=2)
                    Label(root1,text="Nominee Name",font="times 20 bold",bg='Powder blue').grid(row=8,column=1,sticky=W)
                    e7=Entry(root1,font="times 20 bold")
                    e7.grid(row=8,column=2)    
                    Label(root1,text="Policy Name",font="times 20 bold",bg='Powder blue').grid(row=9,column=1,sticky=W)
                    e8=Entry(root1,font="times 20 bold")
                    e8.grid(row=9,column=2)  
                    Label(root1,text="Select Mode of Payment ",font="times 20 bold",bg='Powder blue').grid(row=11,column=1,sticky=W)
                    v2=StringVar()
                    r3=Radiobutton(root1,text="Quarterly",font="times 20 bold",bg='Powder blue',variable=v2,value='Quaterly')
                    r3.grid(row=10,column=2)
                    r1=Radiobutton(root1,text="Half Yearly",font="times 20 bold",bg='Powder blue',variable=v2,value='Half Yearly')
                    r1.grid(row=11,column=2)
                    r2=Radiobutton(root1,text="Yearly",font="times 20 bold",bg='Powder blue',variable=v2,value='Yearly')
                    r2.grid(row=12,column=2)
                    Label(root1,text="Premium Amount",font="times 20 bold",bg='Powder blue').grid(row=13,column=1,sticky=W)
                    e9=Entry(root1,font="times 20 bold")
                    e9.grid(row=13,column=2)
                    Label(root1,text="Number of Years (Max-25 and Min-5)",font="times 20 bold",bg='Powder blue').grid(row=14,column=1,sticky=W)
                    e10=Entry(root1,font="times 20 bold")
                    e10.grid(row=14,column=2)
                    Label(root1,text="Security_Amount",font="times 20 bold",bg='Powder blue').grid(row=15,column=1,sticky=W)
                    e11=Entry(root1,font="times 20 bold")
                    e11.grid(row=15,column=2)
                    def inslic():
                        l=0;
                        if e2.get() == '' and e3.get() == '' and e3.get() == '' and e4.get() == '' and e5.get() == '' and e6.get() == '':
                            showerror('Error','Field Is Empty')
                            l=1
                            e1.delete(0,END)
                            e2.delete(0,END)
                            e3.delete(0,END)
                            e4.delete(0,END)
                            e5.delete(0,END)
                            e6.delete(0,END)
                            e7.delete(0,END)
                            e8.delete(0,END)
                            e9.delete(0,END)
                            e10.delete(0,END)
                            e11.delete(0,END)
                        p=(e1.get(),)
                        cur.execute('select * from ins1 where Policy_Number=?',p)
                        d=cur.fetchall()
                        if len(d)!=0:
                            showerror('Error','Duplicate Data')
                        else:
                            i=0
                            j=0
                            a=[(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),v2.get(),e9.get(),e10.get(),e11.get(),i,j)]
                            cur.executemany('insert into ins1 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',a)
                            cur.fetchall()
                            con.commit()
                            e1.delete(0,END)
                            e2.delete(0,END)
                            e3.delete(0,END)
                            e4.delete(0,END)
                            e5.delete(0,END)
                            e6.delete(0,END)
                            e7.delete(0,END)
                            e8.delete(0,END)
                            e9.delete(0,END)
                            e10.delete(0,END)
                            e11.delete(0,END)
                            showinfo('Success','Information Stored')
                            
                    Button(root1,text='Submit',bd=3,bg='green',command=inslic,font="times 15 bold").grid(row=16,column=3)
                    Button(root1,text='BACK',bd=3,bg='green',command=root1.destroy,font="times 15 bold").grid(row=17,column=3)
                    root1.mainloop()
                    
                
                #  SQL PART.......

                def create():
                    cur.execute('create table if not exists ins1(Policy_Number number(10) primary key,First_Name varchar2(20),Last_Name varchar2(20),Age number(2),Fathers_Name varchar(30),Date_Insurance date,Nominee_Name varchar2(20),Policy_Name varchar2(20),Paymode_Mode varchar(20),Premium_Amount number(7),No_Of_Years number(2),Amount_Paid number(10),No_Of_Installment number(10),Benefit number(10))')

                    # FUNCTION TO SEARCH INFORMATION ......
                def search_info():
                    root_info=Toplevel()
                    root_info.configure(bg='Powder blue')
                    icon=ImageTk.PhotoImage(file='logo.gif')
                    Label(root_info,image=icon).grid(row=0,column=0,sticky=W)
                    root_info.geometry('1700x1700')
                    root_info.configure(bg='Powder blue')
                    Label(root_info,text="LIFE INSURANCE CORPORATION OF INDIA",relief='ridge',font="times 35 bold",bg='green',padx=10,pady=5).grid(row=0,column=1,columnspan=2)
                    Label(root_info,text="Enter the Policy Number ",font="times 25 bold",pady=50,bg='Powder blue').grid(row=1,column=1,sticky=W)
                    d1=Entry(root_info,font="times 25 bold")
                    d1.grid(row=1,column=2)
                    def display_info():
                        a=(d1.get(),)
                        cur.execute("select * from ins1 where Policy_Number=?",a)
                        c= cur.fetchall()
                        z=3
                        m=0
                        list1=[]
                        for i in c:
                            Label(root_info,text="Policy_Number :                       "+str(i[0]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.4)
                            Label(root_info,text="Name :                                      "+str(i[1]+" "+str(i[2])),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.45)
                            Label(root_info,text="Age :                                         "+str(i[3]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.50)
                            Label(root_info,text="Father's Name :                       "+str(i[4]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.55)
                            Label(root_info,text="Date Of Isurance :                   "+str(i[5]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.60)
                            Label(root_info,text="Nominee Name :                      "+str(i[6]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.65)
                            Label(root_info,text="Policy Name :                           "+str(i[7]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.70)
                            Label(root_info,text="Mode Of Payment :                 "+str(i[8]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.75)
                            Label(root_info,text="Premium Amount :                   "+str(i[9]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.80)
                            Label(root_info,text="Tenure :                                    "+str(i[10]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.85)
                            Label(root_info,text="Total Amount Paid :                 "+str(i[11]),font="times 15 bold",bg='Powder blue').place(relx=0.20,rely=0.90)
                            Label(root_info,text="Benifit Got :                      "+str(i[13]),font="times 15 bold",bg='Powder blue').place(relx=0.50,rely=0.40)
                        #root_info.destroy()
                    Button(root_info,text="Submit",command=display_info,bd=5,font="times 20 bold").grid(row=2,column=1,sticky='E')     
                    Button(root_info,text="BACK",command=root_info.destroy,bd=5,font="times 20 bold").grid(row=2,column=2,sticky='E')
                    root_info.mainloop()


                #   CREATE  OF POLICY TABLE  FUNCTION.......

                def create_listplcy():
                    cur.execute('create table if not exists plcy(Serial_No integer primary key autoincrement , Policy_Name varchar2(30) ,agegrp1 number(2),agegrp2 number(2),agegrp3 number(2),agegrp4 number(2),agegrp5 number(2),agegrp6 number(2),agegrp7 number(2))')
                    cur.fetchall()
                # INSERTING THE POLICY DETAILS FUNCTION.......

                def insert_listplcy():
                    root2=Toplevel()
                    root2.geometry('1700x1700')
                    root2.configure(bg='Powder blue')
                    p1=PhotoImage(file='logo.gif')
                    Label(root2,image=p1).grid(row=0,column=0,sticky=W)
                    Label(root2,text="LIFE INSURANCE CORPORATION OF INDIA",font="times 30 bold",bg='Powder blue').grid(row=0,column=1,columnspan=3,sticky=W)
                    Label(root2,text="Insert the Policy Details",font="times 35 bold",pady=10,bg='Powder blue').grid(row=1,column=0,columnspan=2)
                    Label(root2,text='Policy_Name ',font="times 20 bold",bg='Powder blue').grid(row=3,column=0,sticky=W)
                    e16=Entry(root2,font="times 20 bold")
                    e16.grid(row=3,column=1)
                    Label(root2,text='Interest_Age_Group1(5-10).',font="times 20 bold",bg='Powder blue',pady=10).grid(row=4,column=0)
                    e17=Entry(root2,font="times 20 bold")
                    e17.grid(row=4,column=1)
                    Label(root2,text='Interest_Age_Group2(10-18).',font="times 20 bold",bg='Powder blue',pady=10).grid(row=5,column=0)
                    e18=Entry(root2,font="times 20 bold")
                    e18.grid(row=5,column=1)
                    Label(root2,text='Interest_Age_Group3(18-25).',font="times 20 bold",bg='Powder blue',pady=10).grid(row=6,column=0)
                    e19=Entry(root2,font="times 20 bold")
                    e19.grid(row=6,column=1)
                    Label(root2,text='Interest_Age_Group4(25-32).',font="times 20 bold",bg='Powder blue',pady=10).grid(row=7,column=0)
                    e20=Entry(root2,font="times 20 bold")
                    e20.grid(row=7,column=1)
                    Label(root2,text='Interest_Age_Group5(32-48).',font="times 20 bold",bg='Powder blue',pady=10).grid(row=8,column=0)
                    e21=Entry(root2,font="times 20 bold")
                    e21.grid(row=8,column=1)
                    Label(root2,text='Interest_Age_Group6(48-55).',font="times 20 bold",bg='Powder blue',pady=10).grid(row=9,column=0)
                    e22=Entry(root2,font="times 20 bold")
                    e22.grid(row=9,column=1)
                    Label(root2,text='Interest_Age_Group7(55-60).',font="times 20 bold",bg='Powder blue',pady=10).grid(row=10,column=0)
                    e23=Entry(root2,font="times 20 bold")
                    e23.grid(row=10,column=1)
                    p=[]
                    def show_message():
                         q=[(e16.get(),e17.get(),e18.get(),e19.get(),e20.get(),e21.get(),e22.get(),e23.get())]
                         i=0
                         p.append(e16.get())
                         for i in range (len(p)-1):
                             if p[i]==e16.get():
                                 i=i+1;
                                 showerror('error','Duplicate data')
                                 break;
                         if e16.get=='' and e17.get()=='' and e18.get()=='' and e19.get()=='' and e20.get()=='':
                             showerror('Error','Field is Empty')
                             e16.delete(0,END)
                             e17.delete(0,END)
                             e18.delete(0,END)
                             e19.delete(0,END)
                             e20.delete(0,END)
                             e21.delete(0,END)
                             e22.delete(0,END)
                             e23.delete(0,END)
                         else:
                             cur.executemany('insert into plcy(Policy_Name,agegrp1,agegrp2,agegrp3,agegrp4,agegrp5,agegrp6,agegrp7) values(?,?,?,?,?,?,?,?)',q)
                             cur.fetchall()
                             con.commit()
                             e16.delete(0,END)
                             e17.delete(0,END)
                             e18.delete(0,END)
                             e19.delete(0,END)
                             e20.delete(0,END)
                             e21.delete(0,END)
                             e22.delete(0,END)
                             e23.delete(0,END)
                             showinfo('Successfully','Stored Data')
                             root2.destroy()
                    Button(root2,text="Submit",bd=3,command=show_message,font="times 23 bold").grid(row=11,column=1,sticky='W')
                    Button(root2,text="Back",bd=3,command=root2.destroy,font="times 23 bold").grid(row=11,column=2,sticky='E')
                    root2.mainloop()

                #   LIST OF POLICY TO BE DISPLAYED.......

                    
                def list_plcy():
                        root4=Toplevel()
                        root4.title('List Policy')
                        root4.geometry('1700x1700')
                        root4.configure(bg='Powder blue')
                        icon=ImageTk.PhotoImage(file='logo.gif')
                        Label(root4,image=icon).grid(row=0,column=0,sticky=W)
                        Label(root4,text="LIFE INSURANCE CORPORATION OF INDIA",font="times 35 bold",bg='Powder blue').grid(row=0,column=1,columnspan=3,sticky=W)
                        Label(root4,text="Details Are",font="times 25 bold",bg='Powder blue').grid(row=1,column=0)
                        cur.execute('select * from plcy')
                        c=cur.fetchall()
                        m=0.2
                        n=0.3
                        for li in c:
                            Label(root4,text=li,bg='Powder blue',font="times 15 bold").place(relx=0.01,rely=n)
                            n=n+0.1
                        Button(root4,text="Back",command=root4.destroy,font="timees 20 bold").place(relx=0.5,rely=0.5)
                        root4.mainloop()

                # DELETE POLICY DETAILS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                #......................................................................................................................................................................

                def close_list():
                    root5=Toplevel()
                    root5.title('Delete Policy')
                    root5.geometry('1700x1700')
                    root5.configure(bg='Powder blue')
                    icon=ImageTk.PhotoImage(file='logo.gif')
                    Label(root5,image=icon).grid(row=0,column=0,sticky=W)
                    Label(root5,text="LIFE INSURANCE CORPORATION OF INDIA",font="times 35 bold",bg='Powder blue',padx=35,pady=15).grid(row=0,column=1,columnspan=3,sticky=W)
                    Label(root5,text="Serial Policy ",font="times 20 bold",bg='Powder blue',pady=30,padx=10).grid(row=1,column=1,sticky=W)
                    e1=Entry(root5,font="times 20 bold")
                    e1.grid(row=1,column=2)
                    def close_list_info():
                        a=(e1.get(),)
                        cur.execute('delete from plcy where Serial_No=?',a)
                        cur.fetchall()
                        con.commit()
                        e1.delete(0,END)
                        showinfo('Success','Deleted')
                    Button(root5,text="Submit",command=close_list_info,font="times 15 bold").grid(row=3,column=1,sticky=E)
                    Button(root5,text="Back",command=root5.destroy,font="times 15 bold").grid(row=3,column=2,sticky=E)
                    root5.mainloop()
                
                    # FUNCTION TO CLOSE YOUR ACCOUNT.......

                def close_account():
                    root_close=Toplevel()
                    root_close.title('Close_Account')
                    root_close.geometry('1700x1700')
                    root_close.configure(bg='Powder blue')
                    icon25=ImageTk.PhotoImage(file='1.gif')
                    Label(root_close,image=icon25).grid(row=0,column=0,sticky=W)
                    Label(root_close,text="LIFE INSURANCE CORPORATION OF INDIA",font="times 30 bold",bg='Powder blue').grid(row=0,column=1,columnspan=3,sticky=W)
                    Label(root_close,text="Enter Policy_Number ",font="times 25 bold",pady=20,bg='Powder blue').grid(row=1,column=0,columnspan=1)
                    c1=Entry(root_close,font="times 25 bold")
                    c1.grid(row=1,column=1)
                    def close_info():
                        a=(c1.get(),)
                        cur.execute('select Premium_Amount from ins1 where Policy_Number=?',a)
                        b=cur.fetchall()
                        Label(root_close,text="Benifit got : "+str(b),font="times 25 bold").grid(row=3,column=0)
                        cur.execute('delete from ins1 where Policy_Number=?',a)
                        cur.fetchall()   
                        showinfo('Successfully ','Closed Account')
                    Button(root_close,text='Submit',command=close_info,font="times 15 bold").grid(row=2,column=0,columnspan=2)
                    Button(root_close,text='Back',command=root_close.destroy,font="times 15 bold").grid(row=2,column=1,columnspan=2)
                    root_close.mainloop()
                    


                        


                    #FUNCTION FOR PAYMENT OF PREMIUM ....
                def pay_amount():
                    root_pay=Toplevel()
                    root_pay.geometry('1700x1700')
                    root_pay.configure(bg='Powder blue')
                    icon=ImageTk.PhotoImage(file='logo.gif')
                    Label(root_pay,image=icon).grid(row=0,column=0,sticky=W)
                    Label(root_pay,text="LIFE INSURANCE CORPORATION OF INDIA",font="times 30 bold",bg='Powder blue').grid(row=0,column=1,columnspan=3,sticky=W)
                    Label(root_pay,text='Enter Policy Number ',font='times 25 bold ',pady=15,bg='Powder blue').grid(row=1,column=0)
                    p1=Entry(root_pay,font="times 25 bold")
                    p1.grid(row=1,column=1)
                    Label(root_pay,text='Enter Amount To Pay ',font='times 25 bold ',bg='Powder blue').grid(row=2,column=0)
                    p2=Entry(root_pay,font="times 25 bold")
                    p2.grid(row=2,column=1)
                    def show_Amount_Message():
                        '''b=(p1.get(),)
                        cur.execute('select Premium_Amount from ins1 where Policy_Number=?',b)
                        d=cur.fetchall()
                        e=int(d)
                        print e'''
                            
                    
                    #   CALCULATION OF PREMIUM.........
                        def premium_cal():
                            b=(p1.get(),)
                            cur.execute('select age from ins1 where Policy_Number =?',b)
                            x=cur.fetchall()
                            age=x[0][0]
                            print age
                            cur.execute('select Policy_Name from ins1 where Policy_Number =?',b)
                            s=cur.fetchall()
                            y=s[0]
                            print y
                            if age>5 and age<10:
                                cur.execute('select agegrp1 from plcy where Policy_Name =?',y)
                                z=cur.fetchall()
                                print z
                                cur.execute('select Amount_Paid from ins1 where Policy_Number =?',b)
                                o=cur.fetchall()
                                print o[0][0]
                                a=z[0][0]
                                amount =(o[0][0]*a)/100.0
                                benefit=o[0][0]+amount
                                print benefit
                                cur.execute('update ins1 set Benefit=(select Benefit from ins1 where Policy_Number=(?))+(?) where Policy_Number=(?)',(p1.get(),benefit,p1.get()))
                                con.commit()
                                
                            elif age>10 and age<18:
                                cur.execute('select agegrp2 from plcy where Policy_Name =?',y)
                                z=cur.fetchall()
                                print z
                                cur.execute('select Amount_Paid from ins1 where Policy_Number =?',b)
                                o=cur.fetchall()
                                print o[0][0]
                                a=z[0][0]
                                amount =(o[0][0]*a)/100.0
                                benefit=o[0][0]+amount
                                print benefit
                                cur.execute('update ins1 set Benefit=(select Benefit from ins1 where Policy_Number=(?))+(?) where Policy_Number=(?)',(p1.get(),benefit,p1.get()))
                                con.commit()
                            
                            elif age>18 and age<25:
                                cur.execute('select agegrp3 from plcy where Policy_Name =?',y)
                                z=cur.fetchall()
                                print z
                                cur.execute('select Amount_Paid from ins1 where Policy_Number =?',b)
                                o=cur.fetchall()
                                print o[0][0]
                                a=z[0][0]
                                
                                amount =(o[0][0]*a)/100.0
                                benefit=o[0][0]+amount
                                print benefit
                                cur.execute('update ins1 set Benefit=(select Benefit from ins1 where Policy_Number=(?))+(?) where Policy_Number=(?)',(p1.get(),benefit,p1.get()))
                                con.commit()
                            
                            elif age>25 and age<32:
                                cur.execute('select agegrp4 from plcy where Policy_Name =?',y)
                                z=cur.fetchall()
                                print z
                                cur.execute('select Amount_Paid from ins1 where Policy_Number =?',b)
                                o=cur.fetchall()
                                print o[0][0]
                                
                                a=z[0][0]
                                amount =(o[0][0]*a)/100.0
                                benefit=o[0][0]+amount
                                print benefit
                                cur.execute('update ins1 set Benefit=(select Benefit from ins1 where Policy_Number=(?))+(?) where Policy_Number=(?)',(p1.get(),benefit,p1.get()))
                                con.commit()
                            
                            elif age>32 and age<48:
                                cur.execute('select agegrp5 from plcy where Policy_Name =?',y)
                                z=cur.fetchall()
                                print z
                                cur.execute('select Amount_Paid from ins1 where Policy_Number =?',b)
                                o=cur.fetchall()
                                print o[0][0]
                                
                                a=z[0][0]
                                amount=0
                                amount =(o[0][0]*a)/100.0
                                benefit=o[0][0]+amount
                                print benefit
                                cur.execute('update ins1 set Benefit=(select Benefit from ins1 where Policy_Number=(?))+(?) where Policy_Number=(?)',(p1.get(),benefit,p1.get()))
                                con.commit()
                            
                            elif age>48 and age<55:
                                cur.execute('select agegrp6 from plcy where Policy_Name =?',y)
                                z=cur.fetchall()
                                print z
                                cur.execute('select Amount_Paid from ins1 where Policy_Number =?',b)
                                o=cur.fetchall()
                                print o[0][0]
                                a=z[0][0]
                                amount=0
                                amount =(o[0][0]*a)/100.0
                                benefit=o[0][0]+amount
                                print benefit
                                cur.execute('update ins1 set Benefit=(select Benefit from ins1 where Policy_Number=(?))+(?) where Policy_Number=(?)',(p1.get(),benefit,p1.get()))
                                con.commit()
                            
                            elif age>55 and age<60:
                                cur.execute('select agegrp7 from plcy where Policy_Name =?',y)
                                z=cur.fetchall()
                                print z
                                cur.execute('select Amount_Paid from ins1 where Policy_Number =?',b)
                                o=cur.fetchall()
                                print o[0][0]
                                a=z[0][0]
                                amount=0
                                amount =(o[0][0]*a)/100.0
                                benefit=o[0][0]+amount
                                print benefit
                                cur.execute('update ins1 set Benefit=(select Benefit from ins1 where Policy_Number=(?))+(?) where Policy_Number=(?)',(p1.get(),benefit,p1.get()))
                                con.commit()
                        premium_cal()  
                            

                        # calculation of No. of installments.......
                        b=(p1.get(),)
                        cur.execute('select Paymode_Mode,No_Of_Years from ins1 where Policy_Number=?',b)
                        z=cur.fetchall()
                        print z
                        mode=0
                        if str(z[0][0])=="Quaterly":
                            mode=4
                        elif str(z[0][0])=="Half Yearly":
                            mode=2
                        elif str(z[0][0])=="Yearly":
                            mode=1
                        installment=mode*int(z[0][1])
                        print installment
                        cur.execute('select No_Of_Installment from ins1 where Policy_Number=?',b)
                        x=cur.fetchall()
                        if x[0] <= installment:
                            showerror('Error','Premium Amount Completed ')
                        else:
                            cur.execute('select Premium_Amount from ins1 where Policy_Number=?',b)
                            v=cur.fetchall()
                            print v[0][0]
                            k=v[0][0]/installment
                            f=x[0][0]
                            f=f+1
                            if int(p2.get())== k:
                                
                                def we():
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
                                                cur.execute('update ins1 set Amount_Paid=(select Amount_Paid from ins1 where Policy_Number=(?))+(?) where Policy_Number=(?)',(p1.get(),p2.get(),p1.get()))
                                                con.commit()
                                                cur.execute('update ins1 set No_Of_Installment=? where Policy_Number=(?)',(f,p1.get()))
                                                cur.fetchall()
                                                con.commit()
                                                r6.destroy()
                                                q1.destroy()
                                                a1.destroy()
                                                
                                                
                                            else:
                                                showinfo('Information','payment Processing')
                                                time.sleep(3)
                                                showerror('Error','WRONG OTP')
                                                q1.destroy()
                                                a1.destroy()
                                                
                                        Button(a1,text='Pay',command=u).grid(row=2,column=0)
                                        a1.mainloop()        
                                    q1.mainloop()
                                we()
                                    #os.startfile("Payment.py")
                                #showinfo('Info','DATA UPDATED')
                            else:
                                showerror('Error','Invalid Amount')
                    p1.delete(0,END)
                    p2.delete(0,END)
                    Button(root_pay,text='Proceed',command=show_Amount_Message,font="times 20 bold").grid(row=3,column=1)
                    Button(root_pay,text="Back",command=root_pay.destroy,font="times 20 bold").grid(row=3,column=2,sticky=E)
                    root_pay.mainloop()
                    



                    
     #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#                   
     #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                
                # FUNCTION TO JUDGE THE CHOICE OF USESR SELECTED....

                def jugde():
                    c=int(v1.get())
                    if c == 1:                                       # 1. RADIO_BUTTON
                        create()
                        insert1()                                    
                    elif c == 2:                                     # 2. RADIO_BUTTON
                        search_info()
                    elif c == 3:                                     #  3. RADIO_BUTTON
                        create_listplcy()                            
                        insert_listplcy()
                    elif c==4:                                       #  4. RADIO_BUTTON
                        list_plcy()      
                    elif c == 5:                                     #  5. RADIO_BUTTON
                        close_account()
                    elif c == 6:                                     #  6. RADIO_BUTTON
                        pay_amount()
                    elif c == 7:
                        close_list()                                 # 7. RADIO_BUTTON
                Button(root,text='OK',font="times 25 bold",command=jugde,bd=3).grid(row=10,column=1,sticky='W')
                root.mainloop()
            else :

                Label(root_login,text='Wrong Password',font='times 15 bold').place(relx=0.50,rely=0.60)
    Button(root_login,text='Login',command=log,bd=5,font="times 22 bold",pady=3,padx=5,bg='paleturquoise').place(relx=.55,rely=.54,anchor=CENTER)#grid(row=5,column=1,sticky=W+S+N)
    root_login.mainloop()

fun()






