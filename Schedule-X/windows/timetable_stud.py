import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import customtkinter as ct

days = 5
periods = 7
half=2
recess_break_aft = 4 # recess after 3rd Period
section = None
butt_grid = []


period_names = list(map(lambda x: 'Period ' + str(x), range(1, 8)))
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday']



def select_sec():
    global section
    section = str(combo1.get())
    print(section)
    update_table(section)



def update_table(sec):
    for i in range(days):
        for j in range(periods):
            cursor = conn.execute(f"SELECT SUBCODE, FINI FROM SCHEDULE\
                WHERE DAYID={i} AND PERIODID={j} AND SECTION='{sec}'")
            cursor = list(cursor)

            butt_grid[i][j]['bg'] = 'white'
            if len(cursor) != 0:
                subname = cursor[0][0]
                cur1 = conn.execute(F"SELECT SUBTYPE FROM SUBJECTS WHERE SUBNAME='{subname}'")
                cur1 = list(cur1)
                subtype = cur1[0][0]
                butt_grid[i][j]['fg'] = 'white'
                if subtype == 'T':
                    butt_grid[i][j]['bg'] = '#008DDA'
                elif subtype == 'P':
                    butt_grid[i][j]['bg'] = '#65B741'

                butt_grid[i][j]['text'] = str(cursor[0][0]) + '\n' + str(cursor[0][1])
                butt_grid[i][j].update()
                print(i, j, cursor[0][0])
            else:
                butt_grid[i][j]['fg'] = 'black'
                butt_grid[i][j]['text'] = "   "
                butt_grid[i][j].update()



def process_button(d, p, sec):
    details = tk.Tk()
    cursor = conn.execute(f"SELECT * FROM SCHEDULE\
                WHERE ID='{section+str((d*periods)+p)}'")
    res=cursor.fetchall()
    if cursor != 0:
        subcode = str(res[0][3]) 
        fini =  str(res[0][5])

        cur1 = conn.execute(f"SELECT * FROM SUBJECTS\
            WHERE SUBNAME='{subcode}'")
        r=cur1.fetchall()
        subname = str(r[0][1])
        subtype = str(r[0][2])

        cur2 = conn.execute(f"SELECT NAME, EMAIL FROM FACULTY\
            WHERE INI='{fini}'")
        cur2 = list(cur2)
        fname = str(cur2[0][0])
        femail = str(cur2[0][1]) 

        if subtype == 'T':
            subtype = 'Theory'
        elif subtype == 'P':
            subtype = 'Practical'

    else:
        subcode = fini = subname = subtype = fname = femail = 'None'

    print(subcode, fini, subname, subtype, fname, femail)
    tk.Label(details, text='Class Details', font=('Consolas', 15, 'bold')).pack(pady=15)
    tk.Label(details, text='Day: '+day_names[d], font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Period: '+str(p+1), font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subject Code: '+subcode, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subect Name: '+subname, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subject Type: '+subtype, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Initials: '+fini, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Name: '+fname, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Email: '+femail, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)

    tk.Button(
        details,
        text="OK",
        font=('Consolas'),
        width=10,
        command=details.destroy
    ).pack(pady=10)

    details.mainloop()



def student_tt_frame(tt, sec):
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
    global section
    section = sec

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
                command=lambda x=i, y=j, z=sec: process_button(x, y, z)
            )
            b.append(bb)

        butt_grid.append(b)
        # print(b)
        b = []

    print(butt_grid[0][1], butt_grid[1][1])
    update_table(sec)



conn = sqlite3.connect(r'files/timetable.db')
if __name__ == "__main__":
    
    tt = ct.CTk()
    width=900
    tt.overrideredirect(1)
    height=650
    # x=(tt.winfo_screenwidth()//6)-(-width//2)
    # y=(tt.winfo_screenwidth()//6)-(height//5)
    tt.geometry("1050x650+630+230")
    # tt.overrideredirect(1)
    tt.title('Faculty Timetable')
    student_tt_frame(tt, section)

 

    lbl=ct.CTkLabel(
        master=tt,
        text='Select Faculty:  ',
        font=('Consolas', 12, 'bold'),
       
    ).place(x=300,y=570)

    cursor = conn.execute("SELECT DISTINCT SECTION FROM STUDENT")
    fac_li = [row[0] for row in cursor]
    print(fac_li)
    fac_li.reverse()
    # optionmenu_var = ct.StringVar(value="Select")
    combo1 = ct.CTkComboBox(
        tt,
        values=fac_li,
        # variable=optionmenu_var,
        
    )
    combo1.place(x=420,y=570)


    b = ct.CTkButton(
        tt,
        text="OK",
        font=('Consolas', 12, 'bold'),
        command=select_sec,
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