import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ct
import sqlite3
import os

ct.set_default_color_theme("green")
ct.set_appearance_mode("dark")
days = 5
periods = 6
half = 2 #small break after 2nd period
recess_break_aft = 4 # recess after 3rd Period
fini = None
butt_grid = []


period_names = list(map(lambda x: 'Period ' + str(x), range(1, 6+1)))
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday']


def select_fac():
    global fini
    fini = str(combo1.get())
    print(fini)
    update_table(fini)



def update_table(fini):
    for i in range(days):
        for j in range(periods):
            cursor = conn.execute(f"SELECT SECTION, SUBCODE FROM SCHEDULE\
                WHERE DAYID={i} AND PERIODID={j} AND FINI='{fini}'")
            cursor = list(cursor)
            print(cursor)
            
            butt_grid[i][j]['bg'] = '#FBF6EE'  #subjects color
            if len(cursor) != 0:
                subname = cursor[0][1]
                cur1 = conn.execute(F"SELECT SUBTYPE FROM SUBJECTS WHERE SUBNAME='{subname}'")
                cur1 = list(cur1)
                subtype = cur1[0][0]
                butt_grid[i][j]['fg'] = 'white'
                if subtype == 'T':
                    butt_grid[i][j]['bg'] = '#008DDA'
                elif subtype == 'P':
                    butt_grid[i][j]['bg'] = '#65B741'

                sec_li = [x[0] for x in cursor]
                t = ', '.join(sec_li)
                butt_grid[i][j]['text'] = "Sections: " + t
                print(i, j, cursor[0][0])
            else:
                butt_grid[i][j]['fg'] = 'black'   ##text color of the subjects
                butt_grid[i][j]['text'] = "No Class"
                butt_grid[i][j].update()

