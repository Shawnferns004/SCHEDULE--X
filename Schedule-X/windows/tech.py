import customtkinter as ct
from PIL import ImageTk,Image
import os
from tkinter import messagebox
import tkinter as tk
import sqlite3

name=os.environ.get('NAME') 

conn =sqlite3.connect(r'files/timetable.db')
cur=conn.execute(f"SELECT * FROM FACULTY WHERE NAME ='{name}'")
res=cur.fetchall()
fid=res[0][1]
n=res[0][2]

s = ct.CTk()
#<-----------frame settings-------------->
width=1200
height=740
# x=(s.winfo_screenwidth()//15)-(-width//10)
# y=(s.winfo_screenheight()//2)-(height//2)
s.geometry("1200x740+500+150")

#<-------------xxxxx------------------->


#<-----------Navbar------------>
nav =ct.CTkFrame(master=s,height=722,width=230)
nav.pack(side=ct.LEFT,padx=7)

#<-----------xxxx------------->


#<----------Main window--------------->
main_f = ct.CTkFrame(
    master=s,
    height=722,
    width=950
)
main_f.pack(side=ct.LEFT)
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
    conn =sqlite3.connect(r'files/timetable.db')
    cur=conn.execute(f"SELECT * FROM FACULTY WHERE NAME ='{name}'")
    res=cur.fetchall()
    fid=res[0][1]
    n=res[0][2]
    os.environ['FID']=fid
    os.environ['N']=n
    os.system('python windows\\sing_fac.py')
def std_t():
    os.system('python windows\\timetable_stud.py')
def shed():
    os.system('python windows\\scheduler.py')
def out():
    res=messagebox.askquestion('Warning','Do you really want to logout?', icon='warning')
    if res=="Yes" or "yes":
        s.destroy()
        os.system('python windows\\main\\main.py')
    else:
        pass




s.mainloop()