from tkinter import *
import time
import ttkthemes #we can apply themes on buttons
from tkinter import ttk,messagebox,filedialog

import mysql.connector
import pymysql
import pandas
#functionality Part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=projectTable.get_children()
    newlist=[]
    for index in indexing:
        content=projectTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['Id','Project_Name','Team_Name','Team_Members','Guide',
                                 'Technology_used','Abstract_idea','Added_Date','Added_Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved succesfully')


def toplevel_data(title,button_text,command):
    global idEntry,Project_NameEntry,Team_NameEntry,Team_MembersEntry,GuideEntry,Technology_usedEntry,Abstract_ideaEntry,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    Project_NameLabel = Label(screen, text='Project_Name', font=('times new roman', 20, 'bold'))
    Project_NameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    Project_NameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    Project_NameEntry.grid(row=1, column=1, pady=15, padx=10)

    Team_NameLabel = Label(screen, text='Team_Name', font=('times new roman', 20, 'bold'))
    Team_NameLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    Team_NameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    Team_NameEntry.grid(row=2, column=1, pady=15, padx=10)

    Team_MembersLabel = Label(screen, text='Team_Members', font=('times new roman', 20, 'bold'))
    Team_MembersLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    Team_MembersEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    Team_MembersEntry.grid(row=3, column=1, pady=15, padx=10)

    GuideLabel = Label(screen, text='Guide', font=('times new roman', 20, 'bold'))
    GuideLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    GuideEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    GuideEntry.grid(row=4, column=1, pady=15, padx=10)

    Technology_usedLabel = Label(screen, text='Technology_used', font=('times new roman', 20, 'bold'))
    Technology_usedLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    Technology_usedEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    Technology_usedEntry.grid(row=5, column=1, pady=15, padx=10)

    Abstract_ideaLabel = Label(screen, text='Abstract_idea', font=('times new roman', 20, 'bold'))
    Abstract_ideaLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    Abstract_ideaEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    Abstract_ideaEntry.grid(row=6, column=1, pady=15, padx=10)

    project_button = ttk.Button(screen, text=button_text, command=command)
    project_button.grid(row=7, columnspan=2, pady=15)
    if title=='Update project':
        indexing = projectTable.focus()

        content = projectTable.item(indexing)
        listdata = content['values']
        idEntry.insert (0, listdata[0])
        Project_NameEntry.insert(0, listdata[1])
        Team_NameEntry.insert(0, listdata[2])
        Team_MembersEntry.insert(0, listdata[3])
        GuideEntry.insert(0, listdata[4])
        Technology_usedEntry.insert(0, listdata[5])
        Abstract_ideaEntry.insert(0, listdata[6])


def update_data():
    query='update project set Project_Name=%s,Team_Name=%s,Team_Members=%s,Guide=%s,Technology_used=%s,Abstract_idea=%s where id=%s'
    mycursor.execute(query,(Project_NameEntry.get(),Team_NameEntry.get(),Team_MembersEntry.get(),GuideEntry.get(),
                            Technology_usedEntry.get(),Abstract_ideaEntry.get(),idEntry.get()
                            ))
    mycursor.fetchone()
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_project()



def show_project():
    query = 'select * from project'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    projectTable.delete(*projectTable.get_children())
    for data in fetched_data:
        projectTable.insert('', END, values=data)



def delete_project():
    indexing=projectTable.focus()
    print(indexing)
    content=projectTable.item(indexing)
    content_id=content['values'][0]
    query='delete from project where id=%s'
    mycursor.execute(query)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from project'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    projectTable.delete(*projectTable.get_children())
    for data in fetched_data:
        projectTable.insert('',END,values=data)




def search_data():
    query='select * from project where id=%s or Project_Name=%s or Team_Name=%s or Team_Members=%s or Guide=%s or Technology_used=%s or Abstract_idea=%s'
    mycursor.execute(query,(idEntry.get(),Project_NameEntry.get(),Team_NameEntry.get(),Team_MembersEntry.get(),GuideEntry.get(),Technology_usedEntry.get(),Abstract_ideaEntry.get()))
    projectTable.delete(*projectTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        projectTable.insert('',END,values=data)




def add_data():
    if idEntry.get()=='' or Project_NameEntry.get()=='' or Team_NameEntry.get()=='' or Team_MembersEntry.get()=='' or GuideEntry.get()=='' or Technology_usedEntry.get()=='' or Abstract_ideaEntry.get()=='':
        messagebox.showerror('Error','All Fields are required',parent=screen)

    else:
        try:
            query='insert into project values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),Project_NameEntry.get(),Team_NameEntry.get(),Team_MembersEntry.get(),GuideEntry.get(),
                                    Technology_usedEntry.get(),Abstract_ideaEntry.get(),date,currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                Project_NameEntry.delete(0,END)
                Team_NameEntry.delete(0,END)
                Team_MembersEntry.delete(0,END)
                GuideEntry.delete(0,END)
                Technology_usedEntry.delete(0,END)
                Abstract_ideaEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return


        query='select *from project'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        projectTable.delete(*projectTable.get_children())
        for data in fetched_data:
            projectTable.insert('',END,values=data)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=mysql.connector.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()

        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query='create database pms'
            mycursor.execute(query)
            query='use pms'
            mycursor.execute(query)
            query='create table project(Id int not null primary key, Project_Name varchar(30),Team_Name varchar(10),Team_Members varchar(30),' \
                  'Guide varchar(100),Technology_used varchar(20),Abstract_idea varchar(20),Added_Date varchar(50), Added_Time varchar(50))'
            mycursor.execute(query)
        except:
            query='use pms'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addprojectButton.config(state=NORMAL)
        searchprojectButton.config(state=NORMAL)
        updateprojectButton.config(state=NORMAL)
        showprojectsButton.config(state=NORMAL)
        exportprojectButton.config(state=NORMAL)
        deleteprojectButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    if count==len(s): # when it reaches to last character of system word
        count=0
        text=''
    text= text+s[count]#P
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)#300ms




def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')#gives us time in a formatted way
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)#1000ms after 1s time it will call again



#GUI Part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('keramik')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Project Management System')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Project Management System' #s[count]=r when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x= 50,y=80,width=300,height=600)

logo_image=PhotoImage(file='3273070.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addprojectButton=ttk.Button(leftFrame,text='Add Project',width=25,state=DISABLED,command=lambda :toplevel_data('Add Project','Add',add_data))
addprojectButton.grid(row=1,column=0,pady=20)

searchprojectButton=ttk.Button(leftFrame,text='Search Project',width=25,state=DISABLED,command=lambda :toplevel_data('Search Project','Search',search_data))
searchprojectButton.grid(row=2,column=0,pady=20)

deleteprojectButton=ttk.Button(leftFrame,text='Delete Project',width=25,state=DISABLED,command=delete_project)
deleteprojectButton.grid(row=3,column=0,pady=20)

updateprojectButton=ttk.Button(leftFrame,text='Update Project',width=25,state=DISABLED,command=lambda :toplevel_data('Update project','Update',update_data))
updateprojectButton.grid(row=4,column=0,pady=20)

showprojectsButton=ttk.Button(leftFrame,text='Show Projects',width=25,state=DISABLED,command=show_project)
showprojectsButton.grid(row=5,column=0,pady=20)

exportprojectButton=ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED,command=export_data)
exportprojectButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

projectTable=ttk.Treeview(rightFrame,columns=('Id','Project_Name','Team_Name','Team_Members','Guide',
                                 'Technology_used','Abstract_idea','Added_Date','Added_Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=projectTable.xview)
scrollBarY.config(command=projectTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

projectTable.pack(expand=1,fill=BOTH)

projectTable.heading('Id',text='Id')
projectTable.heading('Project_Name',text='Project Name')
projectTable.heading('Team_Name',text='Team Name')
projectTable.heading('Team_Members',text='Team Members')
projectTable.heading('Guide',text='Guide')
projectTable.heading('Technology_used',text='Technology used')
projectTable.heading('Abstract_idea',text='Abstract idea')
projectTable.heading('Added_Date',text='Added Date')
projectTable.heading('Added_Time',text='Added Time')

projectTable.column('Id',width=50,anchor=CENTER)
projectTable.column('Project_Name',width=300,anchor=CENTER)
projectTable.column('Team_Name',width=350,anchor=CENTER)
projectTable.column('Team_Members',width=200,anchor=CENTER)
projectTable.column('Guide',width=300,anchor=CENTER)
projectTable.column('Technology_used',width=200,anchor=CENTER)
projectTable.column('Abstract_idea',width=200,anchor=CENTER)
projectTable.column('Added_Date',width=200,anchor=CENTER)
projectTable.column('Added_Time',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')

projectTable.config(show='headings')

root.mainloop()

