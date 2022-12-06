import kivy
from  kivy.app import  App
from kivy.uix.button import  Label


class  Laptop(App):
    def build(self):
        return Label(text="first kivi project")
if __name__=="__main__":
    Laptop().run()
   
 



