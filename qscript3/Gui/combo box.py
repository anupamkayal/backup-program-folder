from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("700x400")
var=StringVar()
combobox=ttk.Combobox(root,width=15,values=("apple","banana"),textvariable=var,state="readonly")
combobox.current(1)
combobox.pack()



root.mainloop()
