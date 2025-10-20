# Import Modules
from tkinter import *
import os
import random
from tkinter import messagebox
from time import gmtime, strftime
import yfinance as yf
import matplotlib.pyplot as plt



#Main Screen
master = Tk()
master.title('Banking App')
lst_check=[]


#Functions
def clear_screen():
    for widget in master.winfo_children():
        widget.destroy()



def register():
    clear_screen()
    #Vars
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    #Register Screen
    
    master.title('Register')

    #Labels
    Label(master, text="Please enter your details below to register", font=('Calibri',45),bg = color).place(x=230,y=10)
    Label(master, text="Name:", font=('Calibri',30),bg = color).place(x=500,y=150)
    Label(master, text="Age:", font=('Calibri',30),bg = color).place(x=500,y=250)
    Label(master, text="Gender:", font=('Calibri',30),bg = color).place(x=500,y=350)
    Label(master, text="Password:", font=('Calibri',30),bg = color).place(x=500,y=450)
    Label(master, text="Type of account:", font=('Calibri',30),bg = color).place(x=100,y=550)


    #Entries
    Entry(master,textvariable=temp_name,font=('Calibri',20)).place(x=630,y=160)
    Entry(master,textvariable=temp_age,font=('Calibri',20)).place(x=600,y=260)
    Entry(master,textvariable=temp_gender,font=('Calibri',20)).place(x=650,y=360)
    Entry(master,textvariable=temp_password,show="*",font=('Calibri',20)).place(x=700,y=460)

    #Buttons
    Button(master, text="Register", command = finish_reg, font=('Calibri',20)).place(x=600,y=650)
    Button(master, text="Back", command = back_mainscreen , font=('Calibri',20)).place(x=800,y=650)
    #Radio Button
    var=IntVar()
    Radiobutton(master,text="Current Account",variable=var,value=1, font=('Calibri',20),bg = color).place(x=400,y=550)
    Radiobutton(master,text="Savings Account",variable=var,value=2, font=('Calibri',20),bg = color).place(x=630,y=550)
    Radiobutton(master,text="Fixed Deposit Account",variable=var,value=3, font=('Calibri',20),bg = color).place(x=850,y=550)
    Radiobutton(master,text="Recurring Deposit Account",variable=var,value=4, font=('Calibri',20),bg = color).place(x=1150,y=550)
    


def finish_reg():
    global acno
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()
    acno= random.randint(100000000000,999999999999)

    if name == "" or age == "" or gender == "" or password == "":
        messagebox.showinfo("Details","All fields requried * ")
        return

    for name_check in all_accounts:
        lst_check.append(name_check)
    if name == name_check:
        messagebox.showinfo("Details","Account already exists")
        return
    else:
        # Creating User Database
        new_file = open(name,"a")
        new_file.write(name+'\n')
        new_file.write(password+'\n')
        new_file.write(age+'\n')
        new_file.write(gender+'\n')
        new_file.write(str(acno)+'\n')
        new_file.write('0')
        new_file.close()

        # Creating User Database
        f1=open("Accnt_Record.txt",'a')
        f1.write(str(acno)+'\n')
        f1.close()

        
        frec=open(str(acno)+"-rec.txt",'a')
        frec.write("Date                                                  Credit        Debit            Balance\n")
        frec.close()

        messagebox.showinfo("Details","Account has been created And Your Account Number is "+str(acno))
        return


def login():
    clear_screen()
    #Vars
    global temp_login_name
    global temp_login_password
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    
    master.title('Login')
    #Labels
    Label(master, text="Please enter your details below to register", font=('Calibri',45),bg = color).place(x=230,y=10)
    Label(master, text="Username:", font=('Calibri',30),bg = color).place(x=500,y=250)
    Label(master, text="Password:", font=('Calibri',30),bg = color).place(x=500,y=400)

    #Entry
    Entry(master, textvariable=temp_login_name, font=('Calibri',20)).place(x=700,y=260)
    Entry(master, textvariable=temp_login_password,show="*", font=('Calibri',20)).place(x=690,y=410)
    #Button
    Button(master, text="Login", command=login_session, width=15,font=('Calibri',20)).place(x=630,y=600)
    Button(master, text="Back", command =back_mainscreen , font=('Calibri',20)).place(x=920,y=600)




def login_session():
    clear_screen()
    global login_name
    global login_password
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all_accounts:
        if name == login_name:
            file = open(name,"r")
            file_data = file.read()
            file_data = file_data.split('\n')
            passwor  = file_data[1]
            file.close() 
            #Account Dashboard
            if login_password == passwor:      
                master.title('Dashboard')
                #Labels
                Label(master, text="Account Dashboard", font=('Calibri',50),bg = color).place(x=510,y=5)
                Label(master, text="----------------------------------------------------------------------------------------------", font=('Calibri',40, 'bold'),bg = color).place(x=0,y=350)
                #Buttons
                Button(master, text="Personal Details",font=('Calibri',20),width=30,command=personal_details).place(x=30,y=100)
                Button(master, text="Deposit Money",font=('Calibri',20),width=30,command=deposit).place(x=530,y=100)
                Button(master, text="Withdraw Money",font=('Calibri',20),width=30,command=withdraw).place(x=1030,y=100)
                Button(master, text="Display Balance",font=('Calibri',20),width=30,command=balance).place(x=30,y=200)
                Button(master, text="Change Pin",font=('Calibri',20),width=30,command=changepinto).place(x=530,y=200)
                Button(master, text="Display Bank Statement",font=('Calibri',20),width=30,command=history).place(x=1030,y=200)
                Button(master, text="Stocks Analysis",font=('Calibri',20),width=30,command=stk).place(x=30,y=300)
                Button(master, text="Quit",font=('Calibri',20),width=30,command=quit).place(x=1030,y=300)
                return
            else:
                messagebox.showinfo("Details","Password incorrect!!")
                login()
                break
    else:
        messagebox.showinfo("Details","No account found !!")
        login()


def personal_details():
    file = open(login_name, 'r')
    file_data = file.read()
    user_details = file_data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_details[5]
    file.close()
    #Personal details screen
    master.title('Personal Details')
    #Labels
    Label(master, text="Personal Details", font=('Calibri',40),bg = color).place(x=600,y=400)
    Label(master, text="Name : "+details_name, font=('Calibri',30),bg = color).place(x=50,y=500)
    Label(master, text="Age : "+details_age, font=('Calibri',30),bg = color).place(x=450,y=500)
    Label(master, text="Gender : "+details_gender, font=('Calibri',30),bg = color).place(x=800,y=500)
    Label(master, text="Balance :Rs."+details_balance, font=('Calibri',30),bg = color).place(x=1200,y=500)
    # Buttons
    Button(master, text="Back", command = login_session , font=('Calibri',20)).place(x=700,y=650)


def deposit():
    #Vars
    global amount
    global acn
    amount = StringVar()
    acn=StringVar()

    #Deposit Screen
    master.title('Deposit')
    #Label
    Label(master, text="Deposit Money", font=('Calibri',40),bg = color).place(x=570,y=400)
    Label(master, text="Amount : ", font=('Calibri',30),bg = color).place(x=500,y=600)
    Label(master, text="Account number : ", font=('Calibri',30),bg = color).place(x=450,y=500)

    #Entry
    Entry(master, textvariable=acn,show="X", font=('Calibri',20)).place(x=750,y=510)
    Entry(master, textvariable=amount, font=('Calibri',20)).place(x=750,y=610)
    #Button
    Button(master,text="Finish",font=('Calibri',20),command=finish_deposit).place(x=600,y=670)
    Button(master,text="Back",font=('Calibri',20),command=login_session).place(x=800,y=670)

def finish_deposit():
    global amount
    global acno
    global acn
    if amount.get() == "":
        messagebox.showinfo("Details","Amount is required!")     
        return
    if float(amount.get()) <=0:
        messagebox.showinfo("Details","Negative currency is not accepted")
        return
    


    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[5]
    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    

    f2=open(str(acn.get())+"-rec.txt",'a')
    f2.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"         "+f"{amount.get()}"+"                                    "+f"{updated_balance}"+"\n")
    f2.close()

    messagebox.showinfo("Details","BALANCE UPDATED. CURRENT BALANCE IS : Rs."+str(updated_balance))


    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = acn.get()
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

 
def withdraw():
    #Vars
    global withdraw_amount
    global accoun
    withdraw_amount = StringVar()
    accoun =  StringVar()
    #Deposit Screen
    master.title('Withdraw')
    #Label
    Label(master, text="Withdraw Money", font=('Calibri',40),bg = color).place(x=570,y=400)
    Label(master, text="Amount : ", font=('Calibri',30),bg = color).place(x=500,y=600)
    Label(master, text="Account number : ", font=('Calibri',30),bg = color).place(x=450,y=500)

    #Entry
    Entry(master, textvariable=withdraw_amount,font=('Calibri',20)).place(x=750,y=610)
    Entry(master, textvariable=accoun,show="X",font=('Calibri',20)).place(x=750,y=510)
    #Button
    Button(master,text="Finish",font=('Calibri',20),command=finish_withdraw).place(x=600,y=670)
    Button(master,text="Back",font=('Calibri',20),command=login_session).place(x=800,y=670)


def finish_withdraw():
    global accoun
    if withdraw_amount.get() == "":
        messagebox.showinfo("Details","Amount is required!") 
        return
    if float(withdraw_amount.get()) <=0:
        messagebox.showinfo("Details","Negative currency is not accepted")
        return

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[5]

    if float(withdraw_amount.get()) >float(current_balance):
        messagebox.showinfo("Details","Insufficient Funds!")
        return

    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()


    f3=open(str(accoun.get())+"-rec.txt",'a')
    f3.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"      "+"                            "+f"{withdraw_amount.get()}"+"                "+f"{updated_balance}"+"\n")
    f3.close()

    messagebox.showinfo("Details","BALANCE UPDATED. CURRENT BALANCE IS : Rs."+str(updated_balance))


    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = accoun.get()
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

   

def balance():
    f121 = open(login_name, "r")
    file_data = f121.read()
    user_details = file_data.split('\n')
    details_balance = user_details[5]
    f121.close()
    # Deposit Screen
    master.title('Balance')
    # Label
    Label(master, text="Current Balance", font=('Calibri',40),bg = color).place(x=570,y=400)
    current_balance_label = Label(master, text="Current Balance : Rs."+details_balance, font=('Calibri',30),bg = color)
    current_balance_label.place(x=540,y=530)
    # Buttons
    Button(master,text="Back",font=('Calibri',20),command=login_session).place(x=700,y=670)




def changepinto():
    global userentryss
    global userentss
    #Deposit Screen
    master.title('Change pin')
    #Label
    Label(master, text="Change Pin", font=('Calibri',40),bg = color).place(x=570,y=400)
    Label(master, text="Enter Old Pin: ", font=('Calibri',30),bg = color).place(x=500,y=500)
    Label(master, text="Enter New Pin: ", font=('Calibri',30),bg = color).place(x=500,y=600)

    #Entry
    uservalss=StringVar()
    uservass=StringVar()
    userentryss=Entry(master,textvariable=uservalss,show="*",font=('Calibri',20))
    userentss=Entry(master,textvariable=uservass,show="*",font=('Calibri',20))
    userentss.place(x=750,y=510)
    userentryss.place(x=750,y=610)
    # Buttons
    Button(master,text="Finish",font=('Calibri',20),command=changepin).place(x=600,y=670)
    Button(master,text="Relogin",font=('Calibri',20),command=login).place(x=800,y=670)
    



def changepin(): 
    global userentryss
    global userentss

    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[1]
    if userentss.get()==current_balance:
        updated_balance = userentryss.get()
        file_data       = file_data.replace(current_balance, str(updated_balance))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        messagebox.showinfo("Details","Pin Changed Successfully.Kindly Relogin")
    else:
        messagebox.showinfo("Details","Incorrect Pin")
    file.close()    
         
    
def history():
    global accoun
    accoun =  StringVar()
	#Deposit Screen
    master.title('Bank Statement')
    #Label
    Label(master, text="Bank Statement", font=('Calibri',40),bg = color).place(x=570,y=400)
    Label(master, text="Account number : ", font=('Calibri',30),bg = color).place(x=450,y=530)
    Entry(master, textvariable=accoun,show="X",font=('Calibri',20)).place(x=760,y=540)
    Button(master,text="Finish",font=('Calibri',20),command=his).place(x=600,y=670)
    Button(master,text="Back",font=('Calibri',20),command=login_session).place(x=800,y=670)


def his():
    login_session()  
    global accoun
    current_balance_label = Label(master, text="Bank Statement", font=('Calibri',30),bg = color)
    current_balance_label.place(x=600,y=400)
 

    f21=open(str(accoun.get())+"-rec.txt",'r')
    f20=f21.readlines()
    j=450
    for line in f20:
        Label(master,anchor="w",text=line,bg = color, font=('Calibri',20)).place(x=400,y=j) 
        j=j+50
    Button(master,text="Back",font=('Calibri',18),command=login_session).place(x=700,y=690)   
    f21.close()

    
    file = open(login_name, 'r+')
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4]
    updated_balance = accoun.get()
    file_data       = file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()


def stk():
    global userva
    global userval
    global startval
    global endval
    master.title('Stock')
    # Labels
    Label(master, text="Stock Analysis", font=('Calibri',40),bg = color).place(x=570,y=400)
    Label(master, text="Company 1:", font=('Calibri',30),bg = color).place(x=100,y=500)
    Label(master, text="Company 2:", font=('Calibri',30),bg = color).place(x=800,y=500)
    Label(master, text="Start date:", font=('Calibri',30),bg = color).place(x=100,y=600)
    Label(master, text="End date:", font=('Calibri',30),bg = color).place(x=800,y=600)    
    # Entry
    userval=StringVar()
    userva=StringVar()
    userentry=Entry(master,textvariable=userval,font=('Calibri',20))
    userent=Entry(master,textvariable=userva,font=('Calibri',20))
    userent.place(x=300,y=510)
    userentry.place(x=1000,y=510) 
    startval=StringVar()
    endval=StringVar()
    startentry=Entry(master,textvariable=startval,font=('Calibri',20))
    endentry=Entry(master,textvariable=endval,font=('Calibri',20))
    startentry.place(x=300,y=610)
    endentry.place(x=1000,y=610)    
    # Buttons
    Button(master,text="Finish",font=('Calibri',20),command=stkf).place(x=600,y=670)
    Button(master,text="Back",font=('Calibri',20),command=login_session).place(x=800,y=670)


def stkf():
    stock = [userval.get(),userva.get()]
    stocks = yf.download(stock, start = startval.get(), end = endval.get())
    data = stocks.loc[:,'Close'].copy()
    data.plot(figsize = (17,8),fontsize = 18)

    plt.style.use('seaborn-v0_8-pastel')
    plt.show()



def back_mainscreen():
    clear_screen()
    Label(master, text = "Pinnacle Bank", font=('Calibri',70),bg = color).place(x=500,y=5)
        
    #Buttons
    Button(master, text="Register", font=('Calibri',20),width=20,command=register).place(x=600,y=300)
    Button(master, text="Login", font=('Calibri',20),width=20,command=login).place(x=600,y=400)
    Button(master, text="Quit", font=('Calibri',20),width=20,command=master.destroy).place(x=600,y=500)



def mainscreen():
    global master
    master.geometry(dimensions)
    Label(master, text = "Pinnacle Bank", font=('Calibri',70),bg = color).place(x=500,y=5)
        
    #Buttons
    Button(master, text="Register", font=('Calibri',20),width=20,command=register).place(x=600,y=300)
    Button(master, text="Login", font=('Calibri',20),width=20,command=login).place(x=600,y=400)
    Button(master, text="Quit", font=('Calibri',20),width=20,command=master.destroy).place(x=600,y=500)
    master.configure(background=color)
    master.mainloop()

# Main screen
color="#1EF1E4"
dimensions="1500x750+15+20"
mainscreen()