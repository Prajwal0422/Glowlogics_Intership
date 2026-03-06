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

root.mainloop()