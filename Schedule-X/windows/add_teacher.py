import customtkinter as ct 
import tkinter as tk 
import os
import sqlite3
from tkinter import ttk
from tkinter import messagebox



con = sqlite3.connect(r'files/timetable.db')
con.execute('CREATE TABLE IF NOT EXISTS FACULTY\
    (FID INT(10) NOT NULL PRIMARY KEY,\
    PASSW CHAR(50) NOT NULL,\
    NAME CHAR(50) NOT NULL,\
    INI CHAR(5) NOT NULL,\
    EMAIL CHAR(50) NOT NULL,\
    SUBCODE1 CHAR(10) NOT NULL,\
    SUBCODE2 CHAR(10) NOT NULL,\
    ROLE VARCHAR(40) NOT NULL,\
    DEPARTMENT CHAR(50))' )

def create_treeview():
    tree['columns'] = list(map(lambda x: '#' + str(x), range(1, 7)))
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("#1", width=50, stretch=tk.NO)
    tree.column("#2", width=150, stretch=tk.NO)
    tree.column("#3", width=150, stretch=tk.NO)
    tree.column("#4", width=80, stretch=tk.NO)
    tree.column("#5", width=80, stretch=tk.NO)
    tree.column("#6", width=60, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('#1', text="fid")
    tree.heading('#2', text="Name")
    tree.heading('#3', text="Email")
    tree.heading('#4', text="Subject 1")
    tree.heading('#5', text="Subject 2")
    tree.heading('#6', text="Role")
    tree['height'] = 19
    tree.tag_configure('gray',background="lightgray")
    tree.tag_configure('normal',background="white")

def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a Teacher from the list first!")
        return
    for i in tree.selection():
        # print(tree.item(i)['values'][0])
        con.execute(f"DELETE FROM FACULTY WHERE FID = '{tree.item(i)['values'][0]}'")
        con.commit()
        tree.delete(i)
        update_treeview()



def update_treeview():
    m_tag='normal'
    for row in tree.get_children():
        tree.delete(row)
    cursor = con.execute("SELECT FID, NAME, EMAIL ,SUBCODE1 ,SUBCODE2, ROLE, DEPARTMENT FROM FACULTY")
    for row in cursor:
        if m_tag == 'gray':
            m_tag='normal'
        else:
            m_tag='gray'

        tree.insert(
            "",
            'end', iid=row[0],text=row[0],
            values=(row[0], row[1], row[2], row[3],row[4],row[5]),tags=(m_tag)
        )
    tree.place(x=475, y=230)


def parse_data():
    pid = str(lbl1.get())
    name = str(lbl2.get())
    email = str(lbl3.get())
    passw = str(lbl4.get())
    ini = str(lbl6.get())
    dep= str(lbl5.get())
    sub1 = str(combobox1.get())
    sub2 = str(combobox2.get())
    role = str(combobox3.get())

    if pid == "" or name == "" or \
        lbl5.get()== "" or email == "" or \
        role == "" or role == "":
        messagebox.showwarning("Bad Input", "Some fields are empty! Please fill them out!")
        return
  
    con.execute(f"REPLACE INTO FACULTY (FID, PASSW, NAME, INI, EMAIL, SUBCODE1, SUBCODE2, ROLE, DEPARTMENT)\
        VALUES ('{pid}','{passw}','{name}', '{ini}', '{email}','{sub1}','{sub2}','{role}','{dep}')")
    con.commit()
    update_treeview()
    
    lbl1.delete(0, ct.END)
    lbl2.delete(0, tk.END)
    lbl3.delete(0, tk.END)
    lbl4.delete(0, tk.END)
    lbl5.set('Select Deparment')
    lbl6.delete(0, tk.END)
    combobox1.set('Select Subject')
    combobox2.set('Select Subject')
    combobox3.set('Select Role')
    
def update_data():
    lbl1.delete(0, tk.END)
    lbl2.delete(0, tk.END)
    lbl3.delete(0, tk.END)
    lbl4.delete(0, tk.END)
    lbl6.delete(0, tk.END)
    lbl5.set('Select Department')
    combobox1.set('Select Department')
    combobox2.set('Select Batch')
    combobox3.set('Select Class')
    try:
        # print(tree.selection())
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one Teacher at a time to update!")
            return

        q_fid = tree.item(tree.selection()[0])['values'][0]
        cursor = con.execute(f"SELECT * FROM FACULTY WHERE FID = '{q_fid}'")

        cursor = list(cursor)
        lbl1.insert(0, cursor[0][0])
        lbl2.insert(0, cursor[0][2])
        lbl3.insert(0, cursor[0][4])
        lbl4.insert(0, cursor[0][1])
        lbl5.set(cursor[0][8])
        lbl6.insert(0, cursor[0][3])
        combobox1.set(cursor[0][5])
        combobox2.set(cursor[0][6])
        combobox3.set(cursor[0][7])
        
        con.execute(f"DELETE FROM FACULTY WHERE FID = '{cursor[0][0]}'")
        con.commit()
        update_treeview()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a Teacher from the list first!")
        return



passw = ct.CTk()
width = 1100
height = 750
# x=(passw.winfo_screenwidth()//24)-(-width//3)
# y=(passw.winfo_screenwidth()//4)-(height//2)
passw.geometry(f"{width}x{height}+{630}+{200}")
passw.overrideredirect(1)

f = ct.CTkFrame(
    master=passw,
    height=800,
    width=1100
).pack()

header = ct.CTkLabel(
    master=f,
    text="Add / Update Teachers",
    font=("Consolas",40,"bold"),
    fg_color="transparent",
    bg_color="#2a2b2a"
)
header.place(x=30,y=20)

lbl1 = ct.CTkEntry(
    master=f,
    placeholder_text="Enter Teacher PID....",
    corner_radius=10,
    width=400,
    height=40
)
lbl1.place(x=30,y=150)

lbl2 = ct.CTkEntry(
    master=f,
    placeholder_text="Enter Teacher Name....",
    corner_radius=10,
    width=400,
    height=40
)
lbl2.place(x=30,y=210)

lbl3 = ct.CTkEntry(
    master=f,
    placeholder_text="Enter Teacher Email....",
    corner_radius=10,
    width=400,
    height=40
)
lbl3.place(x=30,y=270)

lbl4 = ct.CTkEntry(
    master=f,
    placeholder_text="Enter Password....",
    corner_radius=10,
    width=400,
    height=40,
    show="*"
)
lbl4.place(x=30,y=390)

v = ct.StringVar(value=(f"Select Department..... "))
lbl5 = ct.CTkComboBox(
    master=f,
    values=["IT","COMPS","EXTC","MECH","ELEC"],
    variable=v,
    corner_radius=10,
    width=400,
    height=40,
)
lbl5.place(x=30,y=450)

lbl6 = ct.CTkEntry(
    master=f,
    placeholder_text="Enter Teacher Initials....",
    corner_radius=10,
    width=400,
    height=40,
)
lbl6.place(x=30,y=330)

cursor = con.execute("SELECT SUBNAME FROM SUBJECTS")
subcode_li = [row[0] for row in cursor]
subcode_li.insert(0, 'NULL')

v = ct.StringVar(value=(f"Select Subject "))
combobox1 = ct.CTkComboBox(
    master=f,
    values=subcode_li,
    variable=v,
    corner_radius=10,
    width=400,
    height=40,
)
combobox1.place(x=30,y=510)



var = ct.StringVar(value="Select Subject")
combobox2 = ct.CTkComboBox(
    master=f,
    values=subcode_li,
    variable=var,
    corner_radius=10,
    width=400,
    height=40
)
combobox2.place(x=30,y=570)

optionmenu_var = ct.StringVar(value="Select Role")
combobox3 = ct.CTkComboBox(
    master=f,
    values=["HOD","Faculty"],
    variable=optionmenu_var,
    corner_radius=10,
    width=400,
    height=40
)
combobox3.place(x=30,y=630)



table_f = ct.CTkFrame(
    master=f,
    height=500,
    width=600,
    corner_radius=0,
    fg_color="#212120",
    bg_color="#2a2b2a"
)
table_f.place(x=460,y=150)


tree = ttk.Treeview(f,selectmode="extended")

create_treeview()
update_treeview()


btn_del = ct.CTkButton(
    master=f,
    text="Delete Teacher",
    height=40,
    hover=False,
    fg_color="#F45050",
    font=("consolas",18,"bold"),
    # text_color="black"
    command=remove_data
)
btn_del.place(x=800,y=700)

btn_update = ct.CTkButton(
    master=f,
    text="Update Teacher",
    height=40,
    hover=False,
    fg_color="#C490E4",
    font=("consolas",18,"bold"),
    # text_color="black"
    command=update_data
)
btn_update.place(x=620,y=700)

btn_add = ct.CTkButton(
    master=f,
    text="Add Teacher",
    height=40,
    hover=False,
    fg_color="#9BCF53",
    font=("consolas",18,"bold"),
    # text_color="black"
    command=parse_data
)
btn_add.place(x=450,y=700)

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
).place(x=320,y=700)
 
def clear():
    passw.destroy()







passw.mainloop()