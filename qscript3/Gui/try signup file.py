from tkinter import *
from tkinter import messagebox
import mysql.connector 
import time
import random
from PIL import ImageTk

class login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("640x400+320+200")
        self.root.resizable(0,0)
        self.root.title("guessing game")
        #bg image
        self.img=PhotoImage(file=r"C:\Users\sagar\Downloads\IMG_20200720_144928.png")
        background_img=Label(self.root,image=self.img)
        background_img.pack()
        # label
        name=Label(self.root,text="Name:",fg="lightgreen",bg="black",font="Helvetica  18 bold")
        name.place(x=75,y=82)

        user_name=Label(self.root,text="UserName:",fg="red",bg="black",font="Helvetica  18 bold")
        user_name.place(x=75,y=200)

        age=Label(self.root,text="age:",fg="#862159",bg="black",font="Helvetica 18  bold")
        age.place(x=75,y=142)

        password=Label(self.root,text="password:",fg="red",bg="black",font="Helvetica 18  bold")
        password.place(x=75,y=257)

        #VARIABLE
        self.name_var=StringVar()
        self.age_var=StringVar()
        self.user_var=StringVar()
        self.password_var=StringVar()
        self.var=BooleanVar()


        #ENTRY
        name_entry=Entry(self.root,textvariable=self.name_var,width=25,font="Helvetica   18  bold",bg="white",fg="black")
        name_entry.place(x=251,y=82)
        name_entry.focus_set()
        def enter(event):
            age_entry.focus_set()
        name_entry.bind('<Return>',enter)

        age_entry=Entry(self.root,textvariable=self.age_var,width=25,font="Helvetica 18  bold",bg="white",fg="black")
        age_entry.place(x=251,y=142)
        age_entry.bind('<Return>',lambda x:user_entry.focus_set())

        user_entry=Entry(self.root,textvariable=self.user_var,width=25,font="Helvetica   18  bold",bg="white",fg="black")
        user_entry.place(x=251,y=200)
        user_entry.bind('<Return>',lambda x:password.focus_set())

        password=Entry(self.root,textvariable=self.password_var,show="*",width=25,font="Helvetica 18  bold",bg="white",fg="black")
        password.place(x=251,y=257)
        def call(event):
            func()
        password.bind('<Return>',call)

        #checkbox  
        box=Checkbutton(self.root,text="I have read and accept the terms & condition.",font="Helvetica 11  bold",bg="black",fg="red",variable=self.var,activebackground="black",activeforeground="red")
        box.place(x=75,y=310)

        #button
        submit_button=Button(self.root,text="Register",bg="lightgreen",fg="red",activebackground="lightgreen",activeforeground="red",font="Helvetica 15  bold",width=14,cursor="hand2",command=self.func)
        submit_button.place(x=130,y=350)

        #clock
        self.display=Label(self.root,font="Arial  38",justify=CENTER,fg="red",bg="black")
        self.display.place(x=0,y=0,width=650)
        self.clock()   


    #digital clock
    
    def clock(self):
        current_time=time.strftime("%I:%M:%S")
        self.display["text"]=current_time
        self.display.after(200,self.clock)
        
    

    #register function
    def func(self):
        user=self.name_var.get()
        user_age=self.age_var.get()
        username=self.user_var.get()
        user_password=self.password_var.get()
        check_var=self.var.get()
    
        if user  ==" " or user_age=="" or username=="" or user_password=="" or check_var==False :
            messagebox.showerror("Error","All Filed Are Required")
        else:
            if  user_age=="18" or user_age >="18":                                                
                conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="gamedata")
                my_cursor=conn.cursor()
                query1="select * from gameuser where username=%(username)s";
                value={"username":self.user_var.get()}
                my_cursor.execute(query1,value)                
                result=my_cursor.fetchone()
                if result!=None:
                    messagebox.showerror('error','username already have taken')
                else:                                        
                    query=("INSERT INTO gameuser""(name,age,username,password,licence_accept)""VALUES(%s,%s,%s,%s,%s)");
                    val2=(self.name_var.get(),self.age_var.get(),self.user_var.get(),self.password_var.get(),self.var.get())
                    my_cursor.execute(query,val2)
                    conn.commit()
                    messagebox.showinfo('info','Register successfully')
                    conn.close() 
                    root.destroy()
                    if __name__=="__main__":
                        import database
                             
            else:
                   messagebox.showwarning("warning","You are not 18 years old") 
                 









   




root=Tk()
obj=login(root)
root.mainloop()





