from  kivy.app import  App
from kivy.uix.layout import Layout

class Mygridlayout(App):
    pass
    
class  LayoutApp(App):
    def build(self):
        return Mygridlayout()
        
LayoutApp().run()