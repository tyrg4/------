from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import ruffier
import instructions
import seconds
class ScrButton(Button):
    def __init__(self,window,direction,target,**kvargs):
        super().__init__(**kvargs)
        self.window = window
        self.direction = direction
        self.target = target
        btn_color = [.97,.66,.16,1]
        self.background_color = btn_color
    def transfer(self,*args,**kwargs):
        self.window.manager.transition.direction = self.direction
        self.window.manager.current = self.target
class secret_screen(Screen):
    def __init__(self,name="s_screen"):
        super().__init__(name=name)
        layout1 = BoxLayout(orientation = 'vertical',spacing = 20)
        label1 = Label(text = "ТЫ БЛИЗОК К РЕИНКАРНАЦИИ",size_hint=(.5,.25),pos_hint={"x":.25})
        but1 = ScrButton(self,'up','third_screen',text = 'Продолжить(Жить неуверен)',size_hint=(.3,.1),pos_hint={"x":.33})
        but1.on_press = but1.transfer
        layout1.add_widget(label1)
        layout1.add_widget(but1)
        self.add_widget(layout1)
class main_screen(Screen):
    def __init__(self,name="main"):
        super().__init__(name=name)
        layout1 = BoxLayout(orientation = 'vertical',spacing = 20)
        label1 = Label(text = instructions.txt_instruction,size_hint=(.5,.25),pos_hint={"x":.25})
        self.ti1 = TextInput(hint_text = 'Введите имя(ну ладно не бойся):',size_hint=(.5,.025),pos_hint={"x":.25,'center_y':.20})
        self.ti2 = TextInput(hint_text = 'Введите возраст(ладно не такой уж ты и старый):',size_hint=(.5,.025),pos_hint={"x":.25,'center_y':.20})
        self.but1 = ScrButton(self,'up','second_screen',text = 'Начать',size_hint=(.3,.1),pos_hint={"x":.33})
        self.but1.on_press = self.next
        layout1.add_widget(label1)
        layout1.add_widget(self.ti1)
        layout1.add_widget(self.ti2)
        layout1.add_widget(self.but1)
        self.add_widget(layout1)
    def next(self):
        try:
            if self.ti2.text.isdigit():
                if int(self.ti2.text) >= 7:
                    global name, age
                    name = self.ti1.text
                    age = int(self.ti2.text)
                    self.but1.transfer()
                else:
                    self.ti2.text = ''
                    self.ti2.hint_text = "НАДО ВВЕСТИ ЧИСЛО БОЛЬШЕ ИЛИ РАВНОЕ          С Е М И ЧЕЛОВЕК БЕЗ ИЛИ С ВЫСШИМ ОБРАЗОВАНИЕМ"
            else:
                self.ti2.text = ''
                self.ti2.hint_text = "НАДО ВВЕСТИ ЧИСЛО ЧЕЛОВЕК БЕЗ ИЛИ С ВЫСШИМ ОБРАЗОВАНИЕМ"
        except Exception as n:
            print(n)
            
        
class second_screen(Screen):
    def __init__(self,name="second_screen"):
        super().__init__(name=name)
        layout1 = BoxLayout(orientation = 'vertical',spacing = 20)
        label1 = Label(text = instructions.txt_test1,size_hint=(.5,.25),pos_hint={"x":.25})
        self.ti1 = TextInput(hint_text = 'Результат(если есть):',size_hint=(.5,.025),pos_hint={"x":.25,'center_y':.20})
        self.ti1.set_disabled(True)
        self.but1 = ScrButton(self,'up','third_screen',text = 'Продолжить',size_hint=(.3,.1),pos_hint={"x":.33}) 
        self.timer = seconds.Seconds(15, size_hint=(.5,.05),pos_hint = {'x':.25,'center_y':.25})
        self.but1.on_press = self.CMERT
        self.is_activated = False
        self.timer.bind(End = self.blizko)
        layout1.add_widget(label1)
        layout1.add_widget(self.timer)
        layout1.add_widget(self.ti1)
        layout1.add_widget(self.but1)
        self.add_widget(layout1)
    def CMERT(self):
        if self.is_activated == True:
            global P1
            P1 = int(self.ti1.text)
            if self.ti1.text.isdigit():
                if int(self.ti1.text) >= 15:
                    self.but1.transfer()
                    third_screen.startTimer()
                elif int(self.ti1.text)<=15 and int(self.ti1.text)>=5:
                    self.ti1.text = ''
                    self.but1.target = 's_screen'
                    self.ti1.hint_text = "ТЫ БЛИЗОК К РЕИНКАРНАЦИИ"
                    self.but1.transfer()
                elif int(self.ti1.text)<=0 or int(self.ti1.text)<=4:
                    self.ti1.text = ''
                    self.ti1.hint_text = "В МОРГЕ КРУТО?"
            else:
                self.ti1.text = ''
                self.ti1.hint_text = "НАДО ВВЕСТИ ЧИСЛО ЧЕЛОВЕК БЕЗ ИЛИ С ВЫСШИМ ОБРАЗОВАНИЕМ"
        elif self.is_activated == False:
            self.but1.set_disabled(True)
            self.timer.start()
    def blizko(self, *args):
        self.but1.set_disabled(False)
        self.ti1.set_disabled(False)
        self.is_activated = True
