import tkinter as tk
root=tk.Tk()
from tkinter import ttk
root.title("manu bar")
manubar=tk.Menu(root)
nb=ttk.Notebook(root)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text="abcd")
nb.add(page2,text="xyz")
root.config(menu="manubar")
#labelframe=tk.frame(root)
#labelframe.grid(row=1, column=5)

root.mainloop()



