from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
win=Tk()
win.title("Welcome to Project Management System")

path=Image.open("bg.jpg")
render=ImageTk.PhotoImage(path)
img=Label(win,image=render)
img.place(x=0,y=0)
def openadminwindow():
    screen=Toplevel(win)
    screen.geometry("1280x700+0+0")
    screen.title("Admin Login")
    screen.resizable(False, False)
    backgroundImage = ImageTk.PhotoImage(file='bg1.jpg')
    def login():
        username = user.get()
        password = code.get()
        if username == 'neha' and password == '1234':
            messagebox.showinfo("Ok","Login Succesfull!!")
            win.destroy()
            import pms
        elif username != 'neha' and password != '1234':
            messagebox.showerror("Invalid", "Invalid username and password")

        elif password != "1234":
            messagebox.showerror("Invalid", "Invalid password")
        elif username != "neha":
            messagebox.showerror("Invalid", "Invalid username")

    bgLabel = Label(screen, image=backgroundImage)
    bgLabel.place(x=0, y=0)

    loginFrame = Frame(screen, bg='white')
    loginFrame.place(x=400, y=150)

    logoImage = PhotoImage(file='logo.png')

    logoLabel = Label(loginFrame, image=logoImage)
    logoLabel.grid(row=0, column=0, columnspan=2, pady=10)
    usernameImage = PhotoImage(file='user.png')
    usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT
                          , font=('times new roman', 20, 'bold'), bg='white')
    usernameLabel.grid(row=1, column=0, pady=10, padx=20)

    user = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
    user.grid(row=1, column=1, pady=10, padx=20)

    passwordImage = PhotoImage(file='password.png')
    passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT
                          , font=('times new roman', 20, 'bold'), bg='white')
    passwordLabel.grid(row=2, column=0, pady=10, padx=20)

    code = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
    code.grid(row=2, column=1, pady=10, padx=20)

    loginButton = Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15
                         , fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
                         activeforeground='white', cursor='hand2',command=login)
    loginButton.grid(row=3, column=1, pady=10)

    screen.mainloop()

def openadminwindow1():
    screen1=Toplevel(win)
    screen1.geometry("1280x700+0+0")
    screen1.title("Student Login")
    screen1.resizable(False, False)
    backgroundImage = ImageTk.PhotoImage(file='bg1.jpg')
    def login():
        username = user.get()
        password = code.get()
        if username == 'neha' and password == '1234':
            messagebox.showinfo("Ok","Login Succesfull!!")
            win.destroy()
            import All
        elif username != 'neha' and password != '1234':
            messagebox.showerror("Invalid", "Invalid username and password")

        elif password != "1234":
            messagebox.showerror("Invalid", "Invalid password")
        elif username != "neha":
            messagebox.showerror("Invalid", "Invalid username")

    bgLabel = Label(screen1, image=backgroundImage)
    bgLabel.place(x=0, y=0)

    loginFrame = Frame(screen1, bg='white')
    loginFrame.place(x=400, y=150)

    logoImage = PhotoImage(file='logo.png')

    logoLabel = Label(loginFrame, image=logoImage)
    logoLabel.grid(row=0, column=0, columnspan=2, pady=10)
    usernameImage = PhotoImage(file='user.png')
    usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT
                          , font=('times new roman', 20, 'bold'), bg='white')
    usernameLabel.grid(row=1, column=0, pady=10, padx=20)

    user = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
    user.grid(row=1, column=1, pady=10, padx=20)

    passwordImage = PhotoImage(file='password.png')
    passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT
                          , font=('times new roman', 20, 'bold'), bg='white')
    passwordLabel.grid(row=2, column=0, pady=10, padx=20)

    code = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='royalblue')
    code.grid(row=2, column=1, pady=10, padx=20)

    loginButton = Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15
                         , fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
                         activeforeground='white', cursor='hand2',command=login)
    loginButton.grid(row=3, column=1, pady=10)

    screen1.mainloop()
l1=Label(win,text="Welcome to Project Management System!!",font=("Elianto",52,'bold'),bg='black',fg='white')
l1.place(x=50,y=50)
b1=Button(win,text="ADMIN LOGIN",bg='white',font=("Elianto",22,'bold'),command=openadminwindow)
b1.place(x=250,y=400)
b2=Button(win,text="STUDENT LOGIN",bg='white',font=("Elianto",22,'bold'),command=openadminwindow1)
b2.place(x=550,y=400)
win.geometry("1500x1500+10+10")

win.mainloop()
