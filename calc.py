import math
import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.clock import Clock

#maths
def sin(num): return math.sin(math.radians(num))
def cos(num): return math.cos(math.radians(num))
def tan(num): return math.tan(math.radians(num))

#gui
class MyApp(App):
    def build(self):
        Window.clearcolor = '#121212'
        Window.size = (800, 600)

    def appendText(self, txt):
        global exp
        if txt == 'clr':
            exp = ''
            self.root.ids.textBox.text = ''
        elif txt == '=':
            self.root.ids.textBox.text = str(eval(exp))
            exp = ''
        elif txt == 'ans':
            pass #cache system here
        else:
            exp += txt
            self.root.ids.textBox.text = exp


if __name__ == '__main__':
    global exp
    exp = ''
    MyApp().run()
