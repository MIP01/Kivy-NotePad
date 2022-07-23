import kivy
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager



class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass




# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_file("main.kv")
        return screen

    def process(self):
        menuscreen = self.root.get_screen('profile')
        text = menuscreen.ids.input.text
        print(text)
    
    
        


DemoApp().run()
