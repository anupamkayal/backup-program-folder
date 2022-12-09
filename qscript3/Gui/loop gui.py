import tkinter as tk
root=tk.Tk()
root.title("loop gui")
root.geometry("600x600")
from tkinter import ttk
list1=["enter name","age","email"]
for i in range (len(list1)):
	object=len(list1)+i
	label_var=tk.StringVar()
	label1=ttk.Label(root,text="object",textvariable=label_var  )
	label1.grid(row=0,column=0,sticky="w")
root.mainloop()
