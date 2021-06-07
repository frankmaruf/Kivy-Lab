from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton


class ExampleGrid(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("0")

    def clicked(self):
        if self.count_enabled:
            print("Button Clicked")
            self.count += 1
            self.my_text = str(self.count)

    def toggle_btn(self, widget):
        print("Worked"+widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = 'ON'
            self.count_enabled = True


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
