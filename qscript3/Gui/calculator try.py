from tkinter import *
import math 
root=Tk()
root.title("calculator")
root.geometry("700x850")
root.configure(bg='#463155')
def func(event):
	global screenvar
	try:
	   var=event.widget.cget("text")
	   print(var)
	   	   	       
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
        x=int(screenvar.get())
        sin=math.sin(x)
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
        f=int(screenvar.get())
        factorial=math.factorial(f)
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
        x=(int(screenvar.get()))
        radius=math.radians(x)
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
button_power=Button(root,text="^",width=1)
button_power.place(x=127,y=678)
button_power.bind("<Button-1>",func)
button_comma=Button(root,text=",",width=1)
button_comma.place(x=244,y=678)
button_comma.bind("<Button-1>",func)
button_radius=Button(root,text="radians",width=3)
button_radius.place(x=12,y=778)
button_radius.bind("<Button-1>",func_radius)
button_sin=Button(root,text="sin",width=1)
button_sin.place(x=152,y=778)
button_sin.bind("<Button-1>",func_sin)
button_cos=Button(root,text="cos",width=1)
button_cos.place(x=264,y=778)
button_cos.bind("<Button-1>",func_cos)
button_factor=Button(root,text="factorial",width=5)
button_factor.place(x=349,y=88)
button_factor.bind("<Button-1>",func_factorial)
button_sqrt=Button(root,text="sqrt",width=3)
button_sqrt.place(x=542,y=88)
button_sqrt.bind("<Button-1>",func_sqrt)
button_tan=Button(root,text="tan",width=3)
button_tan.place(x=362,y=178)
button_tan.bind("<Button-1>",func_tan)
button_log=Button(root,text="log",width=3)
button_log.place(x=542,y=178)
button_log.bind("<Button-1>",func_log)
button_deg=Button(root,text="degree",width=3)
button_deg.place(x=362,y=278)
button_deg.bind("<Button-1>",func_degree)

button_pi=Button(root,text="π",width=3)
button_pi.place(x=542,y=278)
button_pi.bind("<Button-1>",func_pi)



if __name__=='__main__':
	try:
		root.mainloop()
	except:
		import sys
		exc_type,exc_value,exc_traceback=sys.exc_info()
		with open('/storage/emulated/0/error_app.txt','a+') as f:			
			f.write(f'{exc_type}\n{exc_value}\n{exc_traceback}')
	
