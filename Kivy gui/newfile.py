#pylint:disable=E0001
from tkinter import *
from tkinter import  ttk
from tkinter import  messagebox
import  random
root=Tk()
root.geometry("700x590")
root.configure(bg="lightpink")
root.title("guessing game")
user_name=Label(root,text="UserName:",fg="red",bg="lightpink",font="Helvetica   11  bold")
user_name.place(x=12,y=82)
user_var=StringVar()
user_entry=Entry(root,textvariable=user_var,width=17,font="Helvetica   11  bold")
user_entry.place(x=251,y=82)
age=Label(root,text="Age:",fg="#862159",bg="lightpink", font="Helvetica   11  bold")
age.place(x=52,y=210)
age_var=IntVar()
age_entry=Entry(root,textvariable=age_var,width=17,font="Helvetica 11  bold")
age_entry.place(x=251,y=210)
def func():
    user=user_var.get()
    user_age=age_var.get()
    try: 
        if user  ==" " or user_age==0:
            messagebox.showerror("Error","please! enter username and age ")
        else:
            if  user_age==18 or user_age >=18:
                #with open("file.txt""a") as file:
#                    file.write(f"user_name:{user},user_age:{user_age}\n")
#                    file.close()
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
                    def reset_func():
                        global winning_num                       
                        num_entry.delete(0,END)
                        label3.configure(text="Best of luck")
                        winning_num=(random.randint(1,100))
                                                                                                                
                    reset=Button(win,text="Reset",bg="red",fg="white",activebackground="red",activeforeground="white",cursor="hand2",command=reset_func)
                    reset.place(x=0,y=460)
                    win.mainloop()
                     
               
                   
                          
            else:
                   messagebox.showwarning("warning","You are not 18 years old")
            
                 
    except:
           return
                    
                    
            
            
    
   
    
submit=Button(root,text="Start",width=11,bg="pink",fg="green",activebackground="pink",activeforeground="green",cursor="hand2",command=func)
submit.place(x=91,y=446)
def func_quit():
    var=messagebox.askokcancel("warrning","Do you want to exit")
    if var:
        root.destroy()
exit=Button(root,text="Exit",width=9,bg="pink",fg="green",activebackground="pink",activeforeground="green",cursor="hand2",command=func_quit)
exit.place(x=441,y=446)






root.mainloop()





