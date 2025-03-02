from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
import datetime
from datetime import date
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar

Window.size = (350, 600)


class ToDoCard(FakeRectangularElevationBehavior, MDFloatLayout):
    title = StringProperty()
    description = StringProperty()

class ToDoApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main_screen_to_do.kv"))
        screen_manager.add_widget(Builder.load_file("add_task.kv"))

        return screen_manager

    def on_start(self):
        today = date.today()
        wd = date.weekday(today)
        days = [ "Monday",  "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().strftime("%b"))
        day = str(datetime.datetime.now().strftime("%d"))
        screen_manager.get_screen("main").date.text = f"{days[wd]}, {month} {day}, {year}"

    def on_complete(self, checkbox, value, description, bar):
            if value:
                description.text = f"[s]{description.text}[/s]"
                bar.md_bg_color = 0, 179/255, 0, 1
            else:
                remove = ["[s]", "[/s]"]
                for i in remove:
                    description.text = description.text.replace(i, "")
                    bar.md_bg_color = 0, 179 / 255, 23/255, 1

    def add_task(self, title, description):
        #if title != "" and description != "" and len(title) < 35 and len(description) < 70:
            #screen_manager.current = "main"
            #screen_manager.transition.direction = "right"
            screen_manager.get_screen("main").todo_list.add_widget(ToDoCard(title = title, description = description))

            #screen_manager.get_screen("add_task").description.text = ""
        #screen_manager.get_screen("add_task").title.text = ""

if __name__ == "__main__":
    ToDoApp().run()
