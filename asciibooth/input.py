'''Input event handlers for mouse and keyboard'''
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent

from rx.subjects import Subject
from collections import namedtuple
from threading import Thread

MouseClick = namedtuple('MouseClick', 'x y button')

class StopEvent:
    def stop(self):
        # hack for unreleased context
        # https://github.com/SavinaRoja/PyUserInput/issues/48
        from Xlib.display import Display
        display = Display()
        display.record_disable_context(self.ctx)
        display.close()
        return super().stop()

class ObservableEvent:
    def __init__(self, **kwargs):
        super(ObservableEvent, self).__init__(**kwargs)
        self.subject = Subject()

    def start(self, capture=False):
        self.capture = capture
        super().start()
        return self.subject


class MouseObserver(ObservableEvent, StopEvent, PyMouseEvent):
    def click(self, x, y, button, press):
        if press:
            event = MouseClick(x=x, y=y, button=button)
            self.subject.on_next(event)

class KeyboardObserver(ObservableEvent, StopEvent, PyKeyboardEvent):
    def tap(self, keycode, character, press):
        if press and character:
            self.subject.on_next(character)

class GetchObserver(ObservableEvent, Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True

    def run(self):
        from .getch import getchgen
        getch, self.reset = getchgen()
        while True:
            self.subject.on_next(getch())

    def stop(self):
        self.reset()

def observe_mouse(capture=False):
    observer = MouseObserver()
    return observer, observer.start(capture=capture).filter(
        lambda click: click.button <= 2 # Subscribe only to left and right button
        )

def observe_keyboard(capture=False):
    observer = KeyboardObserver()
    subject = observer.start(capture=capture)

    return observer, subject

def observe_getch():
    observer = GetchObserver()
    subject = observer.start()

    return observer, subject

if __name__ == '__main__':
    o, s = observe_getch()

    s.subscribe(lambda k: print(k))
    while True:
        pass
