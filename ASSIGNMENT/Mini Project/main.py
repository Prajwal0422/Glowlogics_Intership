from tkinter import *
from excel_handler import save_excel
from database import save_mysql

root = Tk()
root.title("Student Marks System")
root.geometry("500x400")

Label(root,text="Roll Number").grid(row=0,column=0)
Label(root,text="Student Name").grid(row=1,column=0)
Label(root,text="Subject 1").grid(row=2,column=0)
Label(root,text="Subject 2").grid(row=3,column=0)
Label(root,text="Subject 3").grid(row=4,column=0)
Label(root,text="Total").grid(row=5,column=0)
Label(root,text="Average").grid(row=6,column=0)

roll=Entry(root)
name=Entry(root)
s1=Entry(root)
s2=Entry(root)
s3=Entry(root)
total=Entry(root)
avg=Entry(root)

roll.grid(row=0,column=1)
name.grid(row=1,column=1)
s1.grid(row=2,column=1)
s2.grid(row=3,column=1)
s3.grid(row=4,column=1)
total.grid(row=5,column=1)
avg.grid(row=6,column=1)

def calculate():

    m1 = int(s1.get())
    m2 = int(s2.get())
    m3 = int(s3.get())

    t = m1 + m2 + m3
    a = t / 3

    total.delete(0,END)
    total.insert(0,t)

    avg.delete(0,END)
    avg.insert(0,a)

def excel_button():

    data = {
        "Roll": roll.get(),
        "Name": name.get(),
        "Subject1": s1.get(),
        "Subject2": s2.get(),
        "Subject3": s3.get(),
        "Total": total.get(),
        "Average": avg.get()
    }

    save_excel(data)

def mysql_button():

    data = {
        "Roll": roll.get(),
        "Name": name.get(),
        "Subject1": s1.get(),
        "Subject2": s2.get(),
        "Subject3": s3.get(),
        "Total": total.get(),
        "Average": avg.get()
    }

    save_mysql(data)

Button(root,text="TOTAL",command=calculate,width=10).grid(row=7,column=0)

Button(root,text="EXCEL",command=excel_button,width=10).grid(row=7,column=1)

Button(root,text="MYSQL",command=mysql_button,width=10).grid(row=7,column=2)

root.mainloop()