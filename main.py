from cProfile import label
from kivy.app import App
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen, ScreenManager

#home screen

class Home(Screen):
    def _init_ (self, **kwarss):
        super()._init_(*kwarss)
        self.initUI()
        
    def initUI(self):
        self.title = label(text="The Elder's Expedition")
        #self.input_option = 
        self.output_option
        self.btn_reverse
        self.btn_clear

class AnchorLayoutApp(App):
      
    def build(self):
 
        # Anchor Layout1
        layout = AnchorLayout(
        anchor_x ='right', anchor_y ='bottom')
        btn = Button(text ='Score',
                     size_hint =(.3, .3),
                     background_color =(1.0, 0.0, 0.0, 1.0))
      
        layout.add_widget(btn)
        return layout 
  
# creating the object root for AnchorLayoutApp() class  
root = AnchorLayoutApp()
# Run the Kivy app
root.run()

