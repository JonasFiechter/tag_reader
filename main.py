from kivy.app import App
from kivy.uix.widget import Widget
from kivy.logger import Logger
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.event import EventDispatcher


class MenuScreen(Screen, App):
    def close_app(self):
        Logger.error('INSIDE CLOSE_APP')
        # TODO: consider adding a quit button into menu screen
        self.stop()

class SettingsScreen(Screen):
    def log_on_screen(self):
        Logger.warning('INSIDE SETTINGS')

class TagReader(Screen):
    pass

class TagReaderApp(App):
    # Load screen
    try:
        print('test')
        Builder.load_file('./src/features/home/screens/home.kv')
    except:
        Logger.error(f'loadfile error')

    def build(self):
        self.title = 'TagReaderApp'
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='Menu'))
        sm.add_widget(SettingsScreen(name='Settings'))
        sm.add_widget(TagReader(name='TagReader'))
        return sm


if __name__ == '__main__':
    TagReaderApp().run()
