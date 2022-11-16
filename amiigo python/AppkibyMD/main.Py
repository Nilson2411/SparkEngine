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
<<<<<<<< HEAD:AppkibyMD/main.Py
    "Holaa 3 xddd"
    "Hola 4 XD"
========
    "Holaa 3 xd"
>>>>>>>> f14e1cfae844cc7f79dd4f5b9a9ba70bced1e317:amiigo python/AppkibyMD/main.Py
