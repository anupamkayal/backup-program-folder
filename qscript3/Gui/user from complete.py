from tkinter import *
from tkinter import  messagebox
import mysql.connector as mariadb
root=Tk()
root.geometry("700x500")
root.configure(bg="yellow")
label=Label(root,text="Enter your name :",fg="red",bg="yellow")
label.grid(row=1,column=0,padx=43,pady=43)
label2=Label(root,text="enter your age : ",fg="red",bg="yellow" )
label2.grid(row=2,column=0)
label3=Label(root,text="email address :",fg="red",bg="yellow"  )
label3.grid(row=3,column=0,pady=43)
val=StringVar()
entrybox=Entry(root,width=18,textvariable=val)
entrybox.grid(row=1,column=1)
val2=IntVar()
entrybox2=Entry(root,width=18,textvariable=val2)
entrybox2.grid(row=2,column=1)
val3=StringVar()
entrybox3=Entry(root,width=18,textvariable=val3)
entrybox3.grid(row=3,column=1,pady=34,sticky=W+E)
try:
    def action():
        obj1=val.get()
        obj2=val2.get()
        obj3=val3.get()
        if obj1=="" and obj2==0 and obj3=="":
            messagebox.showerror("error","please fill the all box")
        else:                   
             conn=mariadb.connect(host="localhost",user="root",password="",database="userdata")
             my_cursor=conn.cursor()
             query=("INSERT INTO checktable""(name,age,email)""VALUES(%s,%s,%s)");
             my_cursor.execute(query, (val.get(),val2.get(),val3.get())   )
             conn.commit()
             conn.close()
             entrybox.delete(0,END)
             entrybox2.delete(0,END)
             entrybox3.delete(0,END)
             messagebox.showinfo("info","save successfully")

except FileNotFoundError:
    print("file not found")

submit=Button(root,text="Submit",width=5,bg="green",fg="lightblue",command=action)
submit.grid(row=4, column=1,pady=56)
def quitfunc():
    variable=messagebox.askyesno("coution","Do you want to close ")
    
    if variable==1:
        root.destroy()
    else:
        return
    
exit=Button(root,text='Exit',width=5,bg="red",fg="white",command=quitfunc)
exit.grid(row=4,column=0,pady=56)
root.mainloop()