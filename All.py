from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
win=Tk()

win.config(bg='sky blue')
win.title("Login Window")
win.geometry("1500x1500")

Image = Image.open("counter_bg1.jpg")
render = ImageTk.PhotoImage(Image)
img = Label(win, image=render)
img.place(x=0, y=0)
f1 = ("Arial", 30, 'bold')
l1 = Label(win, text="Student Project Information", font=f1, fg='black')
l1.place(x=510, y=30)
def show():
    f = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all types", "*.*")))
def student():
    win = Tk()
    win.title("Student Form")
    win.geometry("1500x1500")
    win.config(bg="purple")
    def clrfield():
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete(0, END)
        t7.delete(0, END)


    def showrec():
        mydb = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="pms")
        mycur = mydb.cursor()
        mycur.execute("select Roll_No from student")
        mydata = mycur.fetchone()
        if mydata == None:
            t1.insert(0, '1')
        else:
            cnt = mydata[0] + 1
            t1.insert(0, cnt)

    def saverec():
        s1 = t1.get()
        s2 = t2.get()
        s3 = t3.get()
        s4 = t4.get()
        s5 = t5.get()
        s6 = t6.get()
        s7 = t7.get()
        if s2 == '':
            messagebox.showinfo("plzz enter  Lead_Name")
            return
        if s3 == '':
            messagebox.showinfo("plzz enter E_Mail")
            return
        if s4 == '':
            messagebox.showinfo("plzz enter  Department ")
            return
        if s5 == '':
            messagebox.showinfo("plzz enter Project_Name")
            return
        if s6 == '':
            messagebox.showinfo("plzz enter Sub_Date")
            return
        if s7 == '':
            messagebox.showinfo("plzz enter Mobile_No ")
            return

        mydb = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='pms'
        )
        mycur = mydb.cursor()
        mycur.execute(
            "insert into student values (" + s1 + ",'" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "'," + s6 + ",'" + s7 + "')")
        mydb.commit()
        messagebox.showinfo("confirm", "Rec is saved successfully")
        clrfield()
        showrec()
        win.destroy()

    def serrec():
        s1 = t1.get()
        clrfield()
        mydb = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='pms'
        )
        mycur = mydb.cursor()
        mycur.execute("select * from student where Roll_No=" + s1)
        mydata = mycur.fetchone()
        if mydata is None:
            messagebox.showwarning("warning...", "Rec is not found")
            return
        else:
            t2.insert(0, mydata[1])
            t3.insert(0, mydata[2])
            t4.insert(0, mydata[3])
            t5.insert(0, mydata[4])
            t6.insert(0, mydata[5])
            t7.insert(0, mydata[6])

    def uprec():
        s1 = t1.get()
        s2 = t2.get()
        s3 = t3.get()
        s4 = t4.get()
        s5 = t5.get()
        s6 = t6.get()
        s7 = t7.get()

        if s2 == '':
            messagebox.showinfo("plzz enter Lead_Name")
            return
        if s3 == '':
            messagebox.showinfo("plzz enter E_Mail")
            return
        if s4 == '':
            messagebox.showinfo("plzz enter Department")
            return
        if s5 == '':
            messagebox.showinfo("plzz enter Project_Name")
            return
        if s6 == '':
            messagebox.showinfo("plzz enter Sub_Date")
            return
        if s7 == '':
            messagebox.showinfo("plzz enter Mobile_No")
            return
        mydb = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='pms'
        )
        mycur = mydb.cursor()
        mycur.execute("update student set Lead_Name='" + s2 + "',E_Mail='" + s3 + "',Department='" + s4 + "',Project_Name='" + s5 + "',Sub_Date='" + s6 + "',Mobile_No='" + s7 + "'")
        mydb.commit()
        messagebox.showinfo("confirm", "Rec is updated successfully")
        clrfield()
        showrec()

    def delrec():
        ans = messagebox.askyesnocancel("confirm...", "Are you sure want to delete the record")
        if ans:
            s1 = t1.get()
            mydb = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='pms'
            )
            mycur = mydb.cursor()
            mycur.execute("delete from student where Roll_No=" + s1)
            mydb.commit()
            messagebox.showinfo("confirm", "record is deleted sucessfully")
            clrfield()
            showrec()

    f1 = ("Arial", 30, 'bold')
    l1 = Label(win, text="Student Form", font=f1)
    l1.place(x=600, y=20)

    f2 = ("Arial", 16, 'bold')
    l2 = Label(win, text="Roll_No:", font=f2, fg='black')
    l2.place(x=530, y=150)
    t1 = Entry(win, bd=4, font=f2)
    t1.place(x=700, y=150)

    l3 = Label(win, text="Lead_Name:", font=f2, fg='black')
    l3.place(x=530, y=220)
    t2 = Entry(win, bd=4, font=f2)
    t2.place(x=700, y=220)

    l4 = Label(win, text="E_Mail:", font=f2, fg='black')
    l4.place(x=530, y=290)
    t3 = Entry(win, bd=4, font=f2)
    t3.place(x=700, y=290)

    l5 = Label(win, text="Department:", font=f2, fg='black')
    l5.place(x=530, y=360)
    t4 = Entry(win, bd=4, font=f2)
    t4.place(x=700, y=360)

    l6 = Label(win, text="Project_Name:", font=f2, fg='black')
    l6.place(x=530, y=430)
    t5 = Entry(win, bd=4, font=f2)
    t5.place(x=700, y=430)

    l7 = Label(win, text="Sub_Date:", font=f2, fg='black')
    l7.place(x=530, y=500)
    t6 = Entry(win, bd=4, font=f2)
    t6.place(x=700, y=500)

    l8 = Label(win, text="Mobile_No:", font=f2, fg='black')
    l8.place(x=530, y=570)
    t7 = Entry(win, bd=4, font=f2)
    t7.place(x=700, y=570)

    b1 = Button(win, text="Save", font=f2, bg="yellow", fg='black', command=saverec)
    b1.place(x=420, y=660)

    b3 = Button(win, text="Search", font=f2, bg="yellow", fg='black', command=serrec)
    b3.place(x=550, y=660)

    b1 = Button(win, text="Add", font=f2, bg="yellow", fg='black', command=showrec)
    b1.place(x=720, y=660)

    b4 = Button(win, text="Update", font=f2, bg="yellow", fg='black', command=uprec)
    b4.place(x=850, y=660)

    b5 = Button(win, text="Delete", font=f2, bg="yellow", fg='black', command=delrec)
    b5.place(x=990, y=660)

    b6 = Button(win, text="Exit", font=f2, bg="yellow", fg='black', command=quit)
    b6.place(x=1130, y=660)

    win.mainloop()

f2 = ("Arial", 15, 'bold')
b1 = Button(win, text="Student Form", font=f2, width=25, height=2, command=student)
b1.place(x=150, y=200)
b1 = Button(win, text="Upload Project", font=f2, width=25, height=2,command=show)
b1.place(x=550, y=400)
b1 = Button(win, text="Project Mentor", font=f2, width=25, height=2)
b1.place(x=1000, y=600)
win.mainloop()
