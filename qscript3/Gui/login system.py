from tkinter import *
from PIL import ImageTk
import mysql.connector
from tkinter import messagebox
window=Tk()
window.geometry("600x400+400+200")
background_img=PhotoImage(file=r"C:\Users\sagar\Downloads\images1.png")
bg_label=Label(window)
bg_label.configure(image=background_img)
bg_label.pack()


def singin():
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
	    		def func_close():
	    			win.destroy()
	    		win.mainloop()	                                                                                                          	                                                                           
                                     
                       # frame=Frame(win,height=92,width=584,bd=5,relief=SUNKEN)
                        #frame.place(x=91,y=298)
                
                          
           


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
	singin()
password_entry.bind('<Return>',pass_func)

	
button_bg=PhotoImage(file=r"C:\Users\sagar\Desktop\images.png")
signin_button=Button(window,image=button_bg,command=singin,activebackground="lightgreen",activeforeground="red",font="Helvetica 15  bold",width=190,height=57,cursor="hand2")
signin_button.place(x=240,y=300)



window.mainloop()
