from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton,MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.toast import  toast
from kivymd.uix.dialog import  MDDialog
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
from kivy.config import Config
from kivy.core.text import LabelBase
#from jnius import cast
#from jnius import autoclass
Window.size=(480,800)


KV = '''

<CommonComponentLabel>
    halign: "center"

<Swiperitem@MDSwiperItem>:
    Image:
        source:'banner.jpg'
        radius:10
        size_hint:1,1
        



   

    


    

    

<MobileView>:
    name:"mobile"
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:

    MDSwiper:
        id:swiper
        size_hint_y:None
        height: root.height - toolbar.height - dp(500)
        y: root.height - self.height - toolbar.height - dp(5)
        
        Swiperitem:

        Swiperitem:

        Swiperitem:
    MDFloatLayout:
        id:float1
        padding:[0,0,0,0]
        spacing:"0dp"
        adaptive_height: True
        #size_hint_y:0.5
        height: root.height - swiper.height - toolbar.height-dp(10)
        md_bg_color:0.3,0.2,0.1,0
        ScrollView:
            size_hint: (1,0.8)
            
            pos_hint: {"center_x": 0.5, "top":1}

            MDGridLayout:
                id:grid
                cols:2
                padding:[10,10,10,10]
                spacing:"20dp"
                adaptive_height: True
                size_hint_y:None  
                md_bg_color:0.1,0.5,0.6,0
                MDIconButton:
                    on_release:root.abp_func()               
                    icon:"abp.png"           
                    rounded_button:False
                    icon_size:'66sp'
                    size_hint_y:None
                    height:"300dp"
                    size_hint_x:0.2        
                MDIconButton:
                    on_release:root.zee_func()               
                    icon:"zee24.png"           
                    rounded_button:False
                    icon_size:'66sp'
                    size_hint_y:None
                    height:"300dp"
                    size_hint_x:0.2        
                MDIconButton:
                    on_release:root.news18_func()              
                    icon:"News18.jpg"           
                    rounded_button:False
                    icon_size:'66sp'                        
                    size_hint_y:None
                    height:"300dp"
                    size_hint_x:0.2
                MDIconButton:
                    on_release:root.cn_func()                
                    icon:"cn.png"           
                    rounded_button:False
                    icon_size:'66sp'        
                    size_hint_y:None
                    height:"300dp"
                    size_hint_x:0.2
                MDIconButton:
                    on_release:root.kol_func()                
                    icon:"Kol.jpg"           
                    rounded_button:False
                    icon_size:'66sp'
                    size_hint_y:None
                    height:"300dp"
                    size_hint_x:0.2       
                MDIconButton:
                    on_release:root.newstime_func()               
                    icon:"News_Time.png"           
                    rounded_button:False
                    icon_size:'66sp'
                    size_hint_y:None
                    height:"300dp"
                    size_hint_x:0.2        
                MDIconButton:
                    on_release:root.tv9_func()              
                    icon:"TV9.jpg"           
                    rounded_button:False
                    icon_size:'66sp'
                    size_hint_y:None
                    height:"300dp"
                    size_hint_x:0.2        
                        
                       
                       
                
        

            

    
        



            MDBoxLayout:
                id: box
                orientation: "vertical"
                spacing: "12dp"
                pos_hint: {"top": 1}
                adaptive_height: True
                padding:[0,0,0,10]

                MDTopAppBar:
                    id:toolbar
                    type_height:'small'
                    title:"Total News"
                    opposite_colors:True
                    left_action_items:[['menu',lambda x:x,"Menu"]]
   

            
                  


<TabletView>
    CommonComponentLabel:
        text: "Tablet"
    AnchorLayout:
        anchor_x:"center"
        anchor_y:"center"
        
        MDBoxLayout:
            padding:[0,42,0,0]
            addaptive_width:True
            MDNavigationRail:
                id: navigation_rail
                md_bg_color: "#fffcf4"
                selected_color_background: "#e7e4c0"
                ripple_color_item: "#e7e4c0"
                
                bold:True
                markup:True
                on_item_release:root.item_func(*args)
                
                
                MDNavigationRailItem:
                    text: "Home"
                    icon: "home"
                    

                MDNavigationRailItem:
                    text: "Youtube-Tv"
                    icon: "youtube-tv"
                    

                MDNavigationRailItem:
                    text: "Web"
                    icon: "web"
                    

                MDNavigationRailItem:
                    text: "Settings"
                    icon: "star-settings"
                    markup:True
                    

                
                   
                    

    AnchorLayout:
        anchor_x:"center"
        anchor_y:"top"
        
        MDBoxLayout:
            id:box1
            adaptive_height: True
            md_bg_color: "#fffcf4"
            padding: "12dp"

            MDLabel:
                text: "12:00"
                adaptive_height: True
                pos_hint: {"center_y": .5}
    MDRelativeLayout:
        MDScreen:
            id:contented
            name:"content"
            md_bg_color:(62.0/255.0, 56.0/255.0, 50.0/255.0, 0.06)
            radius:[18,0,0,0]
            size_hint_x:0.943
            size_hint_y:0.95
            pos_hint:{'x':0.07,'top':0.93}
            #padding:[50,0,0,0]
            MDFloatLayout:

                MDLabel:
                    text:"Bengali News"
                    font_style:"H4"
                    pos_hint:{"x":0.03,"y":0.45}
                    font_name:"AovelSansRounded-rdDL.ttf"
                    valign:"top"
            
                MDGridLayout:
                    cols:6
                    size_hint:1,0.5
                    spacing: "50dp"              
                    padding:[30,0,10,10]
                    #md_bg_color:0.1,0.3,0.4,1
                    pos_hint:{"center_x":0.5,"center_y":0.65}
                    MDIconButton:
                        on_release:root.abp_func()               
                        icon:"abp.png"           
                        rounded_button:False
                        icon_size:'66sp'
                        pos_hint:{"center_y":0.8}                   
                    MDIconButton:
                        on_release:root.zee_func()                   
                        icon:"zee24.png"                
                        rounded_button:False
                        icon_size:'66sp'
                        pos_hint:{"center_y":0.8}
                    MDIconButton:
                        on_release:root.news18_func()  
                        icon:'News18.jpeg'
                        rounded_button:False
                        icon_size:'66sp'
                        pos_hint:{"center_y":0.8}
                    MDIconButton:  
                        on_release:root.cn_func()                
                        icon:"cn.png"                 
                        rounded_button:False
                        icon_size:'66sp'
                        pos_hint:{"center_y":0.8}
                    MDIconButton:
                        on_release:root.tv9_func()  
                        icon:"TV9.jpg"             
                        rounded_button:False
                        icon_size:'66sp'
                        pos_hint:{"center_y":0.8}
                    MDIconButton:
                        on_release:root.kol_func()  
                        icon:"Kol.jpg"                    
                        rounded_button:False
                        icon_size:'66sp'
                        pos_hint:{"center_y":0.8}
                    MDIconButton:
                        on_release:root.newstime_func()  
                        icon:"News_Time.png"
                        type:"standard"                   
                        rounded_button:False
                        icon_size:'66sp'
                        pos_hint:{"center_y":0.8}
                    MDIconButton:
                        icon:"pencil"
                        type:"standard"
                        theme_icon_color:"Custom"
                        md_bg_color:"#f8d7e3"
                        icon_color:"#311021"
                        rounded_button:False
                        icon_size:'66sp'
                        pos_hint:{"center_y":0.8}

<DesktopView>
    CommonComponentLabel:
        text: "Desktop"
    AnchorLayout:
    	anchor_x:"center"
        anchor_y:"center"
        
        MDBoxLayout:
        	padding:[0,42,0,0]
        	addaptive_width:True
            MDNavigationRail:
                id: navigation_rail
                md_bg_color: "#fffcf4"
                selected_color_background: "#e7e4c0"
                ripple_color_item: "#e7e4c0"
                
                bold:True
                markup:True
                on_item_release:root.item_func(*args)
                
                
                MDNavigationRailItem:
        			text: "Home"
        			icon: "home"
                    

                MDNavigationRailItem:
                    text: "Youtube-Tv"
                    icon: "youtube-tv"
                    

                MDNavigationRailItem:
                    text: "Web"
                    icon: "web"
                    

                MDNavigationRailItem:
                    text: "Settings"
                    icon: "star-settings"
                    markup:True
                    

                
                   
                    

    AnchorLayout:
        anchor_x:"center"
        anchor_y:"top"
        
        MDBoxLayout:
        	id:box1
            adaptive_height: True
            md_bg_color: "#fffcf4"
            padding: "12dp"

            MDLabel:
                text: "12:00"
                adaptive_height: True
                pos_hint: {"center_y": .5}
    MDScreen:
        
        id:contented
        name:"content"
        md_bg_color:(62.0/255.0, 56.0/255.0, 50.0/255.0, 0.06)
        radius:[18,0,0,0]
        size_hint_x:0.943
        size_hint_y:0.95
        pos_hint:{'right':1,'top':0.95}

        MDFloatLayout:

            MDLabel:
                text:"Bengali News"
                font_style:"H4"
                pos_hint:{"x":0.03,"y":0.45}
                font_name:"AovelSansRounded-rdDL.ttf"
                valign:"top"
            
            MDBoxLayout:
                orientation:"horizontal"
                size_hint:1,0.5
                spacing: "50dp"              
                padding:[30,0,10,10]
                #md_bg_color:0.1,0.3,0.4,1
                pos_hint:{"center_x":0.5,"center_y":0.65}
                MDIconButton:
                    on_release:root.abp_func()               
                    icon:"abp.png"           
                    rounded_button:False
                    icon_size:'66sp'
                    pos_hint:{"center_y":0.8}                   
                MDIconButton:
                    on_release:root.zee_func()                   
                    icon:"zee24.png"                
                    rounded_button:False
                    icon_size:'66sp'
                    pos_hint:{"center_y":0.8}
                MDIconButton:
                    on_release:root.news18_func()  
                    icon:'News18.jpeg'
                    rounded_button:False
                    icon_size:'66sp'
                    pos_hint:{"center_y":0.8}
                MDIconButton:  
                    on_release:root.cn_func()                
                    icon:"cn.png"                 
                    rounded_button:False
                    icon_size:'66sp'
                    pos_hint:{"center_y":0.8}
                MDIconButton:
                    on_release:root.tv9_func()  
                    icon:"TV9.jpg"             
                    rounded_button:False
                    icon_size:'66sp'
                    pos_hint:{"center_y":0.8}
                MDIconButton:
                    on_release:root.kol_func()  
                    icon:"Kol.jpg"                    
                    rounded_button:False
                    icon_size:'66sp'
                    pos_hint:{"center_y":0.8}
                MDIconButton:
                    on_release:root.newstime_func()  
                    icon:"News_Time.png"
                    type:"standard"                   
                    rounded_button:False
                    icon_size:'66sp'
                    pos_hint:{"center_y":0.8}
                MDIconButton:
                    icon:"pencil"
                    type:"standard"
                    theme_icon_color:"Custom"
                    md_bg_color:"#f8d7e3"
                    icon_color:"#311021"
                    rounded_button:False
                    icon_size:'66sp'
                    pos_hint:{"center_y":0.8}
                    
                    
            
            
        
            
            
            
                
            
                
                
                
                
                
                



    

ResponsiveView:
'''


class CommonComponentLabel(MDLabel):
    pass


class MobileView(MDScreen):
    def __init__(self,**kwargs):
        
        super().__init__()

        print(type(self))

        
    def on_enter(self):
        print("jgjhgjhk")

    def item_func(self,idse,item):
        
        self.item=item
        print(self.item.text)
    def abp_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@abpanandatv/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
    def zee_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@Zee24Ghanta/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def news18_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('https://www.youtube.com/@News18Bangla/streams')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@abpanandatv/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def cn_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/c/CalcuttaNewsAKD/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def tv9_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/c/TV9BanglaLive/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def kol_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@NewsTimeBangla/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def newstime_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@NewsTimeBangla/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()


class TabletView(MDScreen):
    def item_func(self,idse,item):
        
        self.item=item
        print(self.item.text)
    def abp_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@abpanandatv/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
    def zee_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@Zee24Ghanta/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def news18_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('https://www.youtube.com/@News18Bangla/streams')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@abpanandatv/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def cn_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/c/CalcuttaNewsAKD/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def tv9_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/c/TV9BanglaLive/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def kol_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@NewsTimeBangla/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def newstime_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@NewsTimeBangla/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()


class DesktopView(MDScreen):
    def item_func(self,idse,item):
        
        self.item=item
        print(self.item.text)
    def abp_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@abpanandatv/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
    def zee_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@Zee24Ghanta/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def news18_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('https://www.youtube.com/@News18Bangla/streams')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@abpanandatv/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def cn_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/c/CalcuttaNewsAKD/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def tv9_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/c/TV9BanglaLive/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def kol_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@NewsTimeBangla/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
        
    def newstime_func(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.youtube.com/@NewsTimeBangla/streams'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class Test(MDApp):
    
    def build(self): 
        self.theme_cls.material_style="M3"       
        return Builder.load_string(KV)
    def abp_func(self):
        print('gjhgjh')
    '''
    def on_start(self):
        print(dir(Box))
        
        self.obj=self.root.mobile_view.ids.contentbox
        for i in range(10):
            box1=MDBoxLayout(orientation="horizontal",adaptive_height= True ,spacing= "6dp",padding= [0, 0, 0, 0],pos_hint= {"center_x": .5,"center_y":0.5},md_bg_color=(0.2,0.1,0.3,1))
            box1.add_widget(MDIconButton(icon="abp.png",icon_size='66sp',size_hint=(1,1) ))
            box1.add_widget(MDIconButton(icon="abp.png",icon_size='66sp',size_hint=(1,1) ))
            Card.add_widget(self=self.obj,widget=box1)

            #self.btn=MDIconButton(icon="abp.png",icon_size='66sp',size_hint=(0.5,1) )
            #Box.add_widget(Card(),self.btn)
            #Box.add_widget(Card(),MDIconButton(icon="abp.png",icon_size='66sp',size_hint=(0.5,1) ))
            self.root.mobile_view.ids.contentbox.add_widget(Card())
    '''
            
            
    

    
LabelBase.register(name='nasalization-rg',fn_regular='./nasalization-rg.ttf')
Test().run()



