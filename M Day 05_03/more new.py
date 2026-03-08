from tkinter import *
myw = Tk()
myw.geometry("400x40+500+200")
myw.title("first GUI project")
myw.configure(bg="yellow")

lb1=Label(myw, text = "username",fg="red")
lb1.place(x=10, y=20)
myw.mainloop()