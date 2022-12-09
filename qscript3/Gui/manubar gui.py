import tkinter as tk
root=tk.Tk()
root.title("menubar")
######main menu########$#
main_menu=tk.Menu(root)
#######file menu##########
file_menu=tk.Menu(main_menu)
#######new menu######₹₹#
file_menu.add_command(label="new")
file_menu.add_command(label="open")
main_menu.add_cascade(label="file" ,menu=file_menu  )
root.config(menu=main_menu)
root.mainloop()

