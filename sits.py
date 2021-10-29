# модуль для подсчета количества приседаний
from kivy.uix.label import Label

class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        mytext = "Осталось приседаний: " + str(self.total)
        super().__init__(text = mytext, **kwargs)

    def next(self, *args):
        self.current += 1
        remaining = max(0, self.total - self.current)
        self.text = "Осталось приседаний: " + str(remaining)