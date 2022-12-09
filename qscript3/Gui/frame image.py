from tkinter import *
from PIL import ImageTk, Image#This creates the main window of an application
window = Tk()
window.title("Join")
window.geometry("767x345")
window​.​configure(​background=​'grey'​)
path = r"/storage/emulated/0/WhatsApp/Media/WhatsApp Images/IMG-20200603-WA0002.jpg."#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk​.​PhotoImage​(​Image​.​open​(​path​))​#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(window, image = img)#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")#Start the GUI
window.mainloop()