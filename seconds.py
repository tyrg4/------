# напиши модуль для реализации секундомера
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.properties import BooleanProperty
class Seconds(ProgressBar):
    End = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.total = total
        self.End = False
        super().__init__(max = self.total,value = self.total)
    def restart(self, total, **kwargs):
        pass

    def start(self):
        pass

    def change(self, dt):
        self.value -= 1
        if self.value <=0:
            self.End = True
            return False
        