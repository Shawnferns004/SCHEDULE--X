import tkinter 
import customtkinter as ct
from tkinter import ttk
from tkinter import messagebox
import os
import random
import smtplib


import sqlite3
from PIL import ImageTk,Image,ImageFilter

ct.set_default_color_theme("green")
ct.set_appearance_mode("dark")

con=sqlite3.connect(r'files/timetable.db')

det = ct.CTk()
det.title("ScheduleX")
det.iconbitmap("windows/images/favicon.ico")
width=730
height=600
x=(det.winfo_screenwidth()//7)-(-width//2)
y=(det.winfo_screenwidth()//4)-(height//2)
det.geometry(f"{width}x{height}+{x}+{y}")
det.grab_set()
det.focus_force()
    # det.overrideredirect(1) 

bg=Image.open("windows\images\pattern.png")
img = ImageTk.PhotoImage(bg)
l1=ct.CTkLabel(master=det ,image=img)
l1.pack()

    
det.geometry(f"{width}x{height}+{x}+{y}")

f= ct.CTkFrame(master=l1, width=600,height=500,border_width=3,corner_radius=15)
f.place(relx=0.5 ,rely=0.5, anchor=tkinter.CENTER)

lb = ct.CTkLabel(
    f,
    text="CHANGE PASSWORD",
    font=('Consolas',28,'bold')
)
lb.place(x=200,y=20)
   
email = ct.CTkEntry(
    f,
    placeholder_text="Enter Email...",
    height=40,
    width=400,
    corner_radius=40
)
email.place(x=100,y=100)

back = ct.CTkButton(
    f,
    text="Send OTP",
    font=("consolas",15,'bold'),
    hover=False,
    fg_color="black",
    height=40,
    width=60,
    command=lambda:connectingSender()
).place(x=250,y=160)
    
otp = ct.CTkEntry(
    f,
    placeholder_text="Enter otp...",
    height=40,
    width=400,
    corner_radius=40
)
otp.place(x=100,y=220)


back = ct.CTkButton(
    f,
    text="Back",
    font=("consolas",15,'bold'),
    hover=False,
    fg_color="black",
    height=40,
    width=60,
    command=lambda:back()
).place(x=260,y=500)

vrify = ct.CTkButton(
    f,
    text="Verify",
    font=("consolas",15,'bold'),
    hover=False,
    fg_color="#388E3C",
    height=37,
    width=60,
    command=lambda:checkOtp()
).place(x=265,y=300)

    
change = ct.CTkEntry(
    f,
    placeholder_text="Enter new password...",
    height=40,
    width=400,
    corner_radius=40
)
change.place(x=100,y=370)

change_pass = ct.CTkButton(
    f,
    text="CHANGE PASSWORD",
    font=("consolas",15,'bold'),
    hover=False,
    fg_color="#388E3C",
    height=37,
    width=60,
    command=lambda:passw()
).place(x=230,y=430)

back = ct.CTkButton(
    f,
    text="Back",
    font=("consolas",15,'bold'),
    hover=False,
    fg_color="black",
    height=37,
    width=30,
    command=lambda:back()
).place(x=370,y=430)



def back():
    det.destroy()
    os.system('python windows\\main.py')


def generateOtp():
    randomCode="".join(str(random.randint(0,9)) for i in range(6))
    return randomCode
    

sender = 'shawnferns004@gmail.com'
password = 'ynht dozr gjvj xqzu'
code = generateOtp()


def connectingSender():
    receiver = str(email.get())

    cur=con.execute(F"SELECT EMAIL FROM STUDENT WHERE EMAIL='{email.get()}'")
    em=cur.fetchone()
    cur2=con.execute(F"SELECT EMAIL FROM FACULTY WHERE EMAIL='{receiver}'")
    em1=cur2.fetchone()

    if em:

        messagebox.showinfo("Sucess","Otp Sent. Please check your email.")
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender,password)
        sendingMail(receiver,server)
    elif em1:
        messagebox.showinfo("Sucess","Otp Sent. Please check your email.")
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender,password)
        sendingMail(receiver,server)
    else:
        messagebox.showerror("Error","Email not found.")
        email.delete(0,'end')


def sendingMail(receiver,server):
    msg = (f"Hello! Your Verification Code is {code} ")
    server.sendmail(sender,receiver,msg)
    server.quit()

def checkOtp():
    if code == otp.get():
        accept = ct.CTkLabel(
            f,
            text="Verified Successfully",
            font=("consolas",15,"bold"),
            text_color="green"
        )
        accept.place(x=220,y=260)
    else:
        refuse= ct.CTkLabel(
            f,
            text="Wrong OTP Entered",
            font=("consolas",15,"bold"), 
            text_color="red"
        )
        refuse.place(x=220,y=260)
        otp.delete(0,'end')
        
def passw():
    con.execute(f"UPDATE STUDENT SET PASSW ='{change.get()}' WHERE EMAIL='{email.get()}'")
    con.commit()
    messagebox.showinfo("Sucess", "Password Changed Succesfully")

    email.delete(0, 'end')
    otp.delete(0,'end')
    change.delete(0,'end')



det.mainloop()


        