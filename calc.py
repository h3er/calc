import math
import kivy
from kivy.app import App
from kivy.core.window import Window

#maths
def sin(num): return math.sin(math.radians(num))
def cos(num): return math.cos(math.radians(num))
def tan(num): return math.tan(math.radians(num))
def expandBrackets():
    txt = self.root.ids.textBox.text
    amtbrackets = txt.count('(')
    for x in ') ':
        txt = txt.replace(x, '')
    txt = txt.split('(')
    txt.pop(0)

    var_x = []
    for x in range(0,amtbrackets):
        xlocation = txt[x].find('x')
        if xlocation == 0:
            var_x.append(1)
        elif txt[x][0:2] == '-x':
            var_x.append(-1)   
        else:
            var_x.append(int(txt[x][0:(xlocation)]))

    var_c = []
    for y in range(0,amtbrackets):
        listindlen = len(txt[y])
        symbollocation = txt[y].find('+')
        if symbollocation == -1:
            symbollocation = txt[y].find('-', 1)
        var_c.append(int(txt[y][symbollocation:listindlen]))

    if amtbrackets == 3:
        xcubed = var_x[0] * var_x[1] * var_x[2]
        xsquared = (((var_c[0] * var_x[1]) + (var_c[1] * var_x[0])) * var_x[2]) + (var_c[2] * var_x[0] * var_x[1])
        xregular = (var_c[0] * var_c[1] * var_x[2]) + (((var_c[0] * var_x[1]) + (var_c[1] * var_x[0])) * var_c[2])
        constant = var_c[0] * var_c[1] * var_c[2]
        xsquared = str(xsquared)
        xregular = str(xregular)
        constant = str(constant)
        if xsquared[0] != '-':
            xsquared = '+', xsquared
        if xregular[0] != '-':
            xregular = '+', xregular
        if constant[0] != '-':
            constant = '+', constant
        bracketans = xcubed, 'x^3', xsquared, 'x^2', xregular, 'x', constant 
    elif amtbrackets == 2:
        xsquared = var_x[0] * var_x[1]
        xregular = (var_x[0] * var_c[1]) + (var_x[1] * var_c[0])
        constant = var_c[0] * var_c[1]
        xregular = str(xregular)
        constant = str(constant)
        if xregular[0] != '-':
            xregular = '+', xregular
        if constant[0] != '-':
            constant = '+', constant
        bracketans = xsquared, 'x^2', xregular, 'x', constant  
        self.root.ids.textBox.text = bracketans

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
            global ans
            try:
                if 'π' in exp:
                    #if exp.find('π')   coefficient of pi
                    exp = exp.replace('π', str(math.pi))
                ans = str(eval(exp))
                self.root.ids.textBox.text = ans
                exp = ''
            except:
                pass
        elif txt == 'ans':
            exp += ans
            self.root.ids.textBox.text = exp
        else:
            exp += txt
            self.root.ids.textBox.text = exp

if __name__ == '__main__':
    global exp
    exp = ''
    MyApp().run()