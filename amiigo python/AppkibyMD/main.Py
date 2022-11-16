from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp


class Ui(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette= 'Teal'
        return Ui()
    def change_style(self,checked,value):
        if value:
            self.theme_cls.theme_style='Dark'
        else:
            self.theme_cls.theme_style='Light'

if __name__ == "__main__":
    MainApp().run()
    
    "holaa xddd" 
    "Hola 2 xdd"
    "Holaa 3 xd"