from kivy.app import App
from kivy.uix.widget import Widget
from kivy.logger import Logger
from kivy.lang import Builder

Builder.load_file('./src/features/home/screens/home.kv')

class TagReader(Widget):
    pass

class TagApp(App):
    # Load screen
    try:
        print('testing')
    except:
        Logger.error(f'loadfile error')
    def build(self):
        self.title = 'Tag Reader'
        return TagReader()


if __name__ == '__main__':
    TagApp().run()