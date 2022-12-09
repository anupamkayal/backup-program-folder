from tkinter import *
root=Tk()
root.title("label font gui")
canvas_width="657"
canvas_height="560"
root.geometry(f"{canvas_width}x{canvas_height}")
canvas1=Canvas(root)
canvas1.create_line(0,40,80,40,fill="#353555")
canvas1.pack(side=TOP)
root.mainloop()