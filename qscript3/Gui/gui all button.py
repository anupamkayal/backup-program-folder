import tkinter as Tk
root=Tk.Tk()
root.title("gui")
#----create label------#
from tkinter import ttk
label1=ttk.Label(root,text="enter your name")
label1.grid(row=1,column=1,sticky="w")
label2=ttk.Label(root,text="enter your email address")
label2.grid(row=2,column=1,sticky="w")
label3=ttk.Label(root,text="enter your age")
label3.grid(row=3,column=1,sticky="w")
#---entry box--#

value1=Tk.StringVar()
entrybox1=ttk.Entry(root, width=16,textvariable=value1)
entrybox1.grid(row=1,column=2)
value2=Tk.StringVar()
entrybox2=ttk.Entry(root, width=16,textvariable=value2)
entrybox2.grid(row=2, column=2)
value3=Tk.StringVar()
entrybox3=ttk.Entry(root, width=16,textvariable=value3)
entrybox3.grid(row=3, column=2)

#---radio button---#

   
radiovar1=Tk.StringVar()
radiobutton1=ttk.Radiobutton(root,text="male", value="male",variable="radiovar1")
radiobutton1.grid(row=4,column=1,sticky="w")
radio_var2=Tk.StringVar()
radiobutton2=ttk.Radiobutton(root,text="female" , value="female", variable="radio_var2 " )
radiobutton2.grid(row=4,column=2)

#----combobox---#
combo_var=Tk.StringVar()
combobox1=ttk.Combobox(root,width=14,textvariable=combo_var)
combobox1["values"]=("male",  "female" ,  "other"  )
combobox1.grid(row=5 ,column=1  )

#---checkbutton----#

check_var=Tk.IntVar()
checkbox1=ttk.Checkbutton(root, text="ascept terms and conditions",variable=check_var)
checkbox1.grid(row=6,columnspan=3,sticky="w")

#----button----#
def action():
	var1=entrybox1.get()
	var2=entrybox2.get()
	var3=entrybox3.get()
	print(f"name={var1},email={var2},age={var3}")
with open(file1.txt,"a") as file:
	file.a(var1,var2,var3)


entrybox1.delete(0,Tk.END)
entrybox2.delete(0,Tk.END)
entrybox3.delete(0,Tk.END)


submit=ttk.Button(root,text="submit", width=10 ,command=action  )
submit.grid(row=7,column=2)




root.mainloop()



