from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

class Login:
	def __init__(self,root):
		self.root=root
		self.root.geometry("600x400+400+200")
		self.root.title('login system')
		self.root.resizable(0,0)
		self.root.wm_iconbitmap('student_icon.ico')
		#variable
		self.uservar=StringVar()
		self.passwordvar=StringVar()

		self.img=PhotoImage(file="loginimg.png")
		background_img=Label(self.root,image=self.img)
		background_img.pack()
		user_name=Label(self.root,text="UserName:",fg="red",bg="blue",font="Helvetica  18 bold")
		user_name.place(x=75,y=100)
		password=Label(self.root,text="password:",fg="red",bg="blue",font="Helvetica  18 bold")
		password.place(x=75,y=200)
		username=Entry(self.root,textvariable=self.uservar,width=25,font="Helvetica 18  bold",bg="white",fg="black")
		username.place(x=251,y=100)
		username.focus_set()
		username.bind("<Return>",lambda x:password_entry.focus_set())
		password_entry=Entry(self.root,width=25,textvariable=self.passwordvar,font="Helvetica 18  bold",bg="white",fg="black")
		password_entry.place(x=251,y=200)
		password_entry.bind('<Return>',self.pass_func)
		#self.button_bg=PhotoImage(file=r"C:\Users\sagar\Desktop\images.png")
		signin_button=Button(self.root,command=self.loginfunc,text="Login",bd=3,relief="solid",bg="#3399FF",fg="black",activebackground="#3399FF",activeforeground="black",font="Helvetica 15  bold",cursor="hand2")
		signin_button.place(x=220,y=300,width=250,height=37,)
                    
  
 
	def loginfunc(self):
		username=self.uservar.get()
		password=self.passwordvar.get()
		if username=="" or password =="":
			messagebox.showerror("Error","please! enter username and password")
		else:	
			conn=mysql.connector.connect(host="localhost",user="root",password="12345678",database="gamedata")
			my_cursor=conn.cursor()
			my_cursor.execute("select * from gameuser where username=%s and password=%s",(self.uservar.get(),self.passwordvar.get()));
			row=my_cursor.fetchone()
			if row ==None:
				messagebox.showerror("Error","please! enter a valid username & password")
			else:
				self.root.destroy()
				import database
      
	def pass_func(self,event):
		self.loginfunc()


root=Tk()
obj=Login(root)
root.mainloop()

