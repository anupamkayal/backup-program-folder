import tkinter as tk
root=tk.Tk()
root.title("srring concatenation gui")
root.geometry("678x590")()
pdb.set_trace
labelbox=ttk.Label(root,text="enter your first name : ")
labelbox.grid(row=1, column=1,pady=43)
labelbox2=ttk.Label(root,text="enter your last name : ")
labelbox2.grid(row=2,column=1,pady=43,sticky="w")
labelbox3=ttk.Label(root,text="       your full name is : ")
labelbox3.grid(row=3,column=1,pady=43)
var=tk.StringVar()
entrybox=ttk.Entry(root, width=17,textvariable=var)
entrybox.grid(row=1, column=2,pady=43)
var2=tk.StringVar()
entrybox2=ttk.Entry(root,width=17, textvariable=var2)
entrybox2.grid(row=2,column=2,pady=43)

def action ():
	fname=var.get()
	lname=var2.get()
	full_name=(fname+lname) 
	entrybox.config(text=full_name)

entrybox=ttk.Entry(root,text="",width=17,) 
entrybox.grid(row=3,column=2,pady=43)

entrybox3=ttk.Entry(root,width=17,) 
entrybox3.grid(row=3,column=2,pady=43)

def action ():
	fname=var.get()
	lname=var2.get()
	full_name=(fname+lname) 
	entrybox.config(text=full_name)
action ()
submit=ttk.Button(root,text="submit",width=13,command=action)
submit.grid(row=4, column=2,pady=43)
root.mainloop()