class third_screen(Screen):
    timer = seconds.Seconds(45, size_hint=(.5,.05),pos_hint = {'x':.25,'center_y':.25})
    def __init__(self,name="third_screen"):
        super().__init__(name=name)
        layout1 = BoxLayout(orientation = 'vertical',spacing = 20)
        label1 = Label(text = instructions.txt_test2,size_hint=(.5,.25),pos_hint={"x":.25})
        but1 = ScrButton(self,'up','forth_bayard',text = 'Продолжить',size_hint=(.3,.1),pos_hint={"x":.33})
        self.timer.bind(End = but1.transfer)
        layout1.add_widget(label1)
        layout1.add_widget(self.timer)
        self.add_widget(layout1) 
    @classmethod
    def startTimer(cls):
        cls.timer.start() 
class forth_screen(Screen):
    def __init__(self,name="forth_bayard"):
        super().__init__(name=name)
        self.state = 1
        layout1 = BoxLayout(orientation = 'vertical',spacing = 20)
        label1 = Label(text = instructions.txt_test3,size_hint=(.5,.25),pos_hint={"x":.25})
        self.ti1 = TextInput(hint_text = 'Результат',size_hint=(.5,.025),pos_hint={"x":.25,'center_y':.20})
        self.ti2 = TextInput(hint_text = 'Результат после отдыха:',size_hint=(.5,.025),pos_hint={"x":.25,'center_y':.20})
        self.but1 = ScrButton(self,'up','five',text = 'Завершить',size_hint=(.3,.1),pos_hint={"x":.33})
        self.timer1 = seconds.Seconds(15, size_hint=(.5,.05),pos_hint = {'x':.25,'center_y':.25})
        self.timer2 = seconds.Seconds(30)
        self.ti1.set_disabled(True)
        self.ti2.set_disabled(True)
        self.timer1.bind(End = self.startTimer1)
        self.but1.on_press = self.next
        layout1.add_widget(label1)
        layout1.add_widget(self.timer1)
        layout1.add_widget(self.ti1)
        layout1.add_widget(self.ti2)
        layout1.add_widget(self.but1)
        self.add_widget(layout1)
    def startTimer1(self,*args,**kwargs):
        self.ti1.set_disabled(False)
        self.state += 1
        if self.state == 2:
            self.timer1.restart(30)
            self.ti1.set_disabled(False)
        elif self.state == 3:
            self.timer1.restart(15)
            self.ti2.set_disabled(False)
            self.but1.set_disabled(False)
    def next(self):
        if self.state >= 3:
            global P2
            P2 = int(self.ti1.text)
            global P3
            P3 = int(self.ti2.text)
            self.but1.transfer()
            fiveth_screen.textIditor(P1,P2,P3,age,name)
        elif self.state == 1:
            self.but1.set_disabled(True)
            self.timer1.start()
class fiveth_screen(Screen):
    text = Label(text = '',size_hint=(.5,.25),pos_hint={"x":.25})
    def __init__(self,name="five"):
        super().__init__(name=name)
        layout1 = BoxLayout(orientation = 'vertical',spacing = 20)
        layout1.add_widget(self.text)
        self.add_widget(layout1)
    @classmethod
    def textIditor(cls,P1,P2,P3,age,name):
        cls.text.text = ruffier.test(P1,P2,P3,age,name)
class MyApp(App):
    def build(self):
        scrmanager = ScreenManager()
        scrmanager.add_widget(main_screen())
        scrmanager.add_widget(second_screen())
        scrmanager.add_widget(secret_screen())
        scrmanager.add_widget(third_screen())
        scrmanager.add_widget(forth_screen())
        scrmanager.add_widget(fiveth_screen())
        return scrmanager
app = MyApp()
app.run()