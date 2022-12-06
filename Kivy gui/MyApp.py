import  kivy
from kivy.uix.widget import Widget
from kivy.app import  App
class Mywidget(Widget):
    pass
    
    
class MyApp(App):
    def build(self):
        return Mywidget()
        
        
if __name__=="__main__":
    MyApp().run()
    
    
    