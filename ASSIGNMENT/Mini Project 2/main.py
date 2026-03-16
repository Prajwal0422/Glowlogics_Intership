from tkinter import *
from tkinter import messagebox
import xlsxwriter

root = Tk()
root.geometry("560x450")

Label(root,text="STUDENT MARKS DETAILS",font=("Arial",18)).pack()

Label(root,text="Roll No").place(x=50,y=80)
e1=Entry(root)
e1.place(x=200,y=80)

Label(root,text="Student Name").place(x=50,y=120)
e2=Entry(root)
e2.place(x=200,y=120)

Label(root,text="Subject 1").place(x=50,y=160)
e3=Entry(root)
e3.place(x=200,y=160)

Label(root,text="Subject 2").place(x=50,y=200)
e4=Entry(root)
e4.place(x=200,y=200)

Label(root,text="Subject 3").place(x=50,y=240)
e5=Entry(root)
e5.place(x=200,y=240)

Label(root,text="Total").place(x=50,y=280)
e6=Entry(root)
e6.place(x=200,y=280)

Label(root,text="Average").place(x=50,y=320)
e7=Entry(root)
e7.place(x=200,y=320)

def calculate():
    roll=e1.get()
    name=e2.get()
    s1=int(e3.get())
    s2=int(e4.get())
    s3=int(e5.get())

    total=s1+s2+s3
    avg=total/3

    e6.delete(0,END)
    e7.delete(0,END)

    e6.insert(0,total)
    e7.insert(0,avg)

    workbook=xlsxwriter.Workbook("students.xlsx")
    sheet=workbook.add_worksheet()

    headers=["Roll","Name","Sub1","Sub2","Sub3","Total","Average"]

    for i in range(len(headers)):
        sheet.write(0,i,headers[i])

    sheet.write_row(1,0,[roll,name,s1,s2,s3,total,avg])

    workbook.close()

    messagebox.showinfo("Saved","Data Saved Successfully")

Button(root,text="CALCULATE & SAVE",command=calculate,width=20,bg="green").place(x=200,y=370)

root.mainloop()