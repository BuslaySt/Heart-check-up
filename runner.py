# модуль для работы с анимацией
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.animation import Animation

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)

    def __init__(self, total = 5, steptime = 1.5, autorepeat = False, **kwargs):
        self.total = total
        self.steptime = steptime
        self.animation = (Animation(pos_hint={'top': 1.0}, duration=steptime/2)
                    + Animation(pos_hint={'top': 0.2}, duration=steptime/2))
        # self.animation.repeat = autorepeat
        self.animation.on_progress = self.next
        super().__init__(**kwargs)

        self.btn = Button(text='Присед',size_hint=(1, 0.2), pos_hint={'top': 0.2})
        self.add_widget(self.btn)
        
    def start(self):
        self.value = 0
        self.finished = False
        self.animation.repeat = True
        self.animation.start(self.btn)

    def next(self, widget, step):
        if step == 1.0:
            self.value += 1
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True
