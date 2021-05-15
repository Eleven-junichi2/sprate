from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class EditorScreen(Screen):
    pass


class SprateScreenManager(ScreenManager):
    pass


class SprateApp(App):
    def build(self):
        root_widget = SprateScreenManager()
        root_widget.add_widget(EditorScreen(name="editor"))
        return root_widget


if __name__ == "__main__":
    SprateApp().run()
