import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class MathMadnessApp(App):
    def build(self):
        self.score = 0
        self.num_questions = 10
        self.question, self.correct_answer = self.ask_question()

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        with self.layout.canvas.before:
            Color(0.5, 0.7, 1, 1)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
        self.layout.bind(size=self.update_rect, pos=self.update_rect)

        self.bg_image = Image(source="./math/symbols.png", allow_stretch=False, keep_ratio=False)
        self.bg_image.size_hint = (1, 2)
        self.bg_image.height = 300
        self.layout.add_widget(self.bg_image)

        self.title_label = Label(text="Welcome to Math Madness!", font_size=50, bold=True, font_name="DejaVuSans", color=(0.2, 0.4, 0.2, 1))
        self.layout.add_widget(self.title_label)

        self.start_button = Button(text="Start Game", font_size=24, size_hint=(None, None), size=(200, 60), background_color=(0.2, 0.6, 0.2, 1))
        self.start_button.bind(on_press=self.start_game)
        self.layout.add_widget(self.start_button)

        return self.layout

    def update_rect(self, *args):
        self.rect.pos = self.layout.pos
        self.rect.size = self.layout.size

    def start_game(self, instance):
        self.layout.clear_widgets()

        with self.layout.canvas.before:
            Color(0.5, 0.7, 1, 1)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
        self.layout.bind(size=self.update_rect, pos=self.update_rect)

        self.title_label = Label(text="Math Madness Game", font_size=50, bold=True, font_name="DejaVuSans", color=(0.2, 0.4, 0.2, 1))
        self.layout.add_widget(self.title_label)

        self.question_label = Label(text=self.question, font_size=35, color=(0.3, 0.2, 0.1, 1))
        self.layout.add_widget(self.question_label)

        self.answer_input = TextInput(hint_text="Your answer", multiline=False, font_size=25, size_hint=(None, None), size=(200, 44), background_color=(0.8, 0.8, 0.6, 1))
        self.layout.add_widget(self.answer_input)

        self.submit_button = Button(text="Submit Answer", font_size=25, size_hint=(None, None), size=(200, 60), background_color=(0.2, 0.6, 0.2, 1))
        self.submit_button.bind(on_press=self.check_answer)
        self.layout.add_widget(self.submit_button)

        self.score_label = Label(text=f"Score: {self.score}/{self.num_questions}", font_size=30, color=(0.2, 0.4, 0.2, 1))
        self.layout.add_widget(self.score_label)

    def ask_question(self):
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        operation = random.choice(['+', '-', '*'])

        if operation == '+':
            correct_answer = num1 + num2
            question = f"What is {num1} + {num2}?"
        elif operation == '-':
            correct_answer = num1 - num2
            question = f"What is {num1} - {num2}?"
        else:
            correct_answer = num1 * num2
            question = f"What is {num1} * {num2}?"
        
        return question, correct_answer

    def check_answer(self, instance):
        try:
            user_answer = int(self.answer_input.text)
        except ValueError:
            self.show_popup("Invalid input", "Please enter a valid number!")
            return

        if user_answer == self.correct_answer:
            self.score += 1
            self.show_popup("Correct!", "Well done, that's the correct answer!")
        else:
            self.show_popup("Incorrect!", f"Oops! The correct answer was {self.correct_answer}.")
        
        self.score_label.text = f"Score: {self.score}/{self.num_questions}"
        self.question, self.correct_answer = self.ask_question()
        self.question_label.text = self.question
        self.answer_input.text = ""

        if self.score == self.num_questions:
            self.show_popup("Game Over", f"Congratulations! You scored {self.score}/{self.num_questions}.")
            self.show_restart_button()

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message, font_size=20))

        close_button = Button(text="Close", font_size=20, size_hint=(None, None), size=(100, 50), background_color=(0.2, 0.6, 0.2, 1))
        close_button.bind(on_press=self.close_popup)
        popup_layout.add_widget(close_button)

        self.popup = Popup(title=title, content=popup_layout, size_hint=(None, None), size=(400, 300))
        self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()

    def show_restart_button(self):
        restart_button = Button(text="Restart Game", font_size=24, size_hint=(None, None), size=(200, 60), background_color=(0.2, 0.6, 0.2, 1))
        restart_button.bind(on_press=self.restart_game)
        self.layout.add_widget(restart_button)

    def restart_game(self, instance):
        self.score = 0
        self.question, self.correct_answer = self.ask_question()
        self.layout.clear_widgets()
        self.start_game(instance)

if __name__ == "__main__":
    MathMadnessApp().run()
