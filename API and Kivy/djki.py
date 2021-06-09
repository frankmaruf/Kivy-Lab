from os import pardir
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest
from kivy.uix.label import Label
import requests


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getapi(self, widget):
        url = "http://localhost:8000/viewset/article"
        items = requests.get(url)
        print(items.status_code)
        for item in items.json():
            print(item['title'])
            lable = Label(
                text="title:"+item['title']+"\n"+"author:"+item['author'])
            self.add_widget(lable)


class MainWidget(Widget):
    pass


class apiApp(App):
    def build(self):
        self.title = "Django API"
        return super().build()


apiApp().run()
