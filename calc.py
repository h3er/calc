import math
import kivy
from kivy.app import App
from kivy.core.window import Window

#maths
def sin(num): return math.sin(math.radians(num))
def cos(num): return math.cos(math.radians(num))
def tan(num): return math.tan(math.radians(num))
def asin(num): return math.degrees(math.asin(num))
def acos(num): return math.degrees(math.acos(num))
def atan(num): return math.degrees(math.atan(num))
def expandBrackets(text):
    txt = str(text)
    amtbrackets = txt.count('(')
    for x in ') ': txt = txt.replace(x, '')
    txt = txt.split('(')
    txt.pop(0)

    vx, vc= [], []
    for x in range(0,amtbrackets):
        xlocation = txt[x].find('x')
        if xlocation == 0: vx.append(1)
        elif txt[x][0:2] == '-x': vx.append(-1)   
        else: vx.append(int(txt[x][0:xlocation]))

        listindlen = len(txt[x])
        symbollocation = txt[x].find('+')
        if symbollocation == -1: symbollocation = txt[x].find('-', 1)
        vc.append(int(txt[x][symbollocation:listindlen]))

    if amtbrackets == 3:
        xcubed = vx[0] * vx[1] * vx[2]
        xsquared = (((vc[0] * vx[1]) + (vc[1] * vx[0])) * vx[2]) + (vc[2] * vx[0] * vx[1])
        xregular = (vc[0] * vc[1] * vx[2]) + (((vc[0] * vx[1]) + (vc[1] * vx[0])) * vc[2])
        constant = vc[0] * vc[1] * vc[2]
        xcubed, xsquared, xregular, constant = str(xcubed), str(xsquared), str(xregular), str(constant)
        if xsquared[0] != '-': xsquared = '+' + xsquared
        if xregular[0] != '-': xregular = '+' + xregular
        if constant[0] != '-': constant = '+' + constant
        return str(xcubed + 'x^3' + xsquared + 'x^2' + xregular + 'x' + constant)

    elif amtbrackets == 2:
        xsquared = vx[0] * vx[1]
        xregular = (vx[0] * vc[1]) + (vx[1] * vc[0])
        constant = vc[0] * vc[1]
        xsquared, xregular, constant = str(xsquared), str(xregular), str(constant)
        if xsquared == '1': xsquared = ''
        elif xsquared == '-1': xsquared = '-'
        if xregular == '1': xregular = ' '
        elif xregular == '-1': xregular = '-'
        if xregular[0] != '-' and xregular != ' ': xregular = '+ ' + xregular
        elif xregular[0] != '-': xregular = '+ '
        else: xregular = '- ' + xregular[1:]
        if constant[0] != '-': constant = '+ ' + constant
        else: constant = '- ' + constant[1:]
        return str(xsquared + 'x\u00B2 ' + xregular + 'x ' + constant)

#gui
class MyApp(App):
    def build(self):
        Window.clearcolor = '#121212'
        Window.size = (800, 600)
        
    def appendText(self, txt, dis):
        global exp, disp, ans
        if txt == 'clr': exp, disp, self.root.ids.textBox.text = '', '', ''
        elif txt == 'del': pass
        elif txt == '=':
            try:
                if exp.count('(') > exp.count(')'):
                    for x in range(0, exp.count('(') - exp.count(')')): exp = exp + ')'
                ans = eval(exp)
                self.root.ids.textBox.text = str(ans)
                exp = ''
            except:
                pass
        elif txt == 'expndbrcts':
            self.root.ids.textBox.text = expandBrackets(self.root.ids.textBox.text)
        else:
            exp += txt
            try:
                disp += dis
            except TypeError:
                disp += txt
            self.root.ids.textBox.text = disp
            
if __name__ == '__main__':
    global exp, disp
    exp, disp = '', ''
    MyApp().run()
