
import kivymd
from kivymd.uix.screen import Screen
from  kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
import helpers
from kivy.lang import Builder


class  MyApp(MDApp):
    def build(self):
        self.theme_cls.palette="Yellow"
        screen=Screen()
        username=MDTextField(pos_hint={"center_x":0.5,"center_y":0.5},size_hint_x=None,width=600)
        
        

        screen.add_widget(username)
        return screen
        
        
        
MyApp().run()



