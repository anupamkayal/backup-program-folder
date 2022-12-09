from tkinter import *
root=Tk()
root.title("calculator")
root.geometry("400x750")
def func(event):
	global screenvar
	try:
	   var=event.widget.cget("text")
	   print(var)

	   if var=="=":
	       if screenvar.get().isdigit():
	           value=int(screenvar.get())
	         
	       else:
		       value=eval(screenvar.get())
		       screenvar.set(value)
		       screen.update()
	   elif var=="C":
	        screenvar.set(" ")
	        screen.update()	   	  
	    	    
	   else:
	        number=screenvar.set(screenvar.get()+var)
	        screen.update()
	        screen.icursor(END)
	except:
	      screenvar.set("syntax error")
	      
def func_del(event):
    lenth=len(screenvar.get())
    screen.delete(lenth-1,END)
    #if lenth==1:
       # screen.insert(0,"0")
       


screenvar=StringVar()
screenvar.set(" ")
screen=Entry(root,text="text",width=29,textvariable=screenvar,font="Helvetica  12  bold")
screen.focus_set()
screen.pack(side=TOP, fill=X,ipady=12)
button1=Button(root,text="1",width=1)
button1.place(x=12,y=88)
button1.bind("<Button-1>",func)
button2=Button(root,text="2",width=1)
button2.place(x=126,y=88)
button2.bind("<Button-1>",func)
button3=Button(root,text="3",width=1)
button3.place(x=240,y=88)
button3.bind("<Button-1>",func)
button4=Button(root,text="4",width=1)
button4.place(x=12,y=178)
button4.bind("<Button-1>",func)
button5=Button(root,text="5",width=1)
button5.place(x=126,y=178)
button5.bind("<Button-1>",func)
button6=Button(root,text="6",width=1)
button6.place(x=242,y=178)
button6.bind("<Button-1>",func)
button7=Button(root,text="7",width=1)
button7.place(x=12,y=278)
button7.bind("<Button-1>",func)
button8=Button(root,text="8",width=1)
button8.place(x=126,y=278)
button8.bind("<Button-1>",func)
button9=Button(root,text="9",width=1)
button9.place(x=244,y=278)
button9.bind("<Button-1>",func)
button0=Button(root,text="0",width=1)
button0.place(x=12,y=378)
button0.bind("<Button-1>",func)
buttonplus=Button(root,text="+",width=1)
buttonplus.place(x=126,y=378)
buttonplus.bind("<Button-1>",func)
buttonminus=Button(root,text="-",width=1)
buttonminus.place(x=244,y=378)
buttonminus.bind("<Button-1>",func)
buttonmultiply=Button(root,text="*",width=1)
buttonmultiply.place(x=12,y=478)
buttonmultiply.bind("<Button-1>",func)
buttondiv=Button(root,text="/",width=1)
buttondiv.place(x=126,y=478)
buttondiv.bind("<Button-1>",func)
button_equal=Button(root,text="=",width=1)
button_equal.place(x=244,y=478)
button_equal.bind("<Button-1>",func)
button_clear=Button(root,text="C",width=1)
button_clear.place(x=12,y=578)
button_clear.bind("<Button-1>",func)
button_point=Button(root,text=".",width=1)
button_point.place(x=126,y=578)
button_point.bind("<Button-1>",func)
buttonexit=Button(root,text="Exit",width=1,command=root.destroy)
buttonexit.place(x=244,y=578)

button_del=Button(root,text="del",width=1)
button_del.place(x=12,y=678)
button_del.bind("<Button-1>",func_del)


root.mainloop()
