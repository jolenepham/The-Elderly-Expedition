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
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.image import Image

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        trees = Image(source='trees.png')
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.6, 0.8, 0.9, 1)  # Pale blue background
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Main layout inside an AnchorLayout for better control
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        layout = BoxLayout(orientation='vertical', spacing=10, padding=50, 
                           size_hint=(0.8, 0.5))

        # Welcome Label - properly centered
        welcome_label = Label(
            text="Welcome to The Elder's Expedition", 
            font_size=90, bold=True, color=(1, 1, 1, 1),
            size_hint_y=None, halign="center", valign="top")

        # Creators Label - positioned slightly lower
        creators = Label(
            text="Made by The Lost and Found",
            font_size=30, 
            size_hint_y=None, pos = (80,80))
        
        class FullImage(Image):
            pass
        
        
        layout.add_widget(welcome_label)
        layout.add_widget(creators)
        anchor_layout.add_widget(layout)
        self.add_widget(anchor_layout)
        layout.add_widget(trees)

    def on_enter(self):
        # Schedule transition to StartScreen after 5 seconds
        Clock.schedule_once(self.switch_to_start, 5)

    def switch_to_start(self, dt):
       self.manager.current = "start"

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


#Start Screen
class StartScreen(Screen):
    #Click Button to Get Started and go to home
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0, 1, 0, 1)  # Green color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        

        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        begin = Button(text = "Get Started", 
                       size_hint=(None, None), size=(390, 150),
                       background_color=(0.2, 0.6, 0.8, 1),  # Blue color
                       color=(1, 1, 1, 1),  # White text
                       font_size=50,
                       bold=True)
        layout.add_widget(begin)
        self.add_widget(layout)
        begin.bind(on_press = self.go_to_home)
    def go_to_home(self,dt):
        self.manager.current = "home"
    



# Home Screen with 3 buttons
class HomeScreen(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       layout = BoxLayout(orientation="vertical", spacing=10, padding=20)


       # Buttons
       btn_score = Button(text="Score", size_hint=(1, 0.2))
       btn_games = Button(text="Games", size_hint=(1, 0.2))
       btn_todo = Button(text="To-Do List", size_hint=(1, 0.2))


       # Add widgets to layout
       layout.add_widget(btn_score)
       layout.add_widget(btn_games)
       layout.add_widget(btn_todo)


       self.add_widget(layout)




# Main App
class EldersExpeditionApp(App):
   def build(self):
       sm = ScreenManager(transition=FadeTransition())


       # Add screens to the manager
       splash = SplashScreen(name="splash")


       sm.add_widget(splash)
       sm.add_widget(HomeScreen(name="home"))
       sm.add_widget(StartScreen(name="start"))


       return sm




# Run the app
if __name__ == "__main__":
   EldersExpeditionApp().run()