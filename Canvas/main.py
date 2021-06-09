from ctypes import windll
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.metrics import dp


class MainInterFace(GridLayout):
    pass


class MainWidget(Widget):
    pass


class CanvasExample(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(600, 400, 150, 100), width=2)
            self.rect = self.react = Rectangle(pos=(350, 200), size=(150, 100))

    def on_button_set_on_rectangle(self, widget):
        print("clicked")
        self.rect.pos = (600, 400)
        widget.disabled = True

    def on_button_plus_x(self, widget):
        print("Clicked")
        x, y = self.rect.pos
        x += dp(10)
        y += dp(0)
        self.rect.pos = (x, y)

    def on_button_minus(self, widget):
        print("Clicked")
        x, y = self.rect.pos
        x += dp(-10)
        y += dp(0)
        self.rect.pos = (x, y)


class CanVApp(App):
    def build(self):
        self.title = "CanVas"
        return super().build()


CanVApp().run()
