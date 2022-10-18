from os import cpu_count
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.logger import Logger
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.event import EventDispatcher
import csv

from datetime import datetime


class MenuScreen(Screen, App):
    def close_app(self):
        Logger.error('INSIDE CLOSE_APP')
        # TODO: consider adding a quit button into menu screen
        self.stop()

class SettingsScreen(Screen):
    pass

class TagReader(Screen):
    count_loop = 1
    def export_to_csv(self):
        Logger.info(f'Creating file...')
        with open(f'test.csv', 'w') as file:
            writer = csv.writer(file)
            for index in range(self.count_loop):
                writer.writerow([f'row({index})', 'column_test', f'max_count_{self.count_loop}'])
    
    def add_to_count(self):
        Logger.warning('INSIDE SETTINGS')
        Logger.error(f'COUNT LOOP => {cpu_count, self.count_loop}')
        self.count_loop += 1
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
