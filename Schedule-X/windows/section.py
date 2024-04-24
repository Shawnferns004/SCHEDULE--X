import customtkinter as ct 
import os
import tkinter as tk 
from PIL import ImageTk,Image,ImageFilter





def clear():
    sec.destroy()


def it():
    sec.destroy()
    os.system('python windows\scheduler.py')
def comp():
    sec.destroy()
    os.system('python windows\schedule_comp.py')

sec = ct.CTk()
sec.geometry("350x600+900+250")

sec.overrideredirect(1)
bg=Image.open("windows\images\\nav.jpeg")
img = ImageTk.PhotoImage(bg)

f= ct.CTkLabel(
    master=sec,
    width=600,
    height=600,
    # fg_color="",
    image=img,
    # bg="#ffffff"?
    # corner_radius=10
).pack()


it_btn= ct.CTkButton(
master=f,
text="I T",
font=('Consolas', 15, 'bold'),
fg_color="black",
width=200,
height=40,
corner_radius=0,
hover_color="grey",
text_color="orange",
command=lambda: it()
)
it_btn.place(x=80, y=100)

comp_btn= ct.CTkButton(
master=f,
text="C O M P S",
font=('Consolas', 15, 'bold'),
fg_color="black",
width=200,
height=40,
corner_radius=0,
hover_color="grey",
text_color="orange",
command=lambda: comp()
)
comp_btn.place(x=80, y=190)

extc_btn= ct.CTkButton(
master=f,
text="E X T C",
font=('Consolas', 15, 'bold'),
fg_color="black",
width=200,
height=40,
corner_radius=0,
hover_color="grey",
text_color="orange",
# command=lambda: pro()
)
extc_btn.place(x=80, y=280)

mech_btn= ct.CTkButton(
master=f,
text="M E C H",
font=('Consolas', 15, 'bold'),
fg_color="black",
width=200,
height=40,
corner_radius=0,
hover_color="grey",
text_color="orange",
# command=lambda: pro()
)
mech_btn.place(x=80, y=370)

btn_back = ct.CTkButton(
    f,
    text="BACK",
    font=('Consolas', 12, 'bold'),
    command=lambda:clear(),
    width=100,
    height=40,
    fg_color="grey",
    hover=False,
    corner_radius=10
).place(x=130,y=450)

sec.mainloop()







    