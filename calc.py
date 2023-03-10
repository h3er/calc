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
def quadEqu(equation):
    try:
        nums = []
        xsqucation = equation.find('x')
        nums.append(equation[:xsqulocation])
        xreglocation = equation.find('x', xsqulocation + 1)
        nums.append(equation[xsqucation + 1:xreglocation])
        nums.append(equation[xreglocation +1:])
        print(nums)
        ans1 = (-nums[1] + math.sqrt(nums[1]**2-(4*nums[0]*nums[2])) / (2 * nums[0])
        ans2 = (-nums[1] - math.sqrt(nums[1]**2-(4*nums[0]*nums[2])) / (2 * nums[0])
        return (f'x = {ans1} and x = {ans2}')
    except: pass
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
        
        if xcubed == '1': xcubed = ''
        elif xcubed == '-1': xcubed = '-'
            
        if xsquared == '1': xsquared = ' '
        elif xsquared == '-1': xsquared = '-'
        if xsquared[0] != '-' and xsquared != ' ': xsquared = '+ ' + xsquared
        elif xsquared[0] != '-': xsquared = '+ '
        else: xsquared = '- ' + xsquared[1:]
            
        if xregular == '1': xregular = ' '
        elif xregular == '-1': xregular = '-'
        if xregular[0] != '-' and xregular != ' ': xregular = '+ ' + xregular
        elif xregular[0] != '-': xregular = '+ '
        else: xregular = '- ' + xregular[1:]
            
        if constant[0] != '-': constant = '+ ' + constant
        else: constant = '- ' + constant[1:]
        
        
        return str(xcubed + 'x\u00B3 ' + xsquared + 'x\u00B2 ' + xregular + 'x' + constant)

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
                
def simultaneousEqu():
    pass

#gui
class MyApp(App):
    def build(self):
        Window.clearcolor = '#121212'
        Window.size = (800, 600)
        
    def changeSpinner(self, txt):
        pass
        
    def appendText(self, txt, dis):
        global exp, disp, ans, lenexp, lendisp
        if txt == 'clr': exp, disp, self.root.ids.textBox.text = '', '', ''
        elif txt == 'del':
            print(exp, disp, lenexp, lendisp)
            try: exp, disp, lenexp, lendisp = exp[:-int(lenexp[-1])], disp[:-int(lendisp[-1])], lenexp.pop(), lendisp.pop()
            except TypeError: exp, disp, lenexp, lendisp = exp[:-int(lenexp[-1])], disp[:-int(lenexp[-1])], lenexp.pop(), lendisp.pop()
            self.root.ids.textBox.text = disp
        elif txt == '=':
            try:
                if exp.count('(') > exp.count(')'):
                    for x in range(0, exp.count('(') - exp.count(')')): exp = exp + ')'
                ans = eval(exp)
                self.root.ids.textBox.text = str(ans)
                exp = ''
            except: pass
        elif txt == 'expndbrcts':
            self.root.ids.textBox.text = expandBrackets(self.root.ids.textBox.text)
        elif txt == 'quadEqu':
            self.root.ids.textBox.text = expandBrackets(self.root.ids.textBox.text)
        else:
            exp += txt
            lenexp.append(len(txt))
            print(lenexp, lendisp)
            if dis == None:
                lendisp.append(len(txt))
                disp += txt
            else:
                lendisp.append(len(dis))
                disp += dis
            self.root.ids.textBox.text = disp
            
if __name__ == '__main__':
    global exp, disp, lenexp, lendisp
    exp, disp, lenexp, lendisp = '', '', [], []
    MyApp().run()
