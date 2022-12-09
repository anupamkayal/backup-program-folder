from tkinter import  *

root=Tk()
root.wm_title("The Eternal City")
img = PhotoImage(file=r'/storage/emulated/0/qscript3/Text-plus.ico')
root.tk.call('wm', 'iconphoto', root._w, img)
#root.wm_iconbitmap(root, resource_filename(" /storage/emulated/0/Download/Text-plus.ico  ", "/storage/emulated/0/Download/Text-plus.ico"))
root.mainloop()