def process_button(d, p):
    print(d, p, fini)
    det = ct.CTk()
    width=300
    height=350
    x=(det.winfo_screenwidth()//4)-(-width//2)
    y=(det.winfo_screenwidth()//4)-(height//2)
    
    det.geometry(f"{width}x{height}+{x}+{y}")
    details = ct.CTkFrame(master=det, width=900,height=50,border_width=3,corner_radius=15,fg_color="#A7D7C5")
    details.place(relx=0.5 ,rely=0.5, anchor=ct.CENTER)
    
    cursor = conn.execute(f"SELECT SECTION, SUBCODE FROM SCHEDULE\
                WHERE DAYID={d} AND PERIODID={p} AND FINI='{fini}'")
    cursor = list(cursor)
    print("section", cursor)
    if len(cursor) != 0:
        sec_li = [x[0] for x in cursor]
        t = ', '.join(sec_li)
        subcode = cursor[0][1]
        cur1 = conn.execute(f"SELECT SUBNAME, SUBTYPE,SUBCODE FROM SUBJECTS\
            WHERE SUBNAME='{subcode}'")
        cur1 = list(cur1)
        subname = str(cur1[0][0])
        subtype = str(cur1[0][1])
        subcode = str(cur1[0][1])

        if subtype == 'T':
            subtype = 'Theory'
        elif subtype == 'P':
            subtype = 'Practical'

    #     print(subcode, fini, subname, subtype, fname, femail)
    else:
        sec_li = subcode = subname = subtype = t = 'None'

    ct.CTkLabel(details, text='Class Details', font=('Consolas', 15, 'bold'),text_color="black").pack(pady=15)
    ct.CTkLabel(details, text='Day: '+day_names[d], font=('Consolas', 15, 'bold'),text_color="black", anchor="w").pack(expand=1, fill=tk.X, padx=20)
    ct.CTkLabel(details, text='Period: '+str(p+1), font=('Consolas', 15, 'bold'),text_color="black", anchor="w").pack(expand=1, fill=tk.X, padx=20)
    ct.CTkLabel(details, text='Subject Code: '+subcode, font=('Consolas', 15, 'bold'),text_color="black", anchor="w").pack(expand=1, fill=tk.X, padx=20)
    ct.CTkLabel(details, text='Subect Name: '+subname, font=('Consolas', 15, 'bold'),text_color="black", anchor="w").pack(expand=1, fill=tk.X, padx=20)
    ct.CTkLabel(details, text='Subject Type: '+subtype, font=('Consolas', 15, 'bold'),text_color="black", anchor="w").pack(expand=1, fill=tk.X, padx=20)
    ct.CTkLabel(details, text='Faculty Initials: '+fini, font=('Consolas', 15, 'bold'),text_color="black", anchor="w").pack(expand=1, fill=tk.X, padx=20)
    ct.CTkLabel(details, text='Sections: '+t, font=('Consolas', 15, 'bold'),text_color="black", anchor="w").pack(expand=1, fill=tk.X, padx=20)

    ct.CTkButton(
        details,
        text="OK",
        font=('Consolas', 15, 'bold'),
        width=70,
        command=det.destroy
    ).pack(side=ct.BOTTOM,pady=10)

    det.mainloop()


def fac_tt_frame(tt, f):
    title_lab = ct.CTkLabel(
        tt,
        text='T  I  M  E  T  A  B  L  E',
        font=('Consolas', 30, 'bold'),
        pady=15,
    )
    title_lab.pack()

    legend_f = ct.CTkFrame(tt)
    legend_f.pack(pady=15)
    ct.CTkLabel(
        tt,
        text='Type: ',
        font=('Consolas', 18, 'bold'),
    ).place(x=200,y=88)

    theory_lbl = ct.CTkLabel(
        legend_f,
        text='Theory Classes',
        fg_color='#008DDA',
        font=('Consolas', 19, 'italic'),
        height=35,
        width=100,
        corner_radius=10,
        text_color='white'
    ).pack(side=tk.LEFT, padx=10)

    prac_lbl = ct.CTkLabel(
        legend_f,
        text='Practical Classes',
        fg_color='#65B741',
        font=('Consolas', 19, 'italic'),
        height=35,
        width=100,
        corner_radius=10
    ).pack(side=tk.LEFT, padx=10)

    global butt_grid
    global fini
    fini = f

    table = ct.CTkFrame(tt,height=100)
    table.pack()


    lb1=ct.CTkLabel(
        master=tt,
        text="9:00 - 10:00",
        height=1,
        fg_color="#f1f0f1",
        text_color="black"
    ).place(x=130,y=174)
    lb2=ct.CTkLabel(
        master=tt,
        text="10:00 - 11:00",
        height=1,
        fg_color="#f1f0f1",
        text_color="black"
    ).place(x=245,y=174)
    lb3=ct.CTkLabel(
        master=tt,
        text="11:15 - 12:15",
        height=1,
        fg_color="#f1f0f1",
        text_color="black"
    ).place(x=395,y=174)
    lb4=ct.CTkLabel(
        master=tt,
        text="1:00 - 2:00",
        height=1,
        fg_color="#f1f0f1",
        text_color="black"
    ).place(x=555,y=174)
    lb5=ct.CTkLabel(
        master=tt,
        text="2:00 - 3:00",
        height=1,
        fg_color="#f1f0f1",
        text_color="black"
    ).place(x=675,y=174)
    lb6=ct.CTkLabel(
        master=tt,
        text="4:00 - 5:00",
        height=1,
        fg_color="#f1f0f1",
        text_color="black"
    ).place(x=795,y=174)

    first_half = ct.CTkFrame(table)
    first_half.pack(side='left')

    recess_frame = ct.CTkFrame(table,fg_color="#FFB534",width=30,height=367,corner_radius=0)
    recess_frame.pack(side='left')


    mid = ct.CTkFrame(table)
    mid.pack(side='left')

    second_half = ct.CTkFrame(table)
    second_half.pack(side='left')
    mid_half_frame = ct.CTkFrame(table,fg_color="#FFB534",width=30,height=367,corner_radius=0,)
    mid_half_frame.pack(side="left" ,after=mid)
    
    recess = ct.CTkLabel(
        recess_frame,
        text='R\n\nE\n\nC\n\nE\n\nS\n\nS',
        font=('Consolas', 18, 'italic'),
        width=30,
        height=405,
        text_color="black"
    )
    recess.pack()

    half_rec = ct.CTkLabel(
        mid_half_frame,
        text='R\n\nE\n\nC\n\nE\n\nS\n\nS',
        font=('Consolas', 18, 'italic'),
        width=30,
        height=405,
        text_color="black"
    )
    half_rec.pack()

    for i in range(days):
        b = tk.Label(
            first_half,
            text=day_names[i],
            font=('Consolas', 12, 'bold'),
            width=9,
            height=2,
            bd=1,
            relief='solid',
        )
        b.grid(row=i+1, column=0,sticky="news")

    for i in range(periods,):
        if i < half :
            b = tk.Label(first_half)
            b.grid(row=0, column=i+1,sticky="news")
        elif i<recess_break_aft:
            b = tk.Label(mid)
            b.grid(row=0, column=i,sticky="news")
        else:
            b = tk.Label(second_half)
            b.grid(row=0, column=i,sticky="news")

        b.config(
            text=period_names[i],
            font=('Consolas', 12, 'bold'),
            width=9,
            height=3,
            bd=1,
            relief='solid'
        )


    for i in range(days):
        b = []
        for j in range(periods):
            if j<half:
                bb = tk.Button(first_half)
                bb.grid(row=i+1, column=j+1,sticky="news")
            elif j<recess_break_aft:
                bb = tk.Button(mid)
                bb.grid(row=i+1, column=j,sticky="news")
            else:
                bb = tk.Button(second_half)
                bb.grid(row=i+1, column=j,sticky="news")

           
            bb.config(
                text='Hello World!',
                font=('Consolas', 10),
                width=16,
                height=4,
                bd=1,
                relief='solid',
                wraplength=80,
                justify='center',
                command=lambda x=i, y=j: process_button(x, y)
            )
            b.append(bb)

        butt_grid.append(b)
        #print(b)
        b = []

    print(butt_grid[0][1], butt_grid[1][1])
    update_table(fini)
        

    for i in range(days):
        b=[]
        for j in range(periods):
            if j==1:
                b=tk.Button(
                    first_half, 
                    text='Hello World!',
                    font=('Consolas', 10),
                    width=16,
                    height=4,
                    bd=1,
                    relief='solid',
                    wraplength=80,
                    justify='center',
                    command=lambda x=i, y=j: process_button(x, y)
                )


conn = sqlite3.connect(r'files/timetable.db')
if __name__ == "__main__":
    
    tt = ct.CTk()
    width=900
    tt.overrideredirect(1)
    height=650
    x=(tt.winfo_screenwidth()//6)-(-width//2)
    # y=(tt.winfo_screenwidth()//6)-(height//5)
    tt.geometry("900x650+770+230")
    # tt.overrideredirect(1)
    tt.title('Faculty Timetable')
    fac_tt_frame(tt, fini)

 

    lbl=ct.CTkLabel(
        master=tt,
        text='Select Faculty:  ',
        font=('Consolas', 12, 'bold'),
       
    ).place(x=300,y=570)

    cursor = conn.execute("SELECT DISTINCT INI FROM FACULTY")
    fac_li = [row[0] for row in cursor]
    print(fac_li)
    optionmenu_var = ct.StringVar(value="Select")
    combo1 = ct.CTkComboBox(
        tt,
        values=fac_li,
        variable=optionmenu_var,
        
    )
    combo1.place(x=420,y=570)


    b = ct.CTkButton(
        tt,
        text="OK",
        font=('Consolas', 12, 'bold'),
        command=select_fac,
        width=70,
        height=40,
        corner_radius=10
    )
    b.place(x=570,y=563)
    b.invoke()
    

    c = ct.CTkButton(
        tt,
        text="BACK",
        font=('Consolas', 12, 'bold'),
        command=lambda:clear(),
        width=70,
        height=40,
        fg_color="grey",
        hover=False,
        corner_radius=10
    )
    c.place(x=650,y=563)

 
    def clear():
        tt.destroy()

        
    tt.mainloop()