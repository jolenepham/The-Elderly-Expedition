
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Line
from kivy.clock import Clock

class ProgressCircle(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_points = 100  # maximum points
        self.current_points = 0  # current points (starting from 0)
        self.size = 200, 200  # size of the widget
        self.center = self.size[0] // 2, self.size[1] // 2  # center of the widget

        # Draw the outer circle and progress arc
        with self.canvas:
            self.background_circle = Ellipse(pos=(self.center[0] - 90, self.center[1] - 90), size=(180, 180))
            self.progress_arc = Line(circle=(self.center[0], self.center[1], 90, 0, 0), width=10)

        # Update the progress every 0.1 seconds (or when points change)
        Clock.schedule_interval(self.update_progress, 0.1)

    def set_points(self, points):
        """Set the current points and update the progress circle"""
        self.current_points = max(0, min(points, self.max_points))  # Clamp points between 0 and max_points

    def update_progress(self, dt):
        """Update the progress circle based on current points"""
        # Calculate the progress as a percentage of max points
        progress = self.current_points / self.max_points
        
        # Calculate the end angle based on the progress
        angle = 360 * progress

        # Update the progress arc (start angle is 0, and the end angle is the calculated one)
        self.progress_arc.circle = (self.center[0], self.center[1], 90, 0, angle)

    def on_touch_down(self, touch):
        """Increase points when user clicks on the widget"""
        if self.collide_point(*touch.pos):
            # Add points (for example, add 10 points per click)
            self.set_points(self.current_points + 10)
            print(f"Current Points: {self.current_points}")

class ProgressCircleApp(App):
    def build(self):
        return ProgressCircle()

if __name__ == "__main__":
    ProgressCircleApp().run()
