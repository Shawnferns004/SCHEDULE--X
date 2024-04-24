import customtkinter as ct
from PIL import ImageTk,Image
import os
from tkinter import messagebox
import tkinter as tk
import sqlite3


s = ct.CTk()
#<-----------frame settings-------------->
width=1200
height=740
# x=(s.winfo_screenwidth()//15)-(-width//10)
# y=(s.winfo_screenheight()//2)-(height//2)
s.geometry("1350x740+350+150")
#<-------------xxxxx------------------->


#<-----------Navbar------------>
nav =ct.CTkFrame(master=s,height=722,width=230)
nav.place(x=10,y=10)

#<-----------xxxx------------->


#<----------Main window--------------->
main_f = ct.CTkFrame(
    master=s,
    height=722,
    width=1099
)
main_f.place(x=245,y=10)
main_f.propagate(False)




#<--------xxxxx---------------------->

#<------------logo-------------->
lbl = ct.CTkLabel(
    nav,
    text="Schedule",
    font=('Game of Squids',20,'bold')
).place(x=12,y=15)

lb2 = ct.CTkLabel(
    nav,
    text="X",
    font=('Game of Squids',45,'bold')
).place(x=160,y=1)

#<-------------buttons--------------->

#profile btn
add_S = ct.CTkButton(
    master=nav,
    text='Add Students',
    font=('Consolas',15,'bold'),
    fg_color="black",
    width=200,
    height=40,
    corner_radius=0,
    hover_color="grey",
    text_color="orange",
    command=lambda:stud()
).place(x=12,y=100)


#timetable btn
add_T = ct.CTkButton(
    master=nav,
    text='Add Faculty',
    font=('Consolas',15,'bold'),
    fg_color="black",
    width=200,
    height=40,
    hover_color="grey",
    text_color="orange",
    corner_radius=0,
    command=lambda:fac()
).place(x=12,y=150)

#pass btn
add_Sub = ct.CTkButton(
    master=nav,
    text='Add Subjects',
    font=('Consolas',15,'bold'),
    fg_color="black",
    width=200,
    text_color="orange",
    height=40,
    hover_color="grey",
    corner_radius=0,
    command=lambda:sub()
).place(x=12,y=200)

shedule = ct.CTkButton(
    master=nav,
    text='Schedule Time Table',
    font=('Consolas',15,'bold'),
    fg_color="black",
    width=200,
    text_color="orange",
    height=40,
    hover_color="grey",
    corner_radius=0,
    command=lambda:shed()
).place(x=12,y=250)

tt_s = ct.CTkButton(
    master=nav,
    text='Student Time-Table',
    font=('Consolas',15,'bold'),
    fg_color="black",
    width=200,
    text_color="orange",
    height=40,
    hover_color="grey",
    corner_radius=0,
    command=lambda:std_t()
).place(x=12,y=300)

tt_t = ct.CTkButton(
    master=nav,
    text='Faculty Time-Table',
    font=('Consolas',15,'bold'),
    fg_color="black",
    width=200,
    text_color="orange",
    height=40,
    hover_color="grey",
    corner_radius=0,
    command=lambda:fac_t()
).place(x=12,y=350)

noti = ct.CTkButton(
    master=nav,
    text='Notify',
    font=('Consolas',15,'bold'),
    fg_color="black",
    width=200,
    text_color="orange",
    height=40,
    hover_color="grey",
    corner_radius=0,
    command=lambda:notify()
).place(x=12,y=400)

#logout btn
image =ct.CTkImage(
    Image.open('windows/images/log.png')
)
log_out = ct.CTkButton(
    master=nav,
    text='LOG OUT',
    font=('Consolas',15,'bold'),
    fg_color="black",
    width=200,
    image=image,
    height=40,
    corner_radius=0,
    hover_color="grey",
    command=lambda:out()
).place(x=12,y=660)



#<-------------xxxxxxxx------------>


#<-------indicator------------>
pro_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
).place(x=8,y=100)

pass_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
).place(x=8,y=150)

tt_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
).place(x=8,y=200)

tt_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
).place(x=8,y=250)

tt_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
).place(x=8,y=300)

tt_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
).place(x=8,y=350)

tt_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
).place(x=8,y=400)

#<----------xxxx--------------->





#<--------on clicks --------->
def stud():
    os.system('python windows\\student.py')

def notify():
    os.system('python windows\\notify.py')

def fac():
    os.system('python windows\\add_teacher.py')
def sub():
    os.system('python windows\\add_subject.py')
def fac_t():
    os.system('python windows\\timetable_fac.py')
def std_t():
    os.system('python windows\\timetable_stud.py')
def shed():
    os.system('python windows\\section.py')
def out():
    res=messagebox.askquestion('Warning','Do you really want to logout?', icon='warning')
    if res=="Yes" or "yes":
        s.destroy()
        os.system('python windows\\main.py')
    else:
        pass




s.mainloop()