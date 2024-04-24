import customtkinter as ct 
import tkinter as tk 
import os
import sqlite3
from tkinter import ttk
from tkinter import messagebox



con = sqlite3.connect(r'files/timetable.db')
con.execute('CREATE TABLE IF NOT EXISTS SUBJECTS\
            (SUBCODE CHAR(10) NOT NULL PRIMARY KEY,\
            SUBNAME CHAR(50) NOT NULL,\
            SUBTYPE CHAR(1) NOT NULL, \
            DEPARTMENT CHAR(50) NOT NULL,\
            HOURS CHAR(30) NOT NULL)' )

def create_treeview():
    tree['columns'] = list(map(lambda x: '#' + str(x), range(1, 5)))
    tree['columns'] = ('one', 'two', 'three','four')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=115, stretch=tk.NO)
    tree.column("two", width=220, stretch=tk.NO)
    tree.column("three", width=110, stretch=tk.NO)
    tree.column("four", width=110, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="Code")
    tree.heading('two', text="Name")
    tree.heading('three', text="Type")
    tree.heading('four', text="Department")
    tree['height'] = 19
    tree.tag_configure('gray',background="lightgray")
    tree.tag_configure('normal',background="white")

def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return
    for i in tree.selection():
        # print(tree.item(i)['values'][0])
        con.execute(f"DELETE FROM SUBJECTS WHERE SUBCODE = '{tree.item(i)['values'][0]}'")
        con.commit()
        tree.delete(i)
        update_treeview()



def update_treeview():
    m_tag='normal'
    for row in tree.get_children():
        tree.delete(row)
    cursor = con.execute("SELECT * FROM SUBJECTS")
    for row in cursor:
        # print(row[0], row[1], row[2])
        if m_tag == 'gray':
            m_tag='normal'
        else:
            m_tag='gray'
        if row[2] == 'T':
            t = 'Theory'
        elif row[2] == 'P':
            t = 'Practical'
        tree.insert(
            "",
            0,
            values=(row[0],row[1],t,row[3])
        )
    tree.place(x=480, y=200)


def parse_data():
    subcode = str(lbl1.get())
    subname = str(lbl2.get()).upper().rstrip()
    subtype = str(var.get()).upper()
    dep=str(lbl3.get())

    if subcode=="":
        subcode = None
    if subname=="":
        subname = None

    if subcode is None or subname is None:
        messagebox.showerror("Bad Input", "Please fill up Subject Code and/or Subject Name!")
        lbl1.delete(0, tk.END)
        lbl2.delete(0, tk.END)
        return

    con.execute(f"INSERT INTO SUBJECTS (SUBCODE, SUBNAME, SUBTYPE , DEPARTMENT) VALUES ('{subcode}','{subname}','{subtype}','{dep}')")
    con.commit()
    update_treeview()
    
    lbl1.delete(0, tk.END)
    lbl2.delete(0, tk.END)
    lbl3.set('Select Depaetment...')
    
def update_data():
    lbl1.delete(0, tk.END)
    lbl2.delete(0, tk.END)
    lbl3.set('Select Depaetment...')
    
    
    try:
        # print(tree.selection())
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one subject at a time to update!")
            return

        row = tree.item(tree.selection()[0])['values']
        lbl1.insert(0, row[0])
        lbl2.insert(0, row[1])
        lbl3.set(row[3])
        if row[2][0] == "T":
            R1.select()
        elif row[2][0] == "P":
            R2.select()

        con.execute(f"DELETE FROM SUBJECTS WHERE SUBCODE = '{row[0]}'")
        con.commit()
        update_treeview()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return


passw = ct.CTk()
width = 1100
height = 750
# x=(passw.winfo_screenwidth()//10)-(-width//3)
# y=(passw.winfo_screenheight()//3)-(height//4)
passw.geometry(f"{width}x{height}+{640}+{200}")
passw.overrideredirect(1)

f = ct.CTkFrame(
    master=passw,
    height=800,
    width=1100
).pack()

header = ct.CTkLabel(
    master=f,
    text="Add / Update Students",
    font=("Consolas",40,"bold"),
    fg_color="transparent",
    bg_color="#2a2b2a"
)
header.place(x=30,y=20)

lbl1 = ct.CTkEntry(
    master=f,
    placeholder_text="Enter Subject Code....",
    corner_radius=10,
    width=400,
    height=40
)
lbl1.place(x=30,y=150)

lbl2 = ct.CTkEntry(
    master=f,
    placeholder_text="Enter Subject Name....",
    corner_radius=10,
    width=400,
    height=40
)
lbl2.place(x=30,y=210)

option= ct.StringVar(value="Select Department...")
lbl3= ct.CTkComboBox(
    master=f,
    values=["IT","COMPS","EXTC","MECH"],
    variable=option,
    corner_radius=10,
    width=400,
    height=40
)
lbl3.place(x=30,y=270)

lbl = ct.CTkLabel(
    master=f,
    bg_color="#2a2b2a",
    corner_radius=10,
    text="Subject Type :",
    width=100,
    font=("Helvetica", 16,"bold"),
    height=40
)
lbl.place(x=20,y=330)

var=ct.StringVar(value='A')
R1= ct.CTkRadioButton(
    master=f,
    variable=var,
    value='T',
    text="THEORY",
    font=("consolas",15,"bold"),
    bg_color="#2a2b2a",
    hover_color="red",
    fg_color="orange"
)
R1.place(x=170, y=340)

R2= ct.CTkRadioButton(
    master=f,
    variable=var,
    value='P',
    text="PRACTICAL",
    bg_color="#2a2b2a",
    font=("consolas",15,"bold"),
    hover_color="red",
    fg_color="orange"
)
R2.place(x=300, y=340)





table_f = ct.CTkFrame(
    master=f,
    height=500,
    width=600,
    corner_radius=0,
    fg_color="#212120",
    bg_color="#2a2b2a",
)
table_f.place(x=460,y=150)


tree = ttk.Treeview(f,selectmode="extended")

create_treeview()
update_treeview()


btn_del = ct.CTkButton(
    master=f,
    text="Delete Subject",
    height=40,
    hover=False,
    fg_color="#F45050",
    font=("consolas",18,"bold"),
    # text_color="black"
    command=remove_data
)
btn_del.place(x=150,y=480)

btn_update = ct.CTkButton(
    master=f,
    text="Update Subject",
    height=40,
    hover=False,
    fg_color="#C490E4",
    font=("consolas",18,"bold"),
    # text_color="black"
    command=update_data
)
btn_update.place(x=250,y=420)

btn_add = ct.CTkButton(
    master=f,
    text="Add Subject",
    height=40,
    hover=False,
    fg_color="#9BCF53",
    font=("consolas",18,"bold"),
    # text_color="black"
    command=parse_data
)
btn_add.place(x=50,y=420)

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
).place(x=170,y=540)
 
def clear():
    passw.destroy()







passw.mainloop()