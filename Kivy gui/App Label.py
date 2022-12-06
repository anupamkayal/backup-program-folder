from kivymd.app import MDApp
from kivymd.uix.label import  MDLabel
from kivymd.font_definitions  import theme_font_styles


class  MobileApp(MDApp):
    def build(self):
        label1=MDLabel(text="hay baby",halign="center",theme_text_color="Custom",text_color=(0,0,1,1))
        return label1

MobileApp().run()
#print(help(kivymd.uix.label))






