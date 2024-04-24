import customtkinter as ct
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
import sqlite3
import sys
import os

con = sqlite3.connect(r'files/timetable.db')


name = os.environ.get('NAME_DATA')
# cur=con.execute(f"SELECT * FROM STUDENT WHERE SID='{name}'")
# res= cur.fetchall()
# std_name= res[0][2]
# roll = res[0][3]
# sec = res[0][4]
# email = res[0][5]
# batch = res[0][6]
# branch = res[0][7]









s = ct.CTk()

# <-----------frame settings-------------->
width = 1200
height = 800
x = (s.winfo_screenwidth() // 24) - (-width // 3)
y = (s.winfo_screenwidth() // 4) - (height // 2)
s.geometry(f"{width}x{height}+{x}+{y}")

# <-------------xxxxx------------------->

# <-----------Navbar------------>
nav = ct.CTkFrame(master=s, height=780, width=230)
nav.pack(side=ct.LEFT, padx=7)

# <-----------xxxx------------->

# <----------Main window--------------->
main_f = ct.CTkFrame(master=s, height=780, width=950)
main_f.pack(side=ct.LEFT)
main_f.propagate(False)

# <--------xxxxx---------------------->

# <------------logo-------------->
lbl = ct.CTkLabel(
    nav,
    text="Schedule",
    font=('Game of Squids', 20, 'bold')
)
lbl.place(x=12, y=15)
lb2 = ct.CTkLabel(
    nav,
    text="X",
    font=('Game of Squids', 45, 'bold')
)
lb2.place(x=160, y=1)

# <-------------buttons--------------->
# profile btn
profile_btn = ct.CTkButton(
    master=nav,
    text="Profile",
    font=('Consolas', 15, 'bold'),
    fg_color="black",
    width=200,
    height=40,
    corner_radius=0,
    hover_color="grey",
    text_color="orange",
    command=lambda: pro()
)
profile_btn.place(x=12, y=100)


# timetable btn
time_table = ct.CTkButton(
    master=nav,
    text='Time-Table',
    font=('Consolas', 15, 'bold'),
    fg_color="black",
    width=200,
    height=40,
    hover_color="grey",
    text_color="orange",
    corner_radius=0,
    command=lambda: tt()
)
time_table.place(x=12, y=150)

# pass btn
change_pass_btn = ct.CTkButton(
    master=nav,
    text='Change Password',
    font=('Consolas', 15, 'bold'),
    fg_color="black",
    width=200,
    text_color="orange",
    height=40,
    hover_color="grey",
    corner_radius=0,
    command=lambda: change_pass_window()
)
change_pass_btn.place(x=12, y=200)

# logout btn
image = ct.CTkImage(Image.open('windows/images/log.png'))
log_out = ct.CTkButton(
    master=nav,
    text='LOG OUT',
    font=('Consolas', 15, 'bold'),
    fg_color="black",
    width=200,
    image=image,
    height=40,
    corner_radius=0,
    hover_color="grey",
    command=lambda: logout()
)
log_out.place(x=12, y=730)


# <-------------xxxxxxxx------------>


# <-------indicator------------>
pro_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
)
pro_indi.place(x=8, y=100)

pass_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
)
pass_indi.place(x=8, y=150)

tt_indi = ct.CTkLabel(
    master=nav,
    text="",
    bg_color="grey",
    width=5,
    height=40
)
tt_indi.place(x=8, y=200)
# <----------xxxx--------------->


# <--------on clicks --------->
def tt():
    pid = os.environ.get('NAME_DATA')
    cur=con.execute(f"SELECT * FROM STUDENT WHERE SID='{pid}'")
    res= cur.fetchall()
    name= res[0][2]
    roll = str(res[0][3])
    sec = res[0][4]
    email = res[0][5]
    batch = res[0][6]
    branch = res[0][7]
    os.environ['PID']= pid
    os.environ['NAME']= name
    os.environ['ROLL_DATA']= roll
    os.environ['SEC']= sec
    os.environ['EMAIL']= email
    os.environ['BATCH']= batch
    os.environ['BRANCH']= branch

    if branch=="IT":
        os.system('python windows\\sing_stud.py')
    elif branch=="COMPS":
        os.system('python windows\\sing_std_comp.py')


def pro():
    con = sqlite3.connect(r'files/timetable.db')


    pid = os.environ.get('NAME_DATA')
    cur=con.execute(f"SELECT * FROM STUDENT WHERE SID='{pid}'")
    res= cur.fetchall()
    name= res[0][2]
    roll = str(res[0][3])
    sec = res[0][4]
    email = res[0][5]
    batch = res[0][6]
    branch = res[0][7]
    os.environ['PID']= pid
    os.environ['NAME']= name
    os.environ['ROLL_DATA']= roll
    os.environ['SEC']= sec
    os.environ['EMAIL']= email
    os.environ['BATCH']= batch
    os.environ['BRANCH']= branch
    os.system('python windows\\profile.py')


def logout():
    res = messagebox.askquestion('Warning', 'Do you really want to logout?', icon='warning')
    if res == "Yes" or res == "yes":
        s.destroy()
        os.system('python windows\\main.py')
    else:
        pass


def change_pass_window():
    det = ct.CTk()
    width = 700
    height = 400
    x = (det.winfo_screenwidth() // 4) - (-width // 2)
    y = (det.winfo_screenwidth() // 4) - (height // 2)
    det.grab_set()
    det.focus_force()
    det.overrideredirect(1)

    det.geometry(f"{width}x{height}+{x}+{y}")
    f = ct.CTkFrame(master=det, width=680, height=370)
    f.place(relx=0.5, rely=0.5, anchor=ct.CENTER)

    lb = ct.CTkLabel(
        f,
        text="CHANGE PASSWORD",
        font=('Consolas', 28, 'bold')
    )
    lb.place(x=240, y=20)

    pid_t = ct.CTkEntry(
        f,
        placeholder_text="PID...",
        height=40,
        width=400,
        corner_radius=40
    )
    pid_t.place(x=140, y=100)

    old_p = ct.CTkEntry(
        f,
        placeholder_text="Old Password...",
        height=40,
        width=400,
        corner_radius=40
    )
    old_p.place(x=140, y=170)

    new_p = ct.CTkEntry(
        f,
        placeholder_text="New Password...",
        height=40,
        width=400,
        corner_radius=40
    )
    new_p.place(x=140, y=240)

    back = ct.CTkButton(
        f,
        text="Back",
        font=("consolas", 15, 'bold'),
        hover=False,
        fg_color="black",
        height=40,
        width=60,
        command=lambda: det.destroy()
    )
    back.place(x=260, y=300)

    change_pass = ct.CTkButton(
        f,
        text="Change",
        font=("consolas", 15, 'bold'),
        hover=False,
        fg_color="#388E3C",
        height=37,
        width=60,
        command=lambda: change()
    )
    change_pass.place(x=340, y=300)

    def change():
        cursor = con.execute(f"SELECT SID, PASSW FROM STUDENT WHERE SID='{pid_t.get()}' AND PASSW='{old_p.get()}'")
        result = cursor.fetchone()

        if result is None:
            messagebox.showerror('Error', 'Invalid pid or password')
        else:
            con.execute(f"UPDATE STUDENT SET PASSW=? WHERE SID=?", (new_p.get(), pid_t.get()))
            con.commit()
            messagebox.showinfo('Success', 'Password changed successfully')
            det.destroy()

    det.mainloop()


s.mainloop()
