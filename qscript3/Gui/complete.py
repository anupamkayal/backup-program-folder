from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import colorchooser
import os     
root=Tk()
root.title("text editor")
img=PhotoImage(r"/storage/emulated/0/Download/Text-plus.ico ")
#root.tk.call("wm" ,"iconphoto",root._w, img)
root.geometry("120x800")

#----------------main menu-----------------
#-----------------end menu-------------------

main_menu=Menu(root)
#file menu image
new=PhotoImage(file=r"/storage/emulated/0/Icon/new.png") 
open=PhotoImage(file=r"/storage/emulated/0/Icon/open.png")
save=PhotoImage(file=r"/storage/emulated/0/Icon/save.png")
saveas=PhotoImage(file=r"/storage/emulated/0/Icon/save_as.png")
exit=PhotoImage(file=r"/storage/emulated/0/Icon/exit.png")
#edit menu image
copy=PhotoImage(file=r"/storage/emulated/0/Icon/copy.png")
cut=PhotoImage(file=r"/storage/emulated/0/Icon/cut.png")
paste=PhotoImage(file=r"/storage/emulated/0/Icon/paste.png")
clearall=PhotoImage(file=r"/storage/emulated/0/Icon/clear_all.png")
find=PhotoImage(file="/storage/emulated/0/Icon/find.png")

#view menu image
statesbar=PhotoImage(file=r"/storage/emulated/0/Icon/status_bar.png")
toolbar=PhotoImage(file=r"/storage/emulated/0/Icon/tool_bar.png")

#color theme image
light=PhotoImage(file=r"/storage/emulated/0/Icon/light_default.png")
lightplus=PhotoImage(file=r"/storage/emulated/0/Icon/light_plus.png")
dark=PhotoImage(file=r"/storage/emulated/0/Icon/dark.png")
monokai=PhotoImage(file=r"/storage/emulated/0/Icon/monokai.png")
nightblue=PhotoImage(file=r"/storage/emulated/0/Icon/night_blue.png")

#Bold image
bold=PhotoImage(file=r"/storage/emulated/0/Icon/bold.png")

#Itali image
itali=PhotoImage(file=r"/storage/emulated/0/Icon/italic.png")

#underline image
underlineimg=PhotoImage(file=r"/storage/emulated/0/Icon/underline.png")

#font_color image
font_colorimg=PhotoImage(file=r"/storage/emulated/0/Icon/font_color.png")

#align left
align_leftimg=PhotoImage(file=r"/storage/emulated/0/Icon/align_left.png")

#align_center
align_centerimg=PhotoImage(file=r"/storage/emulated/0/Icon/align_center.png")

#align_right
align_rightimg=PhotoImage(file=r"/storage/emulated/0/Icon/align_right.png")

file=Menu(main_menu,tearoff=False)

#function menubar
#variable
url=""

#file add_command
def file_func(event=None):
	global url
	url=""
	text_editor.delete(1.0,END)
file.add_command(label="New file",image=new,compound=LEFT,accelerator="ctrl+n",command=file_func)

#open function
	
def open_file(event=None):
    
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(r"url", 'r') as fr:
            text_editor.delete(1.0, END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    root.title(os.path.basename(url))    	    	

file.add_command(label="Open",image=open,compound=LEFT,accelerator="ctrl+o",command=open_file)
#save command
def save_file(event=None):
	global url
	try:
		if url:
		        f = open(url, "w",encoding="utf-8")
		        f.write(text_editor.get(1.0, END))
		        f.close()
		    
		    
		    
		    
		    
			#content=str(text_editor.get(1.0,END))
#			file2=open(r"url","w",encoding="utf-8") 
#			file2.write(content)
		else:
			url=filedialog.asksaveasfile(mode="w", defaultextension=".txt",title="save file",filetypes=(("text","*.txt"),("all file","*.*")))
			content2=text_editor.get(1.0,END)
			url.write(content2)
			url.close()
	except:
		return
	
	
file.add_command(label="Save",image=save,compound=LEFT,accelerator="ctrl+s",command=save_file)
#save as
def save_as_func(event=None):
	global url
	try: 
	     content1=text_editor.get(1.0,END)
	     url=filedialog.asksaveasfile(mode="w",defaultextension=".text",title="save as",filetypes=(("text file",".text"),("all file","*.*")))
	     url.write(content1)
	     url.close()
	except:
		return 

file.add_command(label="Save As",image=saveas,compound=LEFT,accelerator="Alt+s",command=save_as_func)

#exit function

text_change=True
def exit_func(event=None):
	global text_change,url
	try:
		if text_change is True:
		    message=messagebox.askyesnocancel("warning","Do you want to save this file :")
		    if message is True:
		        if url:
		            content4=text_editor.get(1.0,END)
		            with open (url,"w",encoding="utf-8") as file:
		                file.write(content4)
		                root.destroy()
		        else:
		            
		        
		            
		            content1=text_editor.get(1.0,END)
		            url=filedialog.asksaveasfile(mode="w",defaultextension=".text",title="save as",filetypes=(("text file",".text"),("all file","*.*")))
		            url.write(content1)
		            url.close()
	                
		            root.destroy()
		    elif message is False:
		        root.destroy()
		
		else:
		    if text_change is FALSE:
		        
		        root.destroy()
		    else:
		        root.destroy()
	except:
		return

file.add_command( label="Exit",image=exit,compound=LEFT,accelerator="ctrl+e", command=exit_func)
#edit menu
edit=Menu(main_menu,tearoff=False)
#edit add_command

edit.add_command( label="copy",image=copy,compound=LEFT,accelerator="ctrl+c",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="cut",image=cut,compound=LEFT,accelerator="ctrl+x",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="paste",image=paste,compound=LEFT,accelerator="ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Clear All",image=clearall,compound=LEFT,accelerator="alt+c",command=lambda:text_editor.delete(1.0,END))
#find function


def find_replace(event=None):             
    def find():          
        word = entry1.get()
        text_editor.tag_remove('match', '1.0', END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
                
     
    
    
    def replace():
        word=entry1.get()
        replace_word=entry2.get()
        content=text_editor.get(1.0,END)
        new_content=content.replace(word,replace_word)
        text_editor.delete(1.0, END)
        text_editor.insert(1.0,new_content)   
        
        
       
    
    #def find():
#        word=entry1.get()
#        text_editor.tag_remove("match",'1.0',END)
#        matchs=0
#        if word:
#            start_position = "1.0"
#            while True:
#                start_position = text_editor.search("matches", start_position, stopindex=END)
#                if  not start_position:
#                    break
#                end_position=f"{start_position}+{len(word)}"
#                text_editor.tag_add("match",start_position, end_position)
#                matchs += 1
#                start_position = end_position
#                text_editor.tag_config("match", foreground="red", background="yellow")

                                                             
                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        
    find_dialogue=Toplevel()
    find_dialogue.geometry("540x250+500+200")
    find_dialogue.title("Find")
    find_dialogue.resizable(0,0)
      
#fram for find and replace
    frame=LabelFrame(find_dialogue,text="find & replace")
    frame.pack(pady=20)
#label for find and replace
    label1=Label(frame,text="Find")
    label1.grid(row=0,column=0,padx=4,pady=4)
    label2=Label(frame,text="Replace")
    label2.grid(row=1,column=0,padx=4,pady=4)
#entrybox for find and replace

    entry1=Entry(frame,width=30)
    entry1.grid(row=0, column=1,padx=4,pady=4)
    value2=StringVar()
    entry2=Entry(frame,width=30,textvariable=value2)
    entry2.grid(row=1,column=1,padx=4,pady=4)
#button for find and replace
    find_button=Button(frame,text="Find",command=find)
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button=Button(frame,text="Replace",command=replace)
    replace_button.grid(row=2,column=1,padx=8,pady=4)
    find_dialogue.mainloop()





edit.add_command(label="Find",image=find,compound=LEFT,accelerator="ctrl+f",command=find_replace)


view=Menu(main_menu,tearoff=False)
#view add command

show_statesbar=BooleanVar()
show_statesbar.set(True)

def statesbar_func():
    global show_statesbar
    if show_statesbar:
        statesbar.pack_forget()
        show_statesbar=False
    else:
        statesbar.pack(side=BOTTOM, fill=X,anchor=W)
        show_statesbar=True
        
        
    
view.add_checkbutton(label="States Bar",image=statesbar, compound=LEFT,variable=show_statesbar,on=True,off=False,command=statesbar_func)
#toolbar

show_toolbar=BooleanVar()                               
show_toolbar.set(True)

def show_toolbar():
    global show_toolbar
    if show_toolbar:
        label1.pack_forget()
        show_toolbar=False      
    else:
        text_editor.pack_forget()
        statesbar.pack_forget()
        label1.pack(side=TOP,fill=X)
        text_editor.pack(fill=BOTH,expand=True)              
        statesbar.pack(side=BOTTOM,fill=X,anchor=W)
        show_toolbar=True

view.add_checkbutton(label="Toolbar",variable=show_toolbar,on=True,off=False,image=toolbar,compound=LEFT,command=show_toolbar)
#color theme
color_theme=Menu(main_menu,tearoff=False)

theme_select=StringVar()
color_dict = {
    'Light ' : ('#000000', '#ffffff'),
    'LightPlus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Monokai' : ('#d3b774', '#474747'),
    'NightBlue' :('#ededed', '#6b9dc2')
}



def change_colour():
    get_theme=theme_select.get()
    color_tuple=color_dict.get(theme_select)
    fg_color,bg_color=color_dict[0],color_dict[1]
    text_editor.config(foreground=fg_color,background=bg_color)
    
color_theme.add_radiobutton(label="Light",image=light,compound=LEFT,variable=theme_select,command=change_colour)



def change_colour():
    get_theme=theme_select.get()
    color_tuple=color_dict.get(theme_select)
    fg_color,bg_color=color_dict[1],color_dict[2]
    text_editor.config(foreground=fg_color,background=bg_color)
    
color_theme.add_radiobutton(label="Lightplus",image=lightplus, variable=theme_select,compound=LEFT,command=change_colour)

def change_colour():
    get_theme=theme_select.get()
    color_tuple=color_dict.get(theme_select)
    fg_color,bg_color=color_dict[2],color_dict[3]
    text_editor.config(foreground=fg_color,background=bg_color)
    

color_theme.add_radiobutton(label="Dark",image=dark,compound=LEFT, variable=theme_select,command=change_colour)

def change_colour():
    get_theme=theme_select.get()
    color_tuple=color_dict.get(theme_select)
    fg_color,bg_color=color_dict[3],color_dict[4]
    text_editor.config(foreground=fg_color,background=bg_color)
    

color_theme.add_radiobutton(label="Monokai",image=monokai,compound=LEFT, variable=theme_select,command=change_colour)

def change_colour():
    get_theme=theme_select.get()
    color_tuple=color_dict.get(theme_select)
    fg_color,bg_color=color_dict[4],color_dict[5]
    text_editor.config(foreground=fg_color,background=bg_color)
    

color_theme.add_radiobutton(label="NightBlue",image=nightblue,compound=LEFT,variable=theme_select,command=change_colour)
# about
aboutmenu=Menu(main_menu,tearoff=False)
def about():
    messagebox.showinfo("About","This is created by anupam")

aboutmenu.add_command(label="About Notepad",command=about)
#help 
def  help():
    messagebox.showinfo("Help","For any quries releted imformation\nplease! contact us at gmail\n(anupamkayal4@gmail.com)")
aboutmenu.add_command(label="Help",command=help)
#add.cascade
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Colour Theme",menu=color_theme)
main_menu.add_cascade(label="About",menu=aboutmenu)


root.config(menu=main_menu)


#----------------toolbar-----------------


label1=ttk.Label(root) 
label1.pack(side=TOP,fill=X)
#font
font_tuple=font.families()
var=StringVar()
combobox=ttk.Combobox(label1,width=23,textvariable=var,state="readonly") 
combobox['values']=font_tuple
combobox.current(font_tuple.index("Noto Sans Syriac Western"))
combobox.grid(row=0,column=0,padx=5)

#font size

var2=IntVar()
combobox2=ttk.Combobox(label1,width=4,textvariable=var2,state="readonly") 
combobox2["values"]=tuple(range(1,35))
combobox2.current(14)
combobox2.grid(row=0,column=1,padx=5)

button_bold=Button(label1,width=58,height=43,image=bold)
button_bold.grid(row=0,column=2,padx=5)

button_itali=Button(label1,width=58,height=43,image=itali)
button_itali.grid(row=0,column=3,padx=5)


underline_button=Button(label1,width=58,height=43,image=underlineimg)
underline_button.grid(row=0,column=4,padx=5)

font_color_button=Button(label1,width=58,height=43,image=font_colorimg)
font_color_button.grid(row=0,column=5,padx=6)

align_left_button=Button(label1,width=58,height=43,image=align_leftimg)
align_left_button.grid(row=0,column=6,padx=5)

align_center_button=Button(label1,width=58,height=43,image=align_centerimg)
align_center_button.grid(row=0,column=7,padx=5)

align_right_button=Button(label1,width=58,height=43,image=align_rightimg)
align_right_button.grid(row=0,column=8,padx=5)

#-----------------end toolbar-------------------
#----------------TEXT EDITOR bar-----------------
text_editor=Text(root)
text_editor.config(wrap="word",relief=SUNKEN)
text_editor.focus_set()
text_editor.pack(fill=BOTH,expand=True)



#--------------------scrollbar--------------
scrollbar=Scrollbar(text_editor)
scrollbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT,fill=Y)
#--------------------end scrollbar------------

#--------------------statesbar------------------

statesbar=Label(root,text="Ready",bd=1,relief=SUNKEN,anchor=W)
statesbar.pack(side=BOTTOM,fill=X)


#-----------------end statesbar-------------------

#----------------function-----------------

current_font="Noto Sans Syriac Western"
current_font_size=14

def change_font(event):
	global current_font
	
	current_font=var.get()
	text_editor.configure(font=(current_font,current_font_size))
 
def change_fontsize(event):
	global current_font_size
	
	current_font_size=var2.get()
	text_editor.configure(font=(current_font,current_font_size))

combobox.bind("<<ComboboxSelected>>" ,change_font)
combobox2.bind("<<ComboboxSelected>>", change_fontsize)

#bold function

def change_bold():
	variable=font.Font(font=text_editor["font"])
	if variable.actual()["weight"]=='normal':
		text_editor.configure(font=(current_font,current_font_size,"bold"))
	if variable.actual()["weight"]=='bold':
		text_editor.configure(font=(current_font,current_font_size,"normal"))
button_bold.configure(command=change_bold)		


# Italic function

def change_itali():
	variable=font.Font(font=text_editor["font"])
	if variable.actual()["slant"]=="italic":
		text_editor.configure(font=(current_font,current_font_size,"roman"))
	if variable.actual()["slant"]=="roman":
		text_editor.configure(font=(current_font,current_font_size,"italic"))
button_itali.configure(command=change_itali)

# underline function
def change_underline():
	variable2=font.Font(font=text_editor["font"])
	if variable2.actual()["underline"]==1:
		text_editor.configure(font=(current_font,current_font_size,"normal"))
	if  variable2.actual()["underline"]==0:
		text_editor.configure(font=(current_font,current_font_size,"underline"))
underline_button.configure(command=change_underline)

# font_color
def change_fontcolor():
	variable3=colorchooser.askcolor()
	text_editor.configure(fg=variable3[1])
font_color_button.configure(command=change_fontcolor)
	
#align_left
def align_left_func():
	text_content=text_editor.get(1.0,"end")
	text_editor.delete(1.0,END)
	text_editor.tag_config("left",justify=LEFT)
	text_editor.insert(INSERT,text_content,"left")

align_left_button.configure(command=align_left_func)

#align_center
def align_center():
	text_content=text_editor.get(1.0,"end")
	text_editor.tag_config("center",justify=CENTER)
	text_editor.delete(1.0,END)
	text_editor.insert(INSERT,text_content,"center")
align_center_button.configure(command=align_center)

#align right
def align_right():
	text_variable=text_editor.get(1.0,"end")
	text_editor.tag_config("right",justify=RIGHT)
	text_editor.delete(1.0,END)
	text_editor.insert(INSERT,text_variable,"right")
align_right_button.configure(command=align_right)


#-----------------end function-------------------

root.bind("<Control - n>", file_func)
root.bind("<Control - s>",save_file)
root.bind("<Control - Alt-s>",save_as_func)
root.bind("<Control - e>",exit_func)
root.bind("<Control - f> ",find_replace)


root.mainloop()


