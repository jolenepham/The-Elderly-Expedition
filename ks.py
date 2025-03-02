from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
import random


class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Background color setup
        with self.layout.canvas.before:
            Color(0.5, 0.7, 1, 1)  # Light Blue background
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
            self.layout.bind(size=self.update_rect, pos=self.update_rect)

        self.bg_image = Image(source="./game_pics/numbers.png", allow_stretch=False, keep_ratio=False)
        self.bg_image.size_hint = (1, 2)
        self.bg_image.height = 300
        self.layout.add_widget(self.bg_image)

        # Title Label
        title_label = Label(
            text="Welcome to Silly Sequences!", 
            halign="center", 
            font_size=70, 
            color=(1, 1, 1, 1)  # White text for the title
        )
        self.layout.add_widget(title_label)

        # Start Game Button
        start_button = Button(
            text="Start Game", 
            size_hint=(1, None),
            height=90,  # Slightly increased button height
            background_color=(0, 1, 0, 1),  # Light Green button
            font_size=35,
            color=(1, 1, 1, 1)  # White text
        )
        start_button.bind(on_press=self.start_game)
        self.layout.add_widget(start_button)

        self.add_widget(self.layout)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def start_game(self, instance):
        self.manager.current = 'game'  # Switch to the game screen


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Background color setup (light blue)
        with self.layout.canvas.before:
            Color(0.5, 0.7, 1, 1)  # Light Blue background
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
            self.layout.bind(size=self.update_rect, pos=self.update_rect)

        # Title Label
        self.title_label = Label(
            text="Silly Sequences", 
            halign="center", 
            font_size=100, 
            color=(1, 1, 1, 1)  # White text for the title
        )
        self.layout.add_widget(self.title_label)

        # Instructions Label
        self.instructions_label = Label(
            text="First, type a number for the length of the sequence.\n"
                 "Then, you will have 10 seconds to memorize that sequence.\n"
                 "Finally, you will be prompted to enter those numbers, one at a time.\n"
                 "Good Luck!",
            size_hint=(1, None),
            height=200,  # Reduced height for instructions to make room for other elements
            halign="center",
            font_size=25,
            color=(1, 1, 1, 1),  # White color for instructions
            valign="middle"
        )
        self.layout.add_widget(self.instructions_label)

        # Length Input Label
        self.length_input_label = Label(
            text="Enter the number of digits you want to guess:",
            size_hint=(1, None),
            height=70,  # Increased the height slightly to give more space
            halign="center",
            font_size=35,
            color=(1, 1, 1, 1)  # White text
        )
        self.layout.add_widget(self.length_input_label)

        # Text Input for Sequence Length
        self.length_input = TextInput(
            multiline=False,
            input_filter='int',
            halign="center",
            font_size=40,
            size_hint=(1, 0.75),
            height=50,
            background_normal='', 
            background_active='',
            foreground_color=(0, 0, 0, 1),  # Black text on white input field
            border=(0, 0, 0, 0)
        )
        self.layout.add_widget(self.length_input)

        # Start Game Button
        self.start_button = Button(
            text="Generate", 
            size_hint=(1, 1),
            height=90,  # Slightly increased button height
            background_color=(0, 1, 0, 1),  # Light Blue button
            font_size=35,
            color=(1, 1, 1, 1)  # White text
        )
        self.start_button.bind(on_press=self.start_game)
        self.layout.add_widget(self.start_button)

        # Sequence Display Label
        self.sequence_label = Label(text="", height=25, font_size=40, color=(1, 1, 1, 1))  # White text
        self.layout.add_widget(self.sequence_label)

        # Input for the Sequence Numbers
        self.sequence_input = TextInput(
            multiline=False,
            input_filter='int',
            font_size=40,
            size_hint=(1, 0.75),
            height=50,
            size=(30, 100),
            background_normal='', 
            background_active='',
            foreground_color=(0, 0, 0, 1),  # Black text on white input field
            border=(0, 0, 0, 0)
        )
        self.layout.add_widget(self.sequence_input)

        # Submit Button
        self.submit_button = Button(
            text="Submit",
            size_hint=(1, 1),
            height=90,
            background_color=(0, 1, 0, 1),  # Light Blue button
            font_size=35,
            color=(1, 1, 1, 1)  # White text
        )
        self.submit_button.bind(on_press=self.check_sequence)
        self.layout.add_widget(self.submit_button)
        
        self.add_widget(self.layout)

    def start_game(self, instance):
        try:
            # Get sequence length from input
            length = int(self.length_input.text)
            if length < 1 or length > 9:  # Check for a reasonable sequence length
                self.show_popup("Invalid Length", "Please enter a number between 1 and 9.")
                return
        except ValueError:
            self.show_popup("Invalid input", "Please enter a valid number for the sequence length.")
            return

        # Create the random sequence
        self.sequence = [random.randint(0, 9) for _ in range(length)]

        # Display the sequence for 3 seconds
        self.sequence_label.text = f"Memorize this: {''.join(map(str, self.sequence))}"
        Clock.schedule_once(self.hide_sequence, 3)

        # Clear input field
        self.sequence_input.text = ""

    def hide_sequence(self, dt):
        # Hide the sequence
        self.sequence_label.text = "Enter the sequence now."
        # Reset the input field to make it clear for the user to enter their guess
        self.sequence_input.text = ""

    def check_sequence(self, instance):
        # Get the sequence entered by the user
        entered_sequence = self.sequence_input.text.strip()

        if not entered_sequence:
            self.show_popup("Empty Input", "Please enter the sequence.")
            return

        entered_sequence = [int(x) for x in entered_sequence if x.isdigit()]

        # Compare entered sequence with the original
        if entered_sequence == self.sequence:
            self.show_popup("Correct!", "You guessed the sequence correctly!")
        else:
            self.show_popup("Incorrect", f"Oops! The correct sequence was: {''.join(map(str, self.sequence))}")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=20)
        content.add_widget(Label(text=message, font_size=45, color=(0.5, 0.8, 1, 1)))  # Dark Blue for message
        close_button = Button(text="Close", size_hint=(1, None), height=50, background_color=(0.5, 1, 0.5, 1))  # Green button
        content.add_widget(close_button)

        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MemoryGameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(GameScreen(name='game'))
        return sm


if __name__ == "__main__":
    MemoryGameApp().run()