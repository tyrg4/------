# напиши модуль для реализации секундомера
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.properties import BooleanProperty
from kivy.animation import Animation
class Seconds(ProgressBar):
    End = BooleanProperty(False)
    def __init__(self, total,runAnim, **kwargs):
        self.total = total
        self.End = False
        self.anim = Animation(size_hint=(.5,.2),duration = 3)+Animation(size_hint=(.5,.5),duration = 3)
        self.anim.repeat = True
        self.runAnim = runAnim
        super().__init__(max = self.total,value = self.total,**kwargs)
    def animation_start(self,*args):
        if self.value == 0:
            self.anim.stop(self)
    def restart(self, total, **kwargs):
        self.total = total
        self.End = False
        self.max = total
        self.value = total
        self.start()
    def start(self):
        if self.runAnim == True:
            self.anim.start(self)
            self.anim.on_progress = self.animation_start
        Clock.schedule_interval(self.change,1)
    def change(self, dt):
        self.value -= 1
        if self.value <=0:
            self.End = True
            return False
        