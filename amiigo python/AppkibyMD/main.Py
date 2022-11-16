#:kivy 2.1.0
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp


class Ui(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette= 'Teal'
        return ()
    def change_style(self,checked,value):
        if value:
            self.theme_cls.theme_style='Blue'
        else:
            self.theme_cls.theme_style='Light'

if __name__ == "__main__":
    MainApp().run()