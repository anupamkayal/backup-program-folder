import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import  Button
class kivyClass(App):
    def build(self):
        return Button()
        

if __name__=="__main__":
    kivyClass().run()
   # print(help(kivy.uix.button))
