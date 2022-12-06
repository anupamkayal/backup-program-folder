import  kivymd 
from  kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.button import  MDFlatButton,MDFloatingActionButton
from kivymd.uix.button import  MDRectangleFlatButton



class  Myapp(MDApp):
    def  build(self):
        self.theme_cls.primary_palette="DeepPurple"
        self.theme_cls.primary_hue="600"  
        screen=Screen()
        button1=MDRectangleFlatButton(text="submit",pos_hint={"center_x":0.5,"center_y":0.5})
       
        button2=MDFlatButton(text="click here ",pos_hint={"center_x":0.22,"center_y":0.22})
        
        button3=MDFloatingActionButton(icon="whatsapp",pos_hint={"center_x":0.5,"center_y":0.5})
       
        screen.add_widget(button3)        
        return screen
        
        
if __name__=="__main__":
    Myapp().run()

#Button color:
#green,Pink,Purple,DeepPurple,Indigo,Blue,LightBlue,Cyan,Teal,Green,LightGreen,Lime,Yellow,Amber,Orange,DeepOrange,Brown,Gray,BlueGray

#Button hue:
 #   ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’,
#‘A400’, ‘A700’






