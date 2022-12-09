import tkinter as tk
from PIL import Image
root=tk.Tk()
root.title("newspaper")
root.geometry("700x1230")
label_box=tk.Label(root)
     # (side="top",fill="both",anchor="ne",borderwidth="5")
img=Image.open(file=r"/storage/emulated/0/DCIM/Screenshots/IMG_20200504_154406.jpg")
main_photo=tk.PhotoImage(file=r"/storage)emulated/0/Screenshots/IMG_2")
label_box.pack() 
root.mainloop()



