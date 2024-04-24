import customtkinter as ct 
from tkinter import messagebox
import tkinter as tk
from plyer import notification
import time
import sqlite3
from email.message import EmailMessage
import ssl
import smtplib


app =ct.CTk()
app.title("Notification")
width = 800
height = 600
x=(app.winfo_screenwidth()//7)-(-width//2)
y=(app.winfo_screenheight()//2)-(height//2)
app.geometry(f"{width}x{height}+{x}+{y}")
app.config(bg="#2b2a2a")
app.overrideredirect(1) 


main_f = ct.CTkFrame(
    master=app,
    height=580,
    width=780,
    fg_color="#242424",
    corner_radius=10,
    bg_color="#2b2a2a"
)
main_f.place(x=10,y=10)
main_f.propagate(False)


font1=("Consolas",15,"bold")
font=('Game of Squids',40,'bold')
lbl = ct.CTkLabel(
    master=main_f,
    text="NOTIFy",
    font=font,
    bg_color="#2b2a2a",
    corner_radius=10,
    width=100,
    height=40,
    fg_color="#242424"
).place(x=290,y=10)

lbl1 = ct.CTkLabel(
    master=main_f,
    text="Type Message....",
    font=font1,
    bg_color="#2b2a2a",
    corner_radius=10,
    width=100,
    height=40,
    fg_color="#242424"
).place(x=2,y=110)

lbl2 = ct.CTkTextbox(
    master=main_f,
    # text="Type Message....",
    font=font1,
    bg_color="#2b2a2a",
    corner_radius=10,
    width=750,
    height=330,
    fg_color="white",
    text_color="black"
)
lbl2.place(x=15,y=150)

def set_focus(event):
    lbl2.focus_set()

# Bind an event to set focus on the text box
app.bind("<Map>", set_focus)

btn_clear = ct.CTkButton(
    master=main_f,
    text="Clear",
    height=40,
    hover=False,
    fg_color="#F45050",
    font=("consolas",18,"bold"),
    # text_color="black"
    command=lambda:clear()
)
btn_clear.place(x=230,y=500)


def clear():
    lbl2.delete('1.0', tk.END)

btn_send = ct.CTkButton(
    master=main_f,
    text="SEND",
    height=40,
    hover=False,
    fg_color="#9BCF53",
    font=("consolas",18,"bold"),
    # text_color="black"
    command=lambda:send()
)
btn_send.place(x=390,y=500)

btn_back = ct.CTkButton(
        main_f,
        text="BACK",
        font=('Consolas', 12, 'bold'),
        command=lambda:back(),
        width=100,
        height=40,
        fg_color="grey",
        hover=False,
        corner_radius=10
).place(x=80,y=500)
 
def back():
    app.destroy()




def send():
    msg=lbl2.get("1.0", tk.END)
    
    con = sqlite3.connect(r'files/timetable.db')

    cur= con.cursor()

    cur.execute("SELECT EMAIL FROM STUDENT")
    row=['. '.join(map(str,row)) for row in cur.fetchall()]

    email_sender = 'shawnferns004@gmail.com'
    email_pass = "ynht dozr gjvj xqzu"

    email_receiver = row

    subject = "Time table update"

    body= msg

    em= EmailMessage()
    em['From']= email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_pass)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
        print("sent")

    

    lbl2.delete("1.0", tk.END)

app.mainloop()