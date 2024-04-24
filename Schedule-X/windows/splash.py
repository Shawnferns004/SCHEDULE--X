#importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
import os
import sys



w=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


w.overrideredirect(1) 



def new_win():
    os.system('python windows\\main.py')

Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='schedule ', fg='white', bg='#272727')
label1.configure(font=("Game Of Squids", 24, "bold"))   
label2=Label(w, text='X', fg='white', bg='#272727')
label2.configure(font=("Game Of Squids", 70, "bold"))   


label1.place(x=50,y=90)
label2.place(x=295,y=55)

label2=Label(w, text='Loading...', fg='white', bg='#272727')  
label2.configure(font=("Consolas", 11))
label2.place(x=10,y=215)



image_a=ImageTk.PhotoImage(Image.open('windows/images/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('windows/images/c1.png'))




for i in range(2): 
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.3)



w.destroy()
new_win()
w.mainloop()