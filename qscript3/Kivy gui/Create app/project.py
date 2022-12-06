from kivy.config import Config
Config.set('kivy','log_dir','/storage/emulated/0/.kivy/logs/')
from kivymd.app import  MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager,SlideTransition       
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.animation import Animation
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.uix.behaviors import ToggleButtonBehavior
from kivymd.uix.button import  MDIconButton
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import  requests
import json	
import concurrent.futures
from kivy.clock import Clock,mainthread
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.banner import MDBanner
from kivy.metrics import dp
from kivymd.uix.list import MDList,OneLineIconListItem
from kivy.properties import *
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.button import MDFloatingActionButton
import os
from kivymd.uix.filemanager import MDFileManager
from datetime import  datetime,date
import re
from kivy.properties import  *
from kivymd.uix.textfield import MDTextField
import threading
from kivymd.utils import  asynckivy
import random
from jnius import cast
from jnius import autoclass
from plyer import filechooser
import plyer
import pyrebase
from PIL import Image 
#from kivmob import  *
from kivy.base import EventLoop           
from kivy.app import  App
from android.runnable import run_on_ui_thread

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

url='https://user-data-39d9f-default-rtdb.firebaseio.com/.json'
auth='kyhXIS9w7Zu1j80j7SgG1ElflTWis0KLGr4YkMd4'

total_coin='0'

user_email=' '

config={
"apiKey": "AIzaSyD831yLZwF8d_Hw9qktC3AG7eHlto7zI8M",
"authDomain": "user-data-39d9f.firebaseapp.com",
"databaseURL": "https://user-data-39d9f-default-rtdb.firebaseio.com",
"projectId": "user-data-39d9f",
"storageBucket": "user-data-39d9f.appspot.com",
"messagingSenderId": "864339125441",
"appId": "1:864339125441:web:d4210e06cd6ed59323e040",
"measurementId": "G-PL70R27DMX"}

firebase=pyrebase.initialize_app(config)


Color = autoclass("android.graphics.Color")
WindowManager = autoclass('android.view.WindowManager$LayoutParams')
activity = autoclass('org.kivy.android.PythonActivity').mActivity





class IconToggleButton(ToggleButtonBehavior, MDIconButton):
	def __init__(self, **kwargs):
		super(IconToggleButton, self).__init__()


class Content(BoxLayout):
	pass
class Content1(BoxLayout):
	pass
class ScreenManagerClass(ScreenManager):
	wallet_Id=ObjectProperty(None)																																																																																																																																																																																																																			
class Registration_Screen(Screen):
	
	def __init__(self,**kwargs):
		self.statusbar_color("#b468ee")
		super(Registration_Screen,self).__init__()
	@run_on_ui_thread
	def statusbar_color(self,color):
		window = activity.getWindow()
		window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
		window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
		window.setStatusBarColor(Color.parseColor(color)) 
		#window.setNavigationBarColor(Color.parseColor(color))

		
	def keyboard(self):
		Window.bind(on_keyboard=self.back_click)
	def back_click(self,window,key,*largs):
		if key==27:
			self.manager.current='login_screen'
			return  True
	def show_password(self):
		password_id=self.manager.get_screen('registration_screen').ids.password_id.password
		if password_id==True:
			self.manager.get_screen('registration_screen').ids.password_id.password=False
		else:
			self.manager.get_screen('registration_screen').ids.password_id.password=True	
									
	def popup(self):
		
		self.dialog = MDDialog(
		size_hint=(0.86, None),
		auto_dismiss=False,
		type="custom",
		pos_hint={'center_x':0.5,'center_y':0.52},
		content_cls=Content(),
		
		)
		self.dialog.open()	


	def loading(self):
		self.popup()
		
		executor = concurrent.futures.ThreadPoolExecutor()													
		f2 = executor.submit(self.sign_up)
							
	@mainthread	
	def sign_up(self):
		name=self.manager.get_screen('registration_screen').ids.name.text
		number=self.manager.get_screen('registration_screen').ids.number.text
		email=self.manager.get_screen('registration_screen').ids.email.text   											
		password=self.manager.get_screen('registration_screen').ids.password_id.text
		reffer_code=self.manager.get_screen('registration_screen').ids.reffer.text
		Auth=firebase.auth()
		req=requests.get(url=url+'?auth='+auth)
		data=req.json()
		email_set=set()
		for key,value in data.items():
			email_set.add(key)
			
		if (len(name)==0) and (len(email)==0) and (len(password)==0) :
			self.dialog.dismiss()
			toast('Please fill all the field')
		elif email.replace('.','-')  in email_set:
			self.dialog.dismiss(force=True )
			snack=Snackbar(text='This Email has already been created...')
			snack.show()
			
		else:
			user=Auth.create_user_with_email_and_password(email,password)
				
			if (len(reffer_code)==0):
				sign_data=str({f'\"{email}\":{{"Name":\"{name}\","Number":\"{number}\","Password":\"{password}\","Coin":\"0\"}}'})
																			
			else:
				sign_data=str({f'\"{email}\":{{"Name":\"{name}\","Number":\"{number}\","Password":\"{password}\","Coin":\"100\"}}'})

			sign_data=sign_data.replace('.','-')
			sign_data=sign_data.replace("\'"," ")							
			json_file=json.loads(sign_data)
			requests.patch(url=url,json=json_file)
					
			Clock.schedule_once(self.registration_complete,4)
	def registration_complete(self,*args):		    
		self.dialog.dismiss(force=True )
		self.manager.current='login_screen'			                        				
		toast('Registration Successfull')

																																	
							
			
			
	def anim(self,widget):
		anim=Animation(pos_hint={'center_y':1.28})
		anim.start(widget)
	def anim1(self,widget):
		anim=Animation(pos_hint={'center_y':1.1})
		anim.start(widget)
	def anim2(self,widget):
		anim=Animation(opacity=0,pos_hint={'center_y':0.85})
		anim+=Animation(opacity=1,pos_hint={'center_y':0.93})		
		anim.start(widget)
	def anim3(self,widget):
		anim=Animation(opacity=0,duration=2.3)
		anim+=Animation(opacity=1)
		anim.start(widget)
	def anim4(self,widget):
		anim=Animation(opacity=0,duration=1.2)
		anim+=Animation(opacity=1)
		anim.start(widget)

class Login_Screen(Screen):

	def __init__(self,**kwargs):
		super(Login_Screen,self).__init__()
		
	
	def show_password(self):
		password_id=self.manager.get_screen('login_screen').ids.login_password.password
		if password_id==True:
			self.manager.get_screen('login_screen').ids.login_password.password=False
		else:
			self.manager.get_screen('login_screen').ids.login_password.password=True										
	
	def login(self):
		toast('please wait',2)
		login_email=self.manager.get_screen('login_screen').ids.login_email.text
		login_password=self.manager.get_screen('login_screen').ids.login_password.text
		req=requests.get(url=url+'?auth='+auth)
		data=req.json()
		email_set=set()			
		for key,value in data.items():
			email_set.add(key)							
		
		if (len(login_email)==0) and (len(login_password)==0) :			
			toast('Please enter email address and password',5)
		else:
			try:
				Auth=firebase.auth()
				Auth.sign_in_with_email_and_password(login_email,login_password)
				db=firebase.database()																											
				db.child(str(login_email.replace('.','-'))).update({"Password":str(login_password)})
				global user_email
				user_email=login_email
				self.manager.get_screen('main_screen').ids.navbar_label.text=data[login_email.replace('.','-')]['Name']
				self.manager.get_screen('main_screen').ids.nav_email.text=login_email														
				self.manager.get_screen('profile_screen').ids.name_field.text=data[login_email.replace('.','-')]['Name']
				self.manager.get_screen('profile_screen').ids.number_field.text=data[login_email.replace('.','-')]['Number']
				self.manager.get_screen('profile_screen').ids.email_field.text=login_email
				self.manager.get_screen('profile_screen').ids.email_field.disabled=True
				Source=self.manager.get_screen('main_screen').ids.avatar.source
				Profile_img=self.manager.get_screen('profile_screen').ids.profile_avatar
				with open('account.json','w+') as user_file:			
					user_file.write('{"'+str(login_email)+'"'+':{"Name":'+'"'+str(data[login_email.replace('.','-')]['Name'])+'"'+',"Number":'+'"'+str(data[login_email.replace('.','-')]['Number'])+'"'+',"Password":'+'"'+str(data[login_email.replace('.','-')]['Password'])+'"'+',"Source":'+'"'+str(Source)+'"'+',"Profile_img":'+'"'+str(Profile_img)+'"'+'}}')     						
		
				self.manager.get_screen('wallet_screen').ids.coin_num.text=data[login_email.replace('.','-')]['Coin']								
				toast('Login Successfull')
				self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')	
								
				self.manager.current='main_screen'
			except Exception as er :
				toast('Invalid Email & Password')
				print(er)
																					
		
	
	
	
	
	
class Forgot_Screen(Screen):
	def __init__(self,**kwargs):
		super(Forgot_Screen,self).__init__()
	def on_pre_enter(self):
		pass
		#main.ads.request_banner()
		#main.ads.show_banner()
	def keyboard(self):
		Window.bind(on_keyboard=self.back_click)
	def back_click(self,window,key,*largs):
		if key==27:
			self.manager.current='login_screen'
			return  True
	def anim(self,widget):
		anim=Animation(pos_hint={'center_y':1.20})
		anim.start(widget)
	def anim1(self,widget):
		anim=Animation(pos_hint={'center_y':0.93})
		anim.start(widget)
	def anim2(self,widget):
		anim=Animation(opacity=0,duration=2.3)
		anim+=Animation(opacity=1)
		anim.start(widget)
									
	def popup(self):
		
		self.dialog = MDDialog(
		size_hint=(0.86, None),
		auto_dismiss=True,
		type="custom",
		pos_hint={'center_x':0.5,'center_y':0.52},
		content_cls=Content1(),		
		)
		self.dialog.open()	

	
	def loading(self):
		self.popup()
		
		executor = concurrent.futures.ThreadPoolExecutor()													
		f2 = executor.submit(self.forgot_password)
							
	
	def forgot_password(self):
		Auth=firebase.auth()
		email_usser=self.ids.reset_passemail.text
		if email_usser==' ':
			toast('please enter email address')
		else:			
			
			Auth.send_password_reset_email(email_usser)
			self.dialog.dismiss(force=True )
			toast('email send successfully')
		



class Main_Screen(Screen):
	check=0
	#coin_num=ObjectProperty(None )
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		#self.rewards=Rewards_Handler(self)

	def hook_keyboard(self, window, key, *largs):
		count_key=0
		if key == 27:
			if count_key>1:
				App.stop(*largs)
			else:
				
				toast('press again to exit')
				count_key+=1
			
		else:
			return True
				
	#static method
	@staticmethod
	def show(obj):
		print(f'show func start{obj.ids.coin_num.text}')
		#print(obj.coin_num.text)
		global total_coin
		total_coin=str(int(total_coin)+25)
		print(f'after addition{total_coin}')
		
		#obj.coin_num.update()
				
		
	def keyboard(self):
		Window.bind(on_keyboard=self.back_button)
	def back_button(self,window,key,*largs):
		count_key=0
		if key==27:			
			if count_key==1:
				self.get_running_app.stop()
			else:
				toast('press again to exit')
				count_key=1
	
						
		
	
		
	def load_video(self):
		pass
		#main.ads.load_rewarded_ad('ca-app-pub-3940256099942544/5224354917')		
		
			
	def on_enter(self):
		EventLoop.window.bind(on_keyboard=self.hook_keyboard)
	
		
		#main.ads.request_banner()
		#main.ads.show_banner()
		#main.ads.load_rewarded_ad('ca-app-pub-3940256099942544/5224354917')
		#main.ads.request_interstitial()  # Intersitial ads is loaded in memory
		
		#main.ads.set_rewarded_ad_listener(self.rewards)
		Main_Screen.points=self.manager.get_screen('wallet_screen').ids.coin_num.text
		
	
	
				
	def threading_func(self):
		t1=threading.Thread(target=self.show_interstitialad)
		#t2=threading.Thread(target=self.add_coin)
		t1.start()
		
	#	t2.start()
#		t2.join()
			
	def show_interstitialad(self,*args):
		#ScreenManagerClass().get_screen('wallet_screen').ids.coin_num.text='20'
		
		coin=self.manager.get_screen('wallet_screen').ids.coin_num.text
		print(type(coin))
		self.manager.get_screen('wallet_screen').ids.coin_num.text=str(int(coin)+2)
		toast('coin added')
		
		#print(Wallet_Screen().coin_num)
		#self.coin_num=Wallet_Screen().coin_num
		#print(self.coin_num)
	
		
		
		#main.ads.request_interstitial()  # Intersitial ads is loaded in memory		
		#main.ads.show_interstitial()
	def add_coin(self):
		Clock.schedule_once(self.show_interstitialad,0)
		
		print(Wallet_Screen().coin_num.text)
		toast('coin added')
		#coin=self.manager.get_screen('wallet_screen').ids.coin_num.text							
#		self.manager.get_screen('wallet_screen').ids.coin_num.text=str(int(coin)+2)		
		
	def nav_draw(self):
		#main.ads.hide_banner()	
		self.ids.nav_draw.set_state('open')
	
	def continuous_func(self):
		self.current_coin=self.manager.get_screen('wallet_screen').ids.coin_num.text
		self.email=user_email				
		if Main_Screen.check==0:
			Main_Screen.check=1	
			db=firebase.database()
			req=requests.get(url=url+'?auth='+auth)
			data=req.json()
			emailset=set()
			for i in data:
				emailset.add(i)
			if self.email.replace('.','-') in emailset:
				get_coin=data[self.email.replace('.','-')]['Coin']														
				self.manager.get_screen('wallet_screen').ids.coin_num.text=str(get_coin)
													
			db.child(str(self.email.replace('.','-'))).update({"Coin":str(self.current_coin)})

		else:
			db=firebase.database()																											
			db.child(str(self.email.replace('.','-'))).update({"Coin":str(self.current_coin)})

	def nav_home(self):
		self.ids.nav_draw.set_state('close')
								
	def share_func(self):
		try:
			PythonActivity=autoclass('org.kivy.android.PythonActivity')
			Intent=autoclass('android.content.Intent')
			String=autoclass('java.lang.String')
			intent=Intent()
			intent.setAction(Intent.ACTION_SEND)
			intent.setType('text/plain')
			intent.putExtra(Intent.EXTRA_TEXT,String('Check out this amezing cool apps \n https:\\\\www.mediafire.com'))
			chooser=Intent.createChooser(intent,String('Share Via...'))
			PythonActivity.mActivity.startActivity(chooser)
		except Exception as ex:
			self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
			self.dialog.open() 
		
	def privacy_policy(self):					
		try:
			PythonActivity=autoclass('org.kivy.android.PythonActivity')
			Intent=autoclass('android.content.Intent')
			Uri=autoclass('android.net.Uri')
			intent=Intent()
			intent.setAction(Intent.ACTION_VIEW)
			intent.setData(Uri.parse('https://policies.google.com/privacy'))
			currentActivity=cast('android.app.Activity',PythonActivity.mActivity)
			currentActivity.startActivity(intent)		
		except Exception as ex:
			self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
			self.dialog.open() 

	def logout(self):
		file_check=os.path.isfile('./account.json')
		self.manager.get_screen('profile_screen').ids.profile_avatar.source='upload.png'
		self.manager.get_screen('main_screen').ids.avatar.source='upload.png'
		if file_check==True:
			os.remove('./account.json')
			self.manager.current='login_screen'
		else:
			self.manager.current='login_screen'
			
#class Rewards_Handler(RewardedListenerInterface):
#	def __init__(self,mainclass):
#		self.mainObj = mainclass	
#	def on_rewarded(self, reward_name, reward_amount):
#		self.mainObj.points =str(int(self.mainObj.points)+int(reward_amount))  # in Sample ad unit default amount is 10
#		toast("User recieved 5 points")
#	def on_rewarded_video_ad_started(self):    # Reloading Ad
#		self.mainObj.load_video()
#	def on_rewarded_video_ad_completed(self):
#		self.on_rewarded("Points","5")
#	def on_rewarded_video_ad_closed(self):
#		self.mainObj.points = str(int(self.mainObj.points)+0)  

	
		

		
		
		
					

																			
					
		
class Wallet_Screen(Screen):
	
	
	def __init__(self,**kwargs):
		super(Wallet_Screen,self).__init__()
	def on_enter(self):
	
		
		#self.manager.get_screen('wallet_screen').ids.coin_num.text=self.coin_num.text
		pass
	def func(self,value,*args):
		print(value)
		self.ids.coin_num.text=value
		
		#main.ads.request_banner()
		#main.ads.show_banner()
	def continuous_func2(self):		
		current_coin=self.manager.get_screen('wallet_screen').ids.coin_num.text
		self.email=self.manager.get_screen('profile_screen').ids.email_field.text
		db=firebase.database()																								
		db.child(str(self.email.replace('.','-'))).update({"Coin":str(current_coin)})

	
	def keyboard(self):
		Window.bind(on_keyboard=self.back_click)
	def back_click(self,window,key,*largs):
		if key==27:
			self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')
			self.manager.current='main_screen'
			return  True
								
	def change_hint_text(self,checkbox, value):
		print(checkbox,value,checkbox.state)
		paytm_check=self.manager.get_screen('wallet_screen').ids.paytm_check
		gpay_check=self.manager.get_screen('wallet_screen').ids.gpay_check
		upi_check=self.manager.get_screen('wallet_screen').ids.upi_check
		withdraw_num=self.manager.get_screen('wallet_screen').ids.withdraw_num
		try:
			withdraw_num.max_text_length=10
		except:
			toast('only 10 digits')
		if gpay_check.active==True:
			withdraw_num.hint_text='Enter Gpay Number  '				
		elif upi_check.active==True:
			withdraw_num.hint_text='Enter Upi Id  '
			withdraw_num.input_filter=None	
			withdraw_num.max_text_length=1000
		else: 
			withdraw_num.hint_text='Enter Paytm Number  '
			try:
				withdraw_num.max_text_length=10
			except:
				toast('only 10 digits')
		
				
								
	def process_to_pay(self):		
		self.email=self.manager.get_screen('profile_screen').ids.email_field.text		
		payment_no=self.manager.get_screen('wallet_screen').ids.withdraw_num.text										
		coin_amount=self.manager.get_screen('wallet_screen').ids.points.text
		total_coin=self.manager.get_screen('wallet_screen').ids.coin_num.text
		withdraw_num=self.manager.get_screen('wallet_screen').ids.withdraw_num.hint_text
		
		now=datetime.now()
		date_time=now.strftime("%d/%m/%Y  %H:%M:%S")
		today=now.strftime("%d-%m-%Y")
		
		mode_list=['Paytm','Gpay','Upi']
		pay_mode=''
		for i in mode_list:
			if i in withdraw_num:
				pay_mode=i
				
		reqs=requests.get(url=url+'?auth='+auth)	
		data=reqs.json()
		key_set=set()
		for key,value in data.items():
			key_set.add(key)
		
		if (len(payment_no)) and (len(coin_amount))==0:
			toast('All field are required',3)
		elif (self.ids.paytm_check.active==False) and (self.ids.gpay_check==False) and (self.ids.upi_check.active==False):
			toast('Please select payment method')
		elif (today+'-'+str((self.email).replace('.','-'))+'-Wallet') in key_set:
			toast('You have already redeem today ',3)
		
		else:					
			if (int(coin_amount)) <= (int(total_coin)) and (int(coin_amount))>=500:
				
				db=firebase.database()
				
				remaining_coin=int(total_coin)-int(coin_amount)
	
				data={"Email":str(self.email),"Date & Time":date_time,"Total  Coin": int(total_coin),"Redeem Coin":coin_amount,"Payment Mode":pay_mode,"Payment Number":payment_no,"Remaining Coin":remaining_coin}											
				db.child(today+'-'+str((self.email).replace('.','-'))+'-Wallet').set(data)
				self.manager.get_screen('wallet_screen').ids.coin_num.text="0"
				self.manager.get_screen('wallet_screen').ids.coin_num.text=str(remaining_coin)
				
				toast('complete')
			else:
				print('total coin' ,total_coin)
				print('withdraw' ,coin_amount)
				
				toast('pass')
				
class func_coin():
	coin_Num=ObjectProperty(None)
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
	def coin_ad_func(self):
		print(self)
		#print(App.get_running_app().root)
		#self.coin_number=self.ids.coin_num.text
#		self.root.ids.wallet_screen_id.ids.coin_num.text=str(int(self.coin_number)+5)
#		toast('coin_added')
		obj=App.get_running_app().root.wallet_Id.coin_Num.text
		App.get_running_app().root.wallet_Id.coin_Num.text=str(int(obj)+20)
		toast('coin added')
			
						
			
			
			
			
				
						
class Profile_Screen(Screen):
	selection = ListProperty([])
	def __init__(self,**kwargs):
		super(Profile_Screen,self).__init__()
	def on_pre_enter(self):
		pass
		#main.ads.request_banner()
		#main.ads.show_banner()
	def keyboard(self):
		Window.bind(on_keyboard=self.back_click)
	def back_click(self,window,key,*largs):
		if key==27:
			self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')			
			self.manager.current='main_screen'
			return  True
	
	
	def anim1(self,widget):
		anim=Animation(pos_hint={'center_y':1},duration=0.55)
		anim.start(widget)
	def anim2(self,widget):
		anim=Animation(opacity=0,duration=0.66)
		anim+=Animation(opacity=1)
		anim.start(widget)
	def anim3(self,widget):
		anim=Animation(opacity=0,duration=0.46)
		anim+=Animation(opacity=1)
		anim.start(widget)
	def popup(self):		
		self.dialog1= MDDialog(
		size_hint=(0.8, None),
		auto_dismiss=True,
		type="custom",
		pos_hint={'center_x':0.5,'center_y':0.52},
		content_cls=Content(),
		)
		self.dialog1.open()	


	def loading(self):
		self.popup()
		
		executor = concurrent.futures.ThreadPoolExecutor()													
		f2 = executor.submit(self.profile_save)
							
	

	def profile_save(self):
		self.name=self.ids.name_field.text
		self.number=self.ids.number_field.text
		self.email=self.ids.email_field.text
		
		db=firebase.database()
		db.child(str(self.email.replace('.','-'))).update({"Name":self.name})
		db.child(str(self.email.replace('.','-'))).update({"Number":self.number})
		with open('./account.json','r+') as file1:
			data=json.load(file1)
		for key in data:
			json_user=data[key]
		with open('./account.json','w+') as account_file:
			account_file.write('{"'+str(key)+'"'+':{"Name":'+'"'+str(self.name)+'"'+',"Number":'+'"'+str(self.number)+'"'+',"Password":'+'"'+str(json_user['Password'])+'"'+',"Source":'+'"'+str(json_user['Source'])+'"'+',"Profile_img":'+'"'+str(json_user['Profile_img'])+'"'+'}}')     						
		
		self.dialog1.dismiss()
		toast('account updated')
#-----+++ File Manager++++-------
	
	
	def func(self):
		self.manager_open = False
		Window.bind(on_keyboard=self.events)
		self.file_manager = MDFileManager(exit_manager=self.exit_manager,select_path=self.select_path,)      				
		try:
			filechooser.open_file(on_selection=self.handle_selection,filters=["*jpg", "*png"])			
			
		except:
			self.file_manager_open()
	def handle_selection(self,selection):
		self.selection = selection
		self.manager.get_screen('main_screen').ids.avatar.source=selection
		self.ids.profile_avatar.source=selection         
		self.selected_file=(os.path.basename(selection))
		toast(self.selected_file)
		Clock.schedule_once(self.profile_pic,2)
            
	
	def file_manager_open(self):
		self.file_manager.show('/')  # output manager to the screen   
		
		self.manager_open = True
		toast('Use Our Inbuilt File Explorer')
            
            
	def select_path(self, path):      
		self.exit_manager()
		self.selected_file=(os.path.basename(path))
		file_stats = os.stat(path)
		file_size=(file_stats.st_size / (1024 * 1024))
		if file_size >=2.0:           
			file_list=self.selected_file.split('.')
			image = Image.open(path)   
			MAX_SIZE = (500, 500) 
			image.thumbnail(MAX_SIZE)             
			image.save('./'+str(file_list[0])+'.png')
			self.manager.get_screen('main_screen').ids.avatar.source='./'+str(file_list[0])+'.png'
			self.manager.get_screen('profile_screen').ids.profile_avatar.source='./'+str(file_list[0])+'.png'            
			toast(self.selected_file)
			Clock.schedule_once(self.profile_pic,2)
		else:
			self.manager.get_screen('main_screen').ids.avatar.source=path
			self.ids.profile_avatar.source=path           
			toast(self.selected_file)
			Clock.schedule_once(self.profile_pic,2)
            
	def profile_pic(self,*args):      
		toast('Profile picture uploaded')
		with open('account.json','r+') as file:
			data=json.load(file)
		for key in data:
			json_user=data[key]
		with open('./account.json','w+') as testfile:
			testfile.write('{"'+str(key)+'"'+':{"Name":'+'"'+str(json_user['Name'])+'"'+',"Number":'+'"'+str(json_user['Number'])+'"'+',"Password":'+'"'+str(json_user['Password'])+'"'+',"Source":'+'"'+str(self.manager.get_screen('main_screen').ids.avatar.source)+'"'+',"Profile_img":'+'"'+str(self.manager.get_screen('profile_screen').ids.profile_avatar.source)+'"'+'}}')     						
		self.selection.clear()
	def exit_manager(self,*args):
		self.manager_open=False
		self.file_manager.close()
	def events(self,instance,keyboard,keycode,text,modifiers):
		if keyboard in (1001,21):
			if self.manager_open:
				self.file_manager.back()
		return True        	
          
     
                 

	
					

class Password_Screen(Screen):
	def __init__(self,**kwargs):
		super(Password_Screen,self).__init__()
	def on_pre_enter(self):
		pass
		#main.ads.request_banner()
		#main.ads.show_banner()
		
	def keyboard(self):
		Window.bind(on_keyboard=self.back_click)
	def back_click(self,window,key,*largs):
		if key==27:
			self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')		
		
			self.manager.current='main_screen'
			return  True
	def anim1(self,widget):
		anim=Animation(pos_hint={'center_y':1},duration=0.66)
		anim.start(widget)
	def anim2(self,widget):
		anim=Animation(opacity=0,duration=0.69)
		anim+=Animation(opacity=1)
		anim.start(widget)
	def anim3(self,widget):
		anim=Animation(opacity=0,duration=0.48)
		anim+=Animation(opacity=1)
		anim.start(widget)
		
	def password_change(self):
		email=self.ids.email_pass.text
		if email==' ':
			toast('please enter email address')
		else:			
			Auth=firebase.auth()
			Auth.send_password_reset_email(email)			
			toast('Reset password email send successfully',3)
			Clock.schedule_once(self.auto_logout,3)

	def auto_logout(self,*args):
		file_check=os.path.isfile('./account.json')
		if file_check==True:
			os.remove('./account.json')
			self.manager.current='login_screen'
		else:
			self.manager.current='login_screen'
									


class Contact_Screen(Screen):
	def __init__(self,**kwargs):
		super(Contact_Screen,self).__init__()
	def on_pre_enter(self):
		pass
		#main.ads.request_banner()
		#main.ads.show_banner()
	def keyboard(self):
		Window.bind(on_keyboard=self.back_click)
	def back_click(self,window,key,*largs):
		if key==27:
			self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')
		
			self.manager.current='main_screen'
			return  True
	
	def anim1(self,widget):
		anim=Animation(pos_hint={'center_y':1},duration=0.55)
		anim.start(widget)
	def anim2(self,widget):
		anim=Animation(opacity=0,duration=0.51)
		anim+=Animation(opacity=1)
		anim.start(widget)
	def anim3(self,widget):
		anim=Animation(opacity=0,duration=.47)
		anim+=Animation(opacity=1)
		anim.start(widget)
	def popup(self):
		
		self.dialog1= MDDialog(
		size_hint=(0.7, None),
		auto_dismiss=True,
		type="custom",
		pos_hint={'center_x':0.5,'center_y':0.52},
		content_cls=Content1(),
		)
		self.dialog1.open()	


	def loading(self):
		self.popup()
		
		executor = concurrent.futures.ThreadPoolExecutor()													
		f2 = executor.submit(self.user_review)
							
	
	def user_review(self):
		sub_data=self.manager.get_screen('contact_screen').ids.sub_field.text
		body_data=self.manager.get_screen('contact_screen').ids.body_field.text
		with open('account.json','r+') as file:
			data=json.load(file)
		email=''
		for key in data:
			email=key
		
			
			
		with open(str(email)+'.txt','w+') as file:
			file.write(str(sub_data)+'\n\n'+str(body_data))
			
			
		
		storage=firebase.storage()
		put_on_server='User Review/'+str(email)+'/'+str((sub_data))+'.txt'
		put_on_local=str(email)+'.txt'
		storage.child(put_on_server).put(put_on_local)
		self.dialog1.dismiss()
		toast('send successfull')
		os.remove(str(email)+'.txt')
		
		
		


		
class About_Screen(Screen):
	def __init__(self,**kwargs):
		super(About_Screen,self).__init__()
	def on_pre_enter(self):
		pass
		#main.ads.request_banner()
		#main.ads.show_banner()
	def keyboard(self):
		Window.bind(on_keyboard=self.back_click)
	def back_click(self,window,key,*largs):
		if key==27:
			self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')
					
			self.manager.current='main_screen'
			return  True
	
	def back_main(self):
		self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')
	
		self.manager.current='main_screen'
	def facebook(self):		
		try:
			PythonActivity=autoclass('org.kivy.android.PythonActivity')
			Intent=autoclass('android.content.Intent')
			Uri=autoclass('android.net.Uri')
			intent=Intent()
			intent.setAction(Intent.ACTION_VIEW)
			intent.setData(Uri.parse('https://www.facebook.com/anupam.kayal.146'))
			currentActivity=cast('android.app.Activity',PythonActivity.mActivity)
			currentActivity.startActivity(intent)		
		except Exception as ex:
			self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
			self.dialog.open() 
	def whatsapp(self):
		try:
			PythonActivity=autoclass('org.kivy.android.PythonActivity')
			Intent=autoclass('android.content.Intent')
			Uri=autoclass('android.net.Uri')
			intent=Intent()
			intent.setAction(Intent.ACTION_VIEW)
			intent.setData(Uri.parse('https://wa.me/919163742623'))
			currentActivity=cast('android.app.Activity',PythonActivity.mActivity)
			currentActivity.startActivity(intent)		
		except Exception as ex:
			self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
			self.dialog.open() 
	def gmail(self):
		self.dialog = MDDialog(title='Info',text='anupamkayal35@gmail.com',buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
		self.dialog.open() 	
	def youtube(self):
		try:
			PythonActivity=autoclass('org.kivy.android.PythonActivity')
			Intent=autoclass('android.content.Intent')
			Uri=autoclass('android.net.Uri')
			intent=Intent()
			intent.setAction(Intent.ACTION_VIEW)
			intent.setData(Uri.parse('https://youtube.com/channel/UCnYwAFxj9LjaZewOrcIZGxg'))
			currentActivity=cast('android.app.Activity',PythonActivity.mActivity)
			currentActivity.startActivity(intent)		
		except Exception as ex:
			self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
			self.dialog.open() 

	def github(self):
		try:
			PythonActivity=autoclass('org.kivy.android.PythonActivity')
			Intent=autoclass('android.content.Intent')
			Uri=autoclass('android.net.Uri')
			intent=Intent()
			intent.setAction(Intent.ACTION_VIEW)
			intent.setData(Uri.parse('https://github.com/anupamkayal'))
			currentActivity=cast('android.app.Activity',PythonActivity.mActivity)
			currentActivity.startActivity(intent)		
		except Exception as ex:
			self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
			self.dialog.open() 
	def web(self):
		try:
			PythonActivity=autoclass('org.kivy.android.PythonActivity')
			Intent=autoclass('android.content.Intent')
			Uri=autoclass('android.net.Uri')
			intent=Intent()
			intent.setAction(Intent.ACTION_VIEW)
			intent.setData(Uri.parse('http://colourhub.rf.gd/?i=1'))
			currentActivity=cast('android.app.Activity',PythonActivity.mActivity)
			currentActivity.startActivity(intent)		
		except Exception as ex:
			self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
			self.dialog.open() 
		
class Reffer_Screen(Screen):
	count=0
	def __init__(self,**kwargs):
		super(Reffer_Screen,self).__init__()
	def on_pre_enter(self):
		pass
		#main.ads.request_banner()
		#main.ads.show_banner()

	def keyboard(self):
		Window.bind(on_keyboard=self.back_button)
	@mainthread
	def back_button(self,window,key,*largs):
		if key==27:
			self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')
				
			self.manager.current='main_screen'
		return  True
	
	def back_main(self):
		self.manager.get_screen('main_screen').ids.nav_draw.set_state('close')	
			
		self.manager.current='main_screen'		
	def add_reffer(self):	
			
		if Reffer_Screen.count==0:
			self.ids.text_field.text=' '
			Reffer_Screen.count=1			
			rn=random.sample(range(1000001),1000001)
			for i in rn:
				self.ids.text_field.text=str(i)
				self.ids.text_field.disabled=True
				break
		else:
			return True
	def copy(self):
		try:
			from kivy.core.clipboard import Clipboard
			text=self.ids.text_field.text
			Clipboard.copy(text)
			toast('Copied..')
		except:
			toast("Could not be copied to clipboard: "+text)
			pass					
	def share_func(self):
		text=self.ids.text_field.text
		try:
			PythonActivity=autoclass('org.kivy.android.PythonActivity')
			Intent=autoclass('android.content.Intent')
			String=autoclass('java.lang.String')
			intent=Intent()
			intent.setAction(Intent.ACTION_SEND)
			intent.setType('text/plain')
			intent.putExtra(Intent.EXTRA_TEXT,String(f'Check out this amezing cool earnings app \n https:\\\\www.mediafire.com .  use this reffer code {text}'))
			chooser=Intent.createChooser(intent,String('Share Via...'))
			PythonActivity.mActivity.startActivity(chooser)
		except Exception as ex:
			self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
			self.dialog.open() 
			
			


class ProjectApp(MDApp):
	#ads=KivMob('ca-app-pub-3940256099942544/3419835294')
	points=NumericProperty(0)
	
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
			
		
	def on_start(self):
		#from android.permissions import  request_permissions,Permission
#		request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

		login_file=os.path.isfile('./account.json')
		if login_file is True:
			with open('account.json','r+') as file:
				data=json.load(file)
			for key in data:
				json_user=data[key]
		
			self.root.get_screen('main_screen').ids.navbar_label.text=json_user['Name']
			self.root.get_screen('main_screen').ids.nav_email.text=key  		
			self.root.get_screen('profile_screen').ids.name_field.text=json_user['Name']
			self.root.get_screen('profile_screen').ids.number_field.text=json_user['Number']
			self.root.get_screen('profile_screen').ids.email_field.text=key
			self.root.get_screen('profile_screen').ids.email_field.disabled=True
			self.root.get_screen('profile_screen').ids.profile_avatar.source=json_user['Profile_img']
			self.root.get_screen('main_screen').ids.avatar.source=json_user['Source']
			self.root.get_screen('main_screen').ids.nav_draw.set_state('close')	
			self.root.transition.direction='right'		                                 		
			self.root.current='main_screen'
		else:				            
			self.root.current='login_screen'
			
	def build(self):
		#self.ads.new_banner('ca-app-pub-3940256099942544/630097811',False)
		
		#self.ads.new_interstitial('ca-app-pub-3940256099942544/1033173712')
	
		
		self.theme_cls=ThemeManager()
		self.theme_cls.theme_style='Light'
		self.theme_cls.ripple_color=(171.0/255.0,100.0/255.0,233.0/255.0,255.0/255.0)		
		self.theme_cls.bg_darkest
		
		#self.kv=Builder.load_file('/storage/emulated/0/qscript3/Kivy gui/Earn_img/main.kv')
#		return self.kv

	
	def change_theme(self):		
		self.theme_cls.theme_style='Dark' if self.theme_cls.theme_style=='Light' else  'Light'
	def video_func(self):
		func_coin().coin_ad_func()
		#self.coin_number=self.root.ids.wallet_screen_id.ids.coin_num.text
#		self.root.ids.wallet_screen_id.ids.coin_num.text=str(int(self.coin_number)+5)
#		toast('coin_added')

	
												
																				
if __name__=='__main__':
		
	ProjectApp().run()						
#	except:
#		import sys
#		exc_type,exc_value,exc_traceback=sys.exc_info()
#		with open('/storage/emulated/0/error_app.txt','a+') as f:			
#			f.write(f'{exc_type}\n{exc_value}\n{exc_traceback}')
#	
		
