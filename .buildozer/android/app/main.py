from kivy.app import App
from kivy.config import Config 
Config.set('graphics', 'resizable', 1)
from kivy.core.window import Window
#Window.size = (470, 820)
from kivy.uix.image import Image
from kivy.core.window import Window 
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.carousel import Carousel
from kivy.properties import ObjectProperty
from kivy.uix.button import Button as btn
from kivy.uix.label import Label as lbl
from kivy.uix.floatlayout import FloatLayout as fl
from kivy.uix.gridlayout import GridLayout as gl
from kivy.uix.boxlayout import BoxLayout as bl
import sqlite3
import random
import time
from kivy.clock import Clock
from kivy.animation import Animation



class EraScreen(Screen):
#____________________________________________________________________________________
	i = 0.18
	b1, b2 = 2, 2
	b_x, b_y = -2.2, -0.43
	step = 0.2

	def animation(self, *arg):
		Clock.schedule_once(self.an_run, 1)

	def an_run(self,*args):
		#____left
		self.clock_up_1(self.an_off_I_L)
		self.clock_up_2(self.an_on_I_L1)
		self.clock_up_1(self.an_off_I_L1)
		self.clock_up_2(self.an_on_I_L)
		self.clock_up_1(self.an_off_I_L)		
		self.clock_up_2(self.an_on_I_L2)
		self.clock_up_1(self.an_off_I_L2)
		self.clock_up_2(self.an_on_I_L)
		self.clock_up_1(self.an_off_I_L)
		self.clock_up_2(self.an_on_I_L1)
		self.clock_up_1(self.an_off_I_L1)
		self.clock_up_2(self.an_on_I_L)
		self.clock_up_1(self.an_off_I_L)
		self.clock_up_2(self.an_on_I_L2)
		self.clock_up_1(self.an_off_I_L2)
		self.clock_up_2(self.an_on_I_L)
		self.clock_up_1(self.an_off_I_L)
		self.clock_up_2(self.an_on_I_L1)
		self.clock_up_1(self.an_off_I_L1)
		self.clock_up_2(self.an_on_I_L)
		self.clock_up_1(self.an_off_I_L)
		self.clock_up_2(self.an_on_I_L1)
		self.clock_up_1(self.an_off_I_L1)
		self.clock_up_2(self.an_on_I_F)	
		self.clock_up_1(self.an_off_I_F)
		self.clock_up_2(self.an_on_I_F_1)	
		self.clock_up_1(self.an_off_I_F_1)
		self.clock_up_2(self.an_on_I_F_UP)	


	def clock_up_1(self, a, *arg):
		k=self.b1*self.i
		Clock.schedule_once(a, k)
		self.b1 += 1

	def clock_up_2(self, a, *arg):
		k=self.b2*self.i
		Clock.schedule_once(a, k)
		self.b2 += 1



#-----------------------------build animation of all widgets on Screen
	def an_on_I_F(self, *arg):
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_F'])

	def an_off_I_F(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_F'])

	def an_on_I_F_1(self, *arg):
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_F_1'])

	def an_off_I_F_1(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_F_1'])

	def an_on_I_F_UP(self, *arg):
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_F_UP'])

	def an_off_I_F_UP(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_F_UP'])

	def an_on_I_L(self, *arg):
		self.b_x += self.step
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_L'])

	def an_off_I_L(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_L'])

	def an_on_I_L1(self, *arg):
		self.b_x += self.step
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_L1'])

	def an_off_I_L1(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_L1'])

	def an_on_I_L2(self, *arg):
		self.b_x += self.step
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_L2'])

	def an_off_I_L2(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_L2'])

	def an_on_I_R(self, *arg):
		self.b_x -= self.step
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_R'])

	def an_off_I_R(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_R'])

	def an_on_I_R1(self, *arg):
		self.b_x -= self.step
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_R1'])

	def an_off_I_R1(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_R1'])

	def an_on_I_R2(self, *arg):
		self.b_x -= self.step
		an = Animation(pos_hint={"x": self.b_x}, d = 0)
		an += Animation(color=[1,1,1,1], d = 0)
		an.start(self.ids['I_R2'])

	def an_off_I_R2(self, *arg):
		an = Animation(color=[0,0,0,0], d = 0)
		an.start(self.ids['I_R2'])


#____________________________________________________________________________________

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		Clock.schedule_once(self.changer, 10.45-2)
	
	def changer(self,*args):
		self.manager.current = 'menu'

	def animation_logo(self, *arg):
		Clock.schedule_once(self.animation)
		Clock.schedule_once(self.animation_E_A, 7-2)
		Clock.schedule_once(self.animation_GP, 8-2)
		Clock.schedule_once(self.animation_off, 10-2)

	def animation_E_A(self, *arg):
		an1=Animation(pos_hint={"x":0, "y":-0.4}, d = .8)
		an1+=Animation(pos_hint={"x":-0.1, "y":-0.4}, d = .1)
		an1+=Animation(pos_hint={"x":0, "y":-0.4}, d = .1)
		an1.start(self.ids['E'])
		an2=Animation(pos_hint={"x":0, "y":-0.4}, d = .8)
		an2+=Animation(pos_hint={"x":0.1, "y":-0.4}, d = .1)
		an2+=Animation(pos_hint={"x":0, "y":-0.4}, d = .1)
		an2.start(self.ids['A'])
		an3=Animation(pos_hint={"x":0, "y":-0.3}, d = .4)
		an3+=Animation(pos_hint={"x":0, "y":-0.2}, d = .1)
		an3+=Animation(pos_hint={"x":0, "y":-0.3}, d = .1)
		an3.start(self.ids['R'])

	def animation_GP(self, *arg):
		an1=Animation(background_color=[1,1,1,1], d = .6)
		an1.start(self.ids['GP'])

	def animation_off(self, *arg):
		an=Animation(color=[0,0,0,0], d  = .3)
		an.start(self.ids['E'])
		an.start(self.ids['R'])
		an.start(self.ids['A'])
		an.start(self.ids['I_F_UP'])
		an1=Animation(background_color=[0,0,0,0], d = .3)
		an1.start(self.ids['GP'])

class MenuScreen(Screen):
	
	keysis = 0

	def animation_logo(self, *arg):
		if self.keysis==0:
			an1=Animation(pos_hint={"x":0, "top":1}, duration=.6)
			an1.start(self.ids['im_menu1'])
			an2=Animation(pos_hint={"x":0.2+2, "top":0.2}, d = .8)
			an2.start(self.ids['im_menu1_1'])
			an3=Animation(pos_hint={"x":0.3+2, "top":-0.6}, d = .8)
			an3.start(self.ids['im_menu1_2'])
			an4=Animation(pos_hint={"x":0.4+2, "top":-1.4}, d = .8)
			an4.start(self.ids['im_menu1_3'])
			an5=Animation(pos_hint={"x":0.6+2, "top":-2.2}, d = .8)
			an5.start(self.ids['im_menu1_4'])
			an5=Animation(pos_hint={"x":0.7+2, "top":1.8}, d = .8)
			an5.start(self.ids['im_menu1_5'])
			an5=Animation(pos_hint={"x":0.8+2, "top":2.6}, d = .8)
			an5.start(self.ids['im_menu1_6'])
			self.animation_widget()

	def animation_widget(self, *arg): 
		an1 = Animation(pos_hint={"x": 0, "top":1}, duration = 1)
		an1 += Animation(pos_hint={"x": 0, "top":1.1}, duration=.1)
		an1 += Animation(pos_hint={"x": 0, "top":1}, duration=.1)
		an1.start(self.ids['bl_menu1'])
		an2 = Animation(pos_hint={"x": 0, "top":1}, duration = 1)
		an2 += Animation(pos_hint={"x": 0, "top":1.1}, duration=.1)
		an2 += Animation(pos_hint={"x": 0, "top":1}, duration=.1)
		an2.start(self.ids['im_menu2'])
		an2.start(self.ids['im_menu3'])
		
	def animation_logo_2(self, *arg):
		pass



class PlayScreen(Screen):
	
	def animation_widget(self, *arg):
		an1 = Animation(pos_hint={"x": 0}, duration=.4)
		an1 += Animation(pos_hint={"x": -0.04}, duration=.1)
		an1 += Animation(pos_hint={"x": 0}, duration=.1)
		an1.start(self.ids['bl_play1'])
		an2 = Animation(pos_hint={"x": .5}, duration=.4)
		an2 += Animation(pos_hint={"x": .54}, duration=.1)
		an2 += Animation(pos_hint={"x": .5}, duration=.1)
		an2.start(self.ids['bl_play2'])
		an3 = Animation(pos_hint={"x": 0, "top":1}, duration = .1)
		an3 += Animation(pos_hint={"x": 0, "top":1.1}, duration=.1)
		an3 += Animation(pos_hint={"x": 0, "top":1}, duration=.1)
		an3.start(self.ids['bl_play3'])
		an3.start(self.ids['btn_play1'])
		
	def animation_widget_back(self, *arg):
		an1 = Animation(pos_hint={"x": -2, "y":0.15}, duration=.1)
		an1.start(self.ids['bl_play1'])
		an2 = Animation(pos_hint={"x":2.5, "y":0.15}, duration=.1)
		an2.start(self.ids['bl_play2'])
		an3 = Animation(pos_hint={"x": 0, "top": 3}, duration=.1)
		an3.start(self.ids['bl_play3'])
		an4 = Animation(pos_hint={"x":0, "top": 2.5}, duration=.1)
		an4.start(self.ids['btn_play1'])

class OptionScreen(Screen):
	pass

class OptionScreen_1(Screen):
	pass

class RoolsScreen(Screen):
	pass

class AboutScreen(Screen):
	pass


class FACTORIA(App):

	def build(self):
		sm = ScreenManager()
		sm.add_widget(EraScreen())
		sm.add_widget(MenuScreen(name = 'menu'))
		sm.add_widget(PlayScreen(name = 'play'))
		sm.add_widget(OptionScreen(name = 'option'))
		sm.add_widget(OptionScreen_1(name = 'option_1'))
		sm.add_widget(RoolsScreen(name = 'rools'))
		sm.add_widget(AboutScreen(name = 'about'))

		return sm


if __name__== "__main__":
	FACTORIA().run()
