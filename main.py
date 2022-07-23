import kivy
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.textinput import TextInput
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch



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
    
    def add_task(self, task):
        '''Add task to the list of tasks'''

        print(task.text)
        menu = self.root.get_screen("menu")
        menu.ids['container'].add_widget(ListItemWithCheckbox(text='[b]'+task.text+'[/b]'))
        task.text = '' # set the dialog entry to an empty string(clear the text entry)


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    '''Custom list item'''

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk

    def delete_item(self, the_list_item):
        '''Delete the task'''
        self.parent.remove_widget(the_list_item)

    
        


DemoApp().run()
