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

class Welcome(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        master = BoxLayout(orientation='vertical', padding=20, spacings=20)
        master.add_widget(Label(text="Welcome to The Elder's Expedition", font_size='40sp', font_name="DejaVuSans"))
        master.add_widget(Button())
        self.add_widget(master)

class ScreenTransition(Button):
    def __init__(self, screen, direction="up", goal="home" **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name="home"))
        return sm
    
if __name__ in "__main__":
    MainApp().run()
