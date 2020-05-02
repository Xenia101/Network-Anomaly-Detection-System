from kivy.app import App
from kivy.uix.button import  Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.core.window import Window

class App(App):
    def build(self):
        self.title = 'Sample App'
        
        self.box = BoxLayout(orientation='horizontal', spacing=20, padding=10)
        self.txt = TextInput(hint_text='Write here')
        self.btn = Button(text='Submit', on_press=self.BtnEvent, size_hint =(None, .5))

        self.box.add_widget(self.txt)
        self.box.add_widget(self.btn)
        return self.box

    def BtnEvent(self, instance):
        self.txt.text = ''

Window.size = (300, 100)
App().run()
