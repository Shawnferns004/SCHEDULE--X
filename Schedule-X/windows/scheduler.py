import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import customtkinter as ct
from email.message import EmailMessage
import smtplib
import ssl
import os
import time
import subprocess
from subprocess import call
from PIL import ImageTk,Image,ImageFilter


conn=sqlite3.connect(r"files/timetable.db")
days = 5
periods = 7
recess_break_aft = 4 # recess after 3rd Period
section = None
butt_grid = []
half=2


period_names = list(map(lambda x: 'Period ' + str(x), range(1, 7+1)))
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday']



# Generate the schedule automatically
# generate_schedule()

# Close the database connection


def update_p(d, p, tree, parent):
    # print(section, d, p, str(sub.get()))

    try:
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one subject at a time!")
            parent.destroy()
            return
        row = tree.item(tree.selection()[0])['values']
        if row[0] == 'NULL' and row[1] == 'NULL':
            conn.execute(f"DELETE FROM SCHEDULE WHERE ID='{section+str((d*periods)+p)}'")
            conn.commit()
            update_table()
            parent.destroy()
            return

        conn.commit()
        print(row)
        conn.execute(f"REPLACE INTO SCHEDULE (ID, DAYID, PERIODID, SUBCODE, SECTION, FINI)\
            VALUES ('{section+str((d*periods)+p)}', {d}, {p}, '{row[1]}', '{section}', '{row[0]}')")
        conn.commit()
        update_table()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a subject from the list!")
        parent.destroy()
        return

    parent.destroy()



def process_button(d, p):
    print(d, p)
    add_p = ct.CTk()
    add_p.geometry('400x400')

    # get subject code list from the database
    cursor = conn.execute("SELECT SUBCODE FROM SUBJECTS")
    subcode_li = [row[0] for row in cursor]
    subcode_li.insert(0, 'NULL')

    # Label10
    ct.CTkLabel(
        add_p,
        text='Select Subject',
        font=('Consolas', 12, 'bold')
    ).pack()

    ct.CTkLabel(
        add_p,
        text=f'Day: {day_names[d]}',
        font=('Consolas', 12)
    ).pack()

    ct.CTkLabel(
        add_p,
        text=f'Period: {p+1}',
        font=('Consolas', 12)
    ).pack()

    tree = ttk.Treeview(add_p)
    tree['columns'] = ('one', 'two')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=170, stretch=tk.NO)
    tree.column("two", width=170, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="Faculty")
    tree.heading('two', text="Subject Code")
    tree['height']=8


    dep= "IT"
    
    cursor = conn.execute(f"SELECT FACULTY.INI, FACULTY.SUBCODE1, FACULTY.SUBCODE2, SUBJECTS.SUBNAME\
    FROM FACULTY, SUBJECTS\
    WHERE FACULTY.DEPARTMENT='{dep}' AND FACULTY.SUBCODE1=SUBJECTS.SUBNAME OR FACULTY.SUBCODE2=SUBJECTS.SUBNAME ")
    for row in cursor:
        print(row)
        tree.insert(
            "",
            0,
            values=(row[0],row[-1])
        )
    tree.insert("", 0, value=('NULL', 'NULL'))
    tree.place(x=30,y=100)

    ct.CTkButton(
        add_p,
        text="OK",
        command=lambda x=d, y=p, z=tree, d=add_p: update_p(x, y, z, d)
    ).place(y=320, x=130)

    add_p.mainloop()


def select_sec():
    global section
    section = str(combo1.get())
    print(section)
    update_table()


def update_table():
    for i in range(days):
        for j in range(periods):
            cursor = conn.execute(f"SELECT SUBCODE, FINI FROM SCHEDULE\
                WHERE DAYID={i} AND PERIODID={j} AND SECTION='{section}'")
            cursor = list(cursor)
            print(cursor)
            if len(cursor) != 0:
                butt_grid[i][j]['text'] = str(cursor[0][0]) + '\n' + str(cursor[0][1])
                butt_grid[i][j].update()
                print(i, j, cursor[0][0])
            else:
                butt_grid[i][j]['text'] = "      "
                butt_grid[i][j].update()
            

# connecting database
conn = sqlite3.connect(r'files/timetable.db')

# creating Tabe in the database
conn.execute('CREATE TABLE IF NOT EXISTS SCHEDULE\
(ID CHAR(10) NOT NULL PRIMARY KEY,\
DAYID INT NOT NULL,\
PERIODID INT NOT NULL,\
SUBCODE CHAR(10) NOT NULL,\
SECTION CHAR(5) NOT NULL,\
FINI CHAR(10) NOT NULL)')


# DAYID AND PERIODID ARE ZERO INDEXED

tt= ct.CTk()
width=900
height=650
# x=(tt.winfo_screenwidth()//6)-(-width//2)
# y=(tt.winfo_screenwidth()//6)-(height//5)
tt.geometry("1050x650+630+230")
title_lab = ct.CTkLabel(
        tt,
        text='T  I  M  E  T  A  B  L  E',
        font=('Consolas', 30, 'bold'),
        pady=15,
    )
title_lab.pack()


table = ct.CTkFrame(tt)
table.pack()

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
    # print(b)
        b = []


lbl=ct.CTkLabel(
        master=tt,
        text='Select Class:  ',
        font=('Consolas', 12, 'bold'),
       
    ).place(x=250,y=530)


cursor = conn.execute("SELECT DISTINCT SECTION FROM STUDENT")
fac_li = [row[0] for row in cursor]
# fac_li.reverse()
# print(fac_li)

combo1 = ct.CTkComboBox(
        tt,
        values=fac_li, 
        # variable=option     
    )
combo1.place(x=370,y=530)


b = ct.CTkButton(
        tt,
        text="OK",
        font=('Consolas', 12, 'bold'),
        command=select_sec,
        width=70,
        height=40,
        fg_color="#008DDA",
        corner_radius=10
    )
b.place(x=530,y=523)
b.invoke()
    
print(butt_grid[0][1], butt_grid[1][1])
update_table()

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
c.place(x=630,y=523)

d = ct.CTkButton(
        tt,
        text="GENERATE",
        font=('Consolas', 12, 'bold'),
        command=lambda:generate_schedule(),
        width=70,
        height=40,
        fg_color="#65B741",
        hover=False,
        corner_radius=10
    )
d.place(x=400,y=580)

e = ct.CTkButton(
        tt,
        text="SEMD EMAIL",
        font=('Consolas', 12, 'bold'),
        command=lambda:send_mail(),
        width=70,
        height=40,
        fg_color="#FE7A36",
        hover=False,
        corner_radius=10
    )
e.place(x=500,y=580)

 
def clear():
        tt.destroy()
tt.overrideredirect(1)



import random

def generate_schedule():
    global conn

    # Define the sections
    sections = combo1.get()  # Example sections

    for sec in sections:
        for day in range(days):
            for period in range(periods):
                # Get a random subject code from the database
                cursor = conn.execute("SELECT SUBNAME FROM SUBJECTS WHERE DEPARTMENT='IT' ORDER BY RANDOM() LIMIT 1")
                subcode = cursor.fetchone()[0]

                cur = conn.execute(f"SELECT * FROM FACULTY WHERE SUBCODE1='{subcode}' OR SUBCODE2='{subcode}'")
                res = cur.fetchall()
                if res:
                     ini = res[0][3]

                # Insert the schedule into the database
                conn.execute(f"REPLACE INTO SCHEDULE (ID, DAYID, PERIODID, SUBCODE, SECTION, FINI) \
                              VALUES ('{sec}{day * periods + period}', {day}, {period}, '{subcode}', '{sec}', '{ini}')")
                conn.commit()

    # Notify that the schedule has been generated
    messagebox.showinfo("Schedule Generated", "The schedule has been successfully generated.")
    tt.destroy()
    call(["python", "windows\\scheduler.py"])









    

def send_mail():
    con = sqlite3.connect(r'files/timetable.db')
    cur = con.cursor()

    cur.execute("SELECT EMAIL FROM STUDENT")
    rows = cur.fetchall()
    email_receiver = [row[0] for row in rows]

    email_sender = 'shawnferns004@gmail.com'
    email_pass = "ynht dozr gjvj xqzu"

    subject = "Time table update"

    html_body = """
    <html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 0;
      }
      .container {
        max-width: 600px;
        margin: 20px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      }
      h1 {
        color: #007bff;
        text-align: center;
      }
      p {
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 10px;
      }
      .button {
        display: inline-block;
        background-color: #007bff;
        color: black;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        margin-top: 20px;
      }
      .button:hover {
        background-color: #0056b3;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Time Table Update Notification</h1>
      <p>Hello Students!</p>
      <p>We are excited to inform you that the time table has been updated. Please review the changes and plan accordingly.</p>
      <p>If you have any questions or concerns, feel free to contact us.</p>
      <p>Best regards,<br>SFIT</p>
      <a href="https://sfiterp.sfit.co.in:98/" class="button">View Time Table</a>
    </div>
  </body>
</html>

    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content("This email client does not support HTML content. Please upgrade to a modern email client to view this message.", subtype='plain')
    em.add_alternative(html_body, subtype='html')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_pass)
        smtp.send_message(em)
        print("Email sent successfully")



tt.mainloop()