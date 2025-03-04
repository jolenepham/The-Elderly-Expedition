import mathGame
import sequence
import Crazy_Cards
import To_Do_List

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
from kivy.core.window import Window


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.6, 0.8, 0.9, 1)  # Pale blue background
            self.rect = Rectangle(size=self.size, pos=self.pos)

        
        self.bind(size=self.update_rect, pos=self.update_rect)
        background = Image(source='trees.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20, 
        size_hint=(0.8, 0.5), pos_hint={'center_x': 0.5, 'top': 1})

        # Welcome Label - properly centered
        welcome_label = Label(
            text="Welcome to The Elder's Expedition", 
            font_size=90, bold=True, color=(1, 1, 1, 1), 
            size_hint_y=None, height=120, halign = "center" )

        # Creators Label - positioned slightly lower
        creators = Label(
            text="Made by The Lost and Found",
            font_size=50, 
            size_hint_y=None, height = 40, halign = "center")
        
        layout.add_widget(welcome_label)
        layout.add_widget(creators)
        self.add_widget(layout)
        

    def on_enter(self):
        # Schedule transition to LoadScreen after 5 seconds
        Clock.schedule_once(self.switch_to_load, 5)

    def switch_to_load(self, dt):
       self.manager.current = "load"

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

#Loading Screen
class LoadScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)  # White background
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20, 
        size_hint=(0.8, 0.5), pos_hint={'center_x': 0.5, 'top': 1})

        self.frames = ['frame1.png', 'frame2.png', 'frame3.png', 'frame4.png','frame5.png','frame6.png']
        
        # Image widget to display the frames
        self.image_widget = Image(source=self.frames[0],size_hint=(None, None), size=(900, 900),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.5})  # Set initial image
        layout.add_widget(self.image_widget)

        self.loading_label = Label(text="Loading.", font_size=60, bold=True, color=(0, 0, 0, 1))
        layout.add_widget(self.loading_label)

        self.add_widget(layout)
        
        # Set an interval to update the image every 0.1 seconds (adjust time as needed)
        self.frame_index = 0  # Start with the first image
        self.animation = Clock.schedule_interval(self.update_image, 0.1)

        # Schedule an interval to update the "Loading..." text
        self.loading_text_index = 0
        self.loading_texts = ["Loading.", "Loading..", "Loading..."]
        self.loading_animation = Clock.schedule_interval(self.update_loading_text, 0.5)
        
        # Set an interval to update the image every 0.1 seconds (adjust time as needed)
        self.frame_index = 0  # Start with the first image
        self.animation = Clock.schedule_interval(self.update_image, 0.1)

    def update_image(self, dt):
        # Move to the next image in the list
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.image_widget.source = self.frames[self.frame_index]

    def update_loading_text(self, dt):
        # Cycle through "Loading.", "Loading..", "Loading..."
        self.loading_text_index = (self.loading_text_index + 1) % len(self.loading_texts)
        self.loading_label.text = self.loading_texts[self.loading_text_index]

    def on_enter(self):
        # Schedule transition to StartScreen after 8 seconds
        Clock.schedule_once(self.switch_to_start, 8)

    def switch_to_start(self, dt):
        self.manager.current = "start"
    


#Start Screen
class StartScreen(Screen):
    #Click Button to Get Started and go to home
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor =(0.3,0.1,0.4,1)

        background = Image(source='old_couple.webp', allow_stretch=True, keep_ratio=False)
        self.add_widget(background)
            
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        begin = Button(text = "Get Started", 
                       size_hint=(None, None), size=(390, 150),
                       background_color=(1, 0.7, 0.8, 1),  # Blue color
                       color=(1, 1, 1, 1),  # White text
                       font_size=50,
                       bold=True)
        layout.add_widget(begin)

        begin.bind(on_press = self.go_to_home)
        self.add_widget(layout)

    def go_to_home(self,dt):
        self.manager.current = "home"

# Home Screen with 3 buttons
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        # Buttons
        btn_score = Button(text="Score", size_hint=(1, 0.2), font_size=70, background_color = (0.96, 0.96, 0.86, 1))
        btn_games = Button(text="Games", size_hint=(1, 0.2), font_size=70, background_color = (0.89, 0.45, 0.36, 1))
        btn_todo = Button(text="To-Do List", size_hint=(1, 0.2), font_size=70, background_color = (0.50, 0.50, 0, 1))

        # Bind the Games button to the go_to_games method
        btn_games.bind(on_press=self.go_to_games)
        btn_todo.bind(on_press=self.run_to_do_list)

        # Add widgets to layout
        layout.add_widget(btn_score)
        layout.add_widget(btn_games)
        layout.add_widget(btn_todo)

        self.add_widget(layout)

    def go_to_games(self, dt):
        # Switch to the game select screen when the button is clicked
        self.manager.current = "games"

    def run_to_do_list(self, dt):
        To_Do_List.ToDoApp().run()   



#New Screen for the 3 games
class GameSelectScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        btn_game1 = Button(text="Math Madness", size_hint=(1, 0.2), height=100, font_size=70,
                           background_color = (0.96, 0.96, 0.86, 1))
        btn_game2 = Button(text="Crazy Cards", size_hint=(1, 0.2), height=100, font_size=70,
                           background_color = (0, 0.50, 0.50, 1))
        btn_game3 = Button(text="Silly Sequence", size_hint=(1, 0.2), height=100, font_size=70,
                           background_color = (0.42, 0.56, 0.68, 1))

        btn_game1.bind(on_press=self.game1_action)
        btn_game2.bind(on_press=self.game2_action)
        btn_game3.bind(on_press=self.game3_action)

        layout.add_widget(btn_game1)
        layout.add_widget(btn_game2)
        layout.add_widget(btn_game3)

        self.add_widget(layout)

    def game1_action(self, instance):
        print("Math Madness Game Selected")
        mathGame.MathMadnessApp().run()
        

    def game2_action(self, instance):
        print("Crazy Cards Game Selected")
        Crazy_Cards.Memory().run()

    def game3_action(self, instance):
        print("Silly Sequence Game Selected")
        sequence.MemoryGameApp().run()
        

# Main App
class EldersExpeditionApp(App):
   def build(self):
       sm = ScreenManager(transition=FadeTransition())


       # Add screens to the manager
       splash = SplashScreen(name="splash")


       sm.add_widget(splash)
       sm.add_widget(HomeScreen(name="home"))
       sm.add_widget(StartScreen(name="start"))
       sm.add_widget(GameSelectScreen(name="games"))
       sm.add_widget(LoadScreen(name="load"))

       return sm




# Run the app
if __name__ == "__main__":
   EldersExpeditionApp().run()