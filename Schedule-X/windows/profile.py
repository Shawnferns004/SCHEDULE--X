import customtkinter as ct 
import tkinter as tk 
from tkinter import messagebox
import os
import sqlite3


pid = os.environ.get('PID')
name = os.environ.get('NAME')
roll = os.environ.get('ROLL_DATA')
sec = os.environ.get('SEC')
branch = os.environ.get('BRANCH')
batch = os.environ.get('BATCH')
email = os.environ.get('EMAIL')

pro = ct.CTk()
width = 900
height = 650
pro.geometry(f"{width}x{height}+{750}+{170}")
pro.overrideredirect(1)

f=ct.CTkFrame(
    master= pro,
    height=700,
    width=950
).pack()


ff=ct.CTkFrame(
    master=f,
    height=610,
    width=870,
    corner_radius=20,
    fg_color="#212120",
    bg_color="#2a2b2a",
    border_color="black",
    border_width=3
).place(x=13,y=18)

font1=("game of squids",50,"bold")
font2=("consolas",20,"bold")
lbl1=ct.CTkLabel(
    master=ff,
    text="< PROFILE >",
    font=font1,
    fg_color="#212120"

).place(x=260, y=30)

lbl2=ct.CTkLabel(
    master=ff,
    text="Name :",
    font=font2,
    fg_color="#212120"

).place(x=40, y=150)

lbl3=ct.CTkLabel(
    master=ff,
    text="PID :",
    font=font2,
    fg_color="#212120"

).place(x=40, y=200)
lbl4=ct.CTkLabel(
    master=ff,
    text="Roll No :",
    font=font2,
    fg_color="#212120"

).place(x=40, y=250)

lbl5=ct.CTkLabel(
    master=ff,
    text="Email :",
    font=font2,
    fg_color="#212120"

).place(x=40, y=300)
lbl6=ct.CTkLabel(
    master=ff,
    text="Department :",
    font=font2,
    fg_color="#212120"

).place(x=40, y=350)
lbl7=ct.CTkLabel(
    master=ff,
    text="Class :",
    font=font2,
    fg_color="#212120"

).place(x=40, y=400)
lbl8=ct.CTkLabel(
    master=ff,
    text="Batch :",
    font=font2,
    fg_color="#212120"

).place(x=40, y=450)



back = ct.CTkButton(
        ff,
        text="CLOSE",
        font=("consolas", 18, 'bold'),
        hover=False,
        fg_color="black",
        height=40,
        width=150,
        command=lambda: pro.destroy()
)
back.place(x=400, y=500)





lb2=ct.CTkLabel(
    master=ff,
    text=name,
    font=font2,
    fg_color="#212120"

).place(x=250, y=150)

lb3=ct.CTkLabel(
    master=ff,
    text=pid,
    font=font2,
    fg_color="#212120"

).place(x=250, y=200)
lb4=ct.CTkLabel(
    master=ff,
    text=roll,
    font=font2,
    fg_color="#212120"

).place(x=250, y=250)

lb5=ct.CTkLabel(
    master=ff,
    text=email,
    font=font2,
    fg_color="#212120"

).place(x=250, y=300)
lb6=ct.CTkLabel(
    master=ff,
    text=branch,
    font=font2,
    fg_color="#212120"

).place(x=250, y=350)
lb7=ct.CTkLabel(
    master=ff,
    text=sec,
    font=font2,
    fg_color="#212120"

).place(x=250, y=400)
lb8=ct.CTkLabel(
    master=ff,
    text=batch,
    font=font2,
    fg_color="#212120"

).place(x=250, y=450)


pro.mainloop()