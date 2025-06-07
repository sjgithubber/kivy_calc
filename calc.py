# from kivy import require
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.config import Config
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# require('2.3.1')
#
# # set window size
# Config.set('graphics', 'width', '800')
# Config.set('graphics', 'height', '600')
# Config.set('graphics', 'resizable', False)
#
# # define a widget or window
# class MyWidget(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = 'vertical'
#
#         btn_list = [
#             {}
#         ]
#
# # use the App instance to build the window and run it in main method
# class MyCalculator(App):
#     def build(self):
#         return MyWidget()
#
# # import Button class and create buttons and a Text Area for Calculator to work
# # let's add box layout and buttons
#
#
# if __name__ == '__main__':
#     calc = MyCalculator
#     calc().run()
#
#

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        main_layout = GridLayout(cols=1)
        
        # Display
        self.display = TextInput(
            multiline=False, 
            readonly=True, 
            size_hint_y=None, 
            height=150
        )
        main_layout.add_widget(self.display)
        
        # Buttons
        button_layout = GridLayout(cols=4)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        for button_text in buttons:
            btn = Button(text=button_text)
            btn.bind(on_press=self.on_button_press)
            button_layout.add_widget(btn)
        
        main_layout.add_widget(button_layout)
        return main_layout
    
    def on_button_press(self, instance):
        # need to add an instance.text == 'C' to clear screen
        if instance.text == '=':
            try:
                result = str(eval(self.display.text))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Error'
                print(f"Error: {e}")
        else:
            self.display.text += instance.text
if __name__ == '__main__':
    CalculatorApp().run()
# Tasks
# need to learn how to manipulate using .kv file for classes
# also need to add a size for this GUI using kv
# need to add an instance.text == 'C' to clear screen

