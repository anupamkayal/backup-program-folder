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
        self.display=Label(self.root,font="Arial  38",fg="red",bg="black")
        self.display.pack()
        self.clock()   


    #digital clock
    
    def clock(self):
        current_time=time.strftime("%I:%M:%S")
        self.display["text"]=current_time
        self.display.after(300,self.clock)
    
        
    

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
                value={"username":user_var.get()}
                my_cursor.execute(query1,value)                
                result=my_cursor.fetchone()
                if result!=None:
                    messagebox.showerror('error','username already have taken')
                else:                                        
                    query=("INSERT INTO gameuser""(name,age,username,password,licence_accept)""VALUES(%s,%s,%s,%s,%s)");
                    val2=(name_var.get(),age_entry.get(),user_var.get(),password_var.get(),var.get())
                    my_cursor.execute(query,val2)
                    conn.commit()
                    messagebox.showinfo('info','Register successfully')
                    conn.close() 
                    root.destroy()
                   
                    if __name__=="__main__":
                        win=Tk()
                        win.geometry("700x590")
                        win.title("guessing game")
                        win.configure(bg="lightblue")
                        guess_num=Label(win,text="guess a number between 1 to 100 :  ",font="Helvetica  9  bold",bg="orange",fg="white")
                        guess_num.pack()                    
                        num_entry=Entry(win,font="Helvetica  11  bold")
                        num_entry.place(x=91,y=100)
                        out_label=Label(win,text="Output:",font="Helvetica 11 bold",bg="orange",fg="white")
                        out_label.place(x=291,y=239)                                        
                        label3=Label(win,text="Best of luck",font="Helvetica  11  bold",bg="lightblue")
                        label3.place(x=91,y=298)                  
                        winning_num=random.randint(1,100)
                        def game_func():
                            guess_number=int(num_entry.get())        
                            if guess_number==winning_num:
                                label3.configure(text="congratulation,well guessed")                                                                                                
                            elif guess_number>winning_num:
                                label3.configure(text="too high")
                            elif guess_number<winning_num:
                                label3.configure(text="too low")
                            else:
                               label3.configure(text="something went wrong")                                                                                                                                                                                       
                                     
                       # frame=Frame(win,height=92,width=584,bd=5,relief=SUNKEN)
                        #frame.place(x=91,y=298)
                    submit_button=Button(win,text="Submit",bg="lightgreen",fg="red",activebackground="lightgreen",activeforeground="red",command=game_func)
                    submit_button.place(x=197,y=460)
                    def func_close():
                        win.destroy()
                    close=Button(win,text="Back",bg="green",fg="red",activebackground="green",activeforeground="red",command=func_close)
                    close.place(x=490,y=460)
                          
                    win.mainloop()
                                              
            else:
                   messagebox.showwarning("warning","You are not 18 years old") 
                 









   




root=Tk()
obj=login(root)
root.mainloop()








    

def singin():
    root.destroy()
    window=Tk()
    window.
  
    
    user_name=Label(window,text="UserName:",fg="red",bg="blue",font="Helvetica  18 bold")
    user_name.place(x=75,y=100)
    password=Label(window,text="password:",fg="red",bg="blue",font="Helvetica  18 bold")
    password.place(x=75,y=200)

    username=Entry(window,width=25,font="Helvetica 18  bold",bg="white",fg="black")
    username.place(x=251,y=100)
    username.focus_set()
    username.bind("<Return>",lambda x:password_entry.focus_set())
    password_entry=Entry(window,width=25,font="Helvetica 18  bold",bg="white",fg="black")
    password_entry.place(x=251,y=200)
    def pass_func(event):
        login()
    password_entry.bind('<Return>',pass_func)
   

    def login():

        conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="gamedata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from gameuser where username=%s and password=%s",(username.get(),password_entry.get()));
        row=my_cursor.fetchone()
    
        if row ==None:
            messagebox.showerror("Error","please! enter a valid username & password")
        else:
    
            if __name__=="__main__":
                window.destroy()
                win=Tk()
                win.geometry("700x590+320+200")
                win.title("guessing game")
                win.configure(bg="lightblue")
                guess_num=Label(win,text="guess a number between 1 to 100 :  ",font="Helvetica  9  bold",bg="orange",fg="white")
                guess_num.pack()                                
                num_entry=Entry(win,font="Helvetica  11  bold")
                num_entry.place(x=91,y=100)
                num_entry.focus_set()
                out_label=Label(win,text="Output:",font="Helvetica 11 bold",bg="orange",fg="white")
                out_label.place(x=291,y=239)                                                    
                label3=Label(win,text="Best of luck",font="Helvetica  11  bold",bg="lightblue")
                label3.place(x=91,y=298) 
                def func_close():
                        win.destroy()
                close=Button(win,text="Back",bg="green",fg="red",activebackground="green",activeforeground="red",command=func_close)
                close.place(x=490,y=460)
                                
                winning_num=random.randint(1,100)
                def game_func():
                    guess_number=int(num_entry.get())       
                    if guess_number==winning_num:
                        label3.configure(text="congratulation,well guessed")                                                                                               
                    elif guess_number>winning_num:
                        label3.configure(text="too high")
                    elif guess_number<winning_num:
                        label3.configure(text="too low")
                    else:
                        label3.configure(text="something went wrong")
                submit_button=Button(win,text="Submit",bg="lightgreen",fg="red",activebackground="lightgreen",activeforeground="red",command=game_func)
                submit_button.place(x=197,y=460) 
                    
                win.mainloop()                                                                                                                                                                                         
                                     
                       # frame=Frame(win,height=92,width=584,bd=5,relief=SUNKEN)
                       #frame.place(x=91,y=298)
    

    button_bg=PhotoImage(file=r"C:\Users\sagar\Desktop\images.png")
    signin_button=Button(window,image=button_bg,command=login,activebackground="lightgreen",activeforeground="red",font="Helvetica 15  bold",width=190,height=57,cursor="hand2")
    signin_button.place(x=240,y=300)
                        
    window.mainloop()            
                          
           









login_button=Button(root,text="Sign In",command=singin,bg="lightgreen",fg="red",activebackground="lightgreen",activeforeground="red",font="Helvetica 15  bold",width=14,cursor="hand2")
login_button.place(x=370,y=350)


root.mainloop()
