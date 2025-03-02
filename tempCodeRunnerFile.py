from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
import random

class MemoryGameApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Game instructions
        self.instructions_label = Label(
            text="This game is designed to help your memory.\nFirst, type a number for the length of the sequence.\nThen, you will have 10 seconds to memorize that sequence.\nFinally, you will be prompted to enter those numbers, one at a time.\n Good Luck!",
            size_hint=(1, None), height=150)
        
        self.layout.add_widget(self.instructions_label)

        # Input for sequence length
        self.length_input_label = Label(text="Enter the number of digits you want to guess:")
        self.layout.add_widget(self.length_input_label)

        self.length_input = TextInput(multiline=False, input_filter='int', size_hint=(1, None), height=40)
        self.layout.add_widget(self.length_input)

        # Button to start the game
        self.start_button = Button(text="Start Game", size_hint=(1, None), height=50)
        self.start_button.bind(on_press=self.start_game)
        self.layout.add_widget(self.start_button)

        # Label to show the sequence
        self.sequence_label = Label(text="", size_hint=(1, None), height=40)
        self.layout.add_widget(self.sequence_label)

        # Input for the sequence numbers
        self.sequence_input = TextInput(multiline=False, input_filter='int', size_hint=(1, None), height=40)
        self.layout.add_widget(self.sequence_input)

        # Button to submit the sequence
        self.submit_button = Button(text="Submit", size_hint=(1, None), height=50)
        self.submit_button.bind(on_press=self.check_sequence)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def start_game(self, instance):
        try:
            # Get sequence length from input
            length = int(self.length_input.text)
        except ValueError:
            self.show_popup("Invalid input", "Please enter a valid number for the sequence length.")
            return

        # Create the random sequence
        self.sequence = [random.randint(0, 9) for _ in range(length)]

        # Display the sequence for 10 seconds
        self.sequence_label.text = f"Memorize this: {''.join(map(str, self.sequence))}"
        Clock.schedule_once(self.hide_sequence, 10)

        # Clear input field for the user to enter the sequence after delay
        self.sequence_input.text = ""

    def hide_sequence(self, dt):
        # Hide the sequence after 10 seconds
        self.sequence_label.text = "Enter the sequence now."

    def check_sequence(self, instance):
        # Get the sequence entered by the user
        entered_sequence = self.sequence_input.text.strip()

        if not entered_sequence:
            self.show_popup("Empty Input", "Please enter the sequence.")
            return

        # Convert the input string into a list of integers
        entered_sequence = [int(x) for x in entered_sequence if x.isdigit()]

        # Compare entered sequence with the original
        if entered_sequence == self.sequence:
            self.show_popup("Correct!", "You guessed the sequence correctly!")
        else:
            self.show_popup("Incorrect", f"Oops! The correct sequence was: {''.join(map(str, self.sequence))}")

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        close_button = Button(text="Close", size_hint=(1, None), height=50)
        content.add_widget(close_button)

        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    MemoryGameApp().run()