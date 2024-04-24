import tkinter 
import customtkinter
from tkinter import ttk
from tkinter import messagebox
import os
import sys
import sqlite3
from PIL import ImageTk,Image,ImageFilter

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")


def challenge():
    conn = sqlite3.connect(r'files/timetable.db')

    user = str(combobox.get())
    if user == "Student":
        
        cursor = conn.execute(f"SELECT PASSW, NAME,SID FROM STUDENT WHERE SID='{name_entry.get()}' and PASSW='{pass_entry.get()}'")
        result=cursor.fetchone()
        if result:
                messagebox.showinfo('Success','Logged in successfully')
                name = name_entry.get()

                os.environ['NAME_DATA']= name
                m.destroy()
                os.system(f'python windows\\stud.py')
                
        else:
            messagebox.showerror('Error','Invalid username or password')

    elif user == "Faculty":
        cursor = conn.execute(f"SELECT PASSW, INI, NAME, EMAIL, DEPARTMENT FROM FACULTY WHERE FID='{name_entry.get()}'")
        result=cursor.fetchall()
        dep = result[0][4]
        name = result[0][2]
        if result:
            messagebox.showinfo('Success','Logged in successfully')
            os.environ['NAME']=name
            m.destroy()
            os.system('python windows\\tech.py') 
        else:
            messagebox.showerror('Error','Invalid username or password')
    elif user == "Admin":
        if  name_entry.get() == 'admin' and pass_entry.get() == 'admin':
            m.destroy()
            os.system('python windows\\admin.py')
            uname=name_entry.get()
        else:
            messagebox.showerror('Bad Input', 'Incorret Username/Password!')
            

m = customtkinter.CTk()
m.title("ScheduleX")
m.iconbitmap("windows/images/favicon.ico")
width=730
height=600
x=(m.winfo_screenwidth()//7)-(-width//2)
y=(m.winfo_screenwidth()//4)-(height//2)
m.geometry(f"{width}x{height}+{x}+{y}")


bg=Image.open("windows\images\wall.jpeg")
img = ImageTk.PhotoImage(bg)
l1=customtkinter.CTkLabel(master=m ,image=img)
l1.pack()



frame = customtkinter.CTkFrame(master=l1, width=600,height=500,border_width=3,corner_radius=15)
frame.place(relx=0.5 ,rely=0.5, anchor=tkinter.CENTER)


lbl = customtkinter.CTkLabel(
    frame,
    text="Schedule",
    font=('Game of Squids',30,'bold')
).place(x=150,y=40)
lb2 = customtkinter.CTkLabel(
    frame,
    text="X",
    font=('Game of Squids',75,'bold')
).place(x=375,y=8)


l2=customtkinter.CTkLabel(master=frame,text="Login into your account", font=('Poppins',20))
l2.place(x=165,y=120)

name_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username",width=350,height=40,border_width=2,
corner_radius=10 )
name=str(name_entry.get())
name_entry.place(x=117,y=230)


pass_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*",width=350,height=40,border_width=2,
corner_radius=10 )
pass_entry.place(x=117,y=300)

l2=customtkinter.CTkButton(master=frame,text="Fogort Password ?", font=('Poppins',14),border_width=0,fg_color="transparent",hover=False,command=lambda:fogort())
l2.place(x=342,y=350)

optionmenu_var = customtkinter.StringVar(value="Select  User")
combobox = customtkinter.CTkComboBox(master=frame,values=["Student","Faculty","Admin"],variable=optionmenu_var,corner_radius=10,width=350,height=40)
combobox.place(x=117,y=160)

btn = customtkinter.CTkButton(master=frame, text="LOGIN", command=challenge, height=40,corner_radius=10)
btn.place(relx=0.5,rely=0.87,anchor=tkinter.CENTER)


def fogort():
   m.destroy()
   os.system('python windows\\forget.py')





m.mainloop()