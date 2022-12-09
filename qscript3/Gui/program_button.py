from  kivy.app import App
from kivy.uix.widget import Widget
 
 
class  Gamebutton(Widget):
    pass
    
class  GameApp(App):
    def build(self):
        return Gamebutton()
        
GameApp().run()