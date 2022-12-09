from tkinter import *
import math 
root=Tk()
root.title("calculator")
root.geometry("400x550")
root.resizable(1,1)
root.configure(bg='#463155')
def func(event):
	global screenvar
	try:
	   var=event.widget.cget("text")
	
	   	   	       
	   if var=="=":
	       if screenvar.get().isdigit():
	           value=int(screenvar.get())
	       data=screenvar.get()
	       for   i in data:
	               if i=="^":
	                   base,power=(screenvar.get()).split("^")
	                   powervar=math.pow(int(base),int(power))
	                   screenvar.set(powervar)
	                   screen.update()         
	               	           	           	           	           	          	         
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
try:
    def func_del(event):
        lenth=len(screenvar.get())
        screen.delete(lenth-1,END)
       #if lenth==1:
     # screen.insert(0,"0")
     
    def func_radius(event):
        x=(int(screenvar.get()))
        radius=math.radians(x)
        screenvar.set(radius)
        screen.update()
        screen.icursor(END)        
    def func_sin(event):
        p=int(screenvar.get())
        sin=math.sin(p)
        screenvar.set(sin)
        screen.update()
        screen.icursor(END)       
    def func_cos(event):
        y=int(screenvar.get())
        cos=math.cos(y)
        screenvar.set(cos)
        screen.update()
        screen.icursor(END)        
    def func_factorial(event):
        xf=int(screenvar.get())
        factorial=math.factorial(xf)
        screenvar.set(factorial)
        screen.update()
        screen.icursor(END)       
    def func_sqrt(event):
        s=int(screenvar.get())
        sqrt=math.sqrt(s)
        screenvar.set(sqrt)
        screen.update()
        screen.icursor(END)                                      
    def func_tan(event):
        i=(int(screenvar.get()))
        radius=math.radians(i)
        tan=math.tan(radius)
        screenvar.set(tan)
        screen.update()
        screen.icursor(END)        
    def func_log(event):
        l=int(screenvar.get())
        log=math.log(l)
        screenvar.set(log)
        screen.update()
        screen.icursor(END)
    def func_degree(event):
        deg=int(screenvar.get())
        #x=math.radians(deg)
        degree=math.degrees(deg)
        screenvar.set(degree)
        screen.update()
        screen.icursor(END)
    def func_pi(event):
        screen.insert(END,"22/7")
        
        
        
        
        
except ValueError as  ve:   
    screenvar.set(ve,"syntax error")       
except: 
    screenvar.set("syntax error")
    

checkvar=BooleanVar()
checkvar.set(False)
def func_menu():
    global checkvar
    if checkvar:
        frame1.place_forget()
        checkvar=False
        if checkvar==False:
                root.geometry("450x500")
    else:
        frame1.place(x=370,y=102,height=730,width=340)       
        checkvar=True
        if checkvar==True:
                root.resizable(1,1)
                root.geometry("700x500")
        
        
                                                                                                                        
main_menu=Menu(root)
calculator_menu=Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="calculator_menu",menu=calculator_menu)
calculator_menu.add_checkbutton(label="sciencetific calculator",variable=checkvar,on=True,off=False,command=func_menu)
root.config(menu=main_menu)
screenvar=StringVar()
screenvar.set(" ")
screen=Entry(root,text="text",width=29,textvariable=screenvar,font="Helvetica  12  bold")
screen.focus_set()
screen.pack(side=TOP,fill=X,ipady=12)
frame1=Frame(root,relief=SUNKEN)

frame=Frame(root,relief=SUNKEN,bg='#463155')
frame.place(x=0,y=102,height=730,width=344)
button1=Button(frame,text="1",activebackground="#564744")
button1.place(x=5,y=0,height=34,width=46)
button1.bind("<Button-1>",func)
button2=Button(frame,text="2", activebackground="#554446"  )
button2.place(x=116,y=0, height=34,width=46)
button2.bind("<Button-1>",func)
button3=Button(frame,text="3",width=1)
button3.place(x=240,y=0)
button3.bind("<Button-1>",func)
button4=Button(frame,text="4",width=1)
button4.place(x=0,y=100)
button4.bind("<Button-1>",func)
button5=Button(frame,text="5",width=1)
button5.place(x=116,y=100)
button5.bind("<Button-1>",func)
button6=Button(frame,text="6",width=1)
button6.place(x=240,y=100)
button6.bind("<Button-1>",func)
button7=Button(frame,text="7",width=1)
button7.place(x=0,y=200)
button7.bind("<Button-1>",func)
button8=Button(frame,text="8",width=1)
button8.place(x=116,y=200)
button8.bind("<Button-1>",func)
button9=Button(frame,text="9",width=1)
button9.place(x=240,y=200)
button9.bind("<Button-1>",func)
button0=Button(frame,text="0",width=1)
button0.place(x=0,y=300)
button0.bind("<Button-1>",func)
buttonplus=Button(frame,text="+",width=1)
buttonplus.place(x=116,y=300)
buttonplus.bind("<Button-1>",func)
buttonminus=Button(frame,text="-",width=1)
buttonminus.place(x=244,y=300)
buttonminus.bind("<Button-1>",func)
buttonmultiply=Button(frame,text="*",width=1)
buttonmultiply.place(x=0,y=400)
buttonmultiply.bind("<Button-1>",func)
buttondiv=Button(frame,text="/",width=1)
buttondiv.place(x=116,y=400)
buttondiv.bind("<Button-1>",func)
button_equal=Button(frame,text="=",width=1)
button_equal.place(x=244,y=400)
button_equal.bind("<Button-1>",func)
button_clear=Button(frame,text="C",width=1)
button_clear.place(x=0,y=500)
button_clear.bind("<Button-1>",func)
button_point=Button(frame,text=".",width=1)
button_point.place(x=116,y=500)
button_point.bind("<Button-1>",func)
buttonexit=Button(frame,text="Exit",width=1,command=root.destroy)
buttonexit.place(x=116,y=600)
button_del=Button(frame,text="del",width=1)
button_del.place(x=244,y=500)
button_del.bind("<Button-1>",func_del)
button_power=Button(frame,text="^",width=1)
button_power.place(x=0,y=600)
button_power.bind("<Button-1>",func)
button_comma=Button(frame1,text=",",width=1)
button_comma.place(x=244,y=778)
button_comma.bind("<Button-1>",func)
button_radius=Button(frame1,text="radians",width=3)
button_radius.place(x=0,y=0)
button_radius.bind("<Button-1>",func_radius)
button_sin=Button(frame1,text="sin",width=3)
button_sin.place(x=180,y=0)
button_sin.bind("<Button-1>",func_sin)
button_cos=Button(frame1,text="cos",width=3)
button_cos.place(x=0,y=100)
button_cos.bind("<Button-1>",func_cos)
button_factor=Button(frame1,text="factorial",width=5)
button_factor.place(x=177,y=100)
button_factor.bind("<Button-1>",func_factorial)
button_sqrt=Button(frame1,text="sqrt",width=3)
button_sqrt.place(x=0,y=200)
button_sqrt.bind("<Button-1>",func_sqrt)
button_tan=Button(frame1,text="tan",width=3)
button_tan.place(x=180,y=200)
button_tan.bind("<Button-1>",func_tan)
button_log=Button(frame1,text="log",width=3)
button_log.place(x=0,y=300)
button_log.bind("<Button-1>",func_log)
button_deg=Button(frame1,text="degree",width=3)
button_deg.place(x=180,y=300)
button_deg.bind("<Button-1>",func_degree)
button_pi=Button(frame1,text="π",width=3)
button_pi.place(x=0,y=400)
button_pi.bind("<Button-1>",func_pi)




root.mainloop()
