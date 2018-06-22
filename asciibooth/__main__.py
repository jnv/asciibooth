from threading import Semaphore
from rx import Observable
from rx.concurrency import Scheduler
from time import sleep
from .input import observe_mouse, observe_keyboard, observe_getch
from . import ascii
from . import screen
from . import config
from . import raster
from . import output
from .statuses import status_generator
from .state import State, set_callback
from .camera import Camera

CAMERA = Camera()
OUTPUT_CONVERTOR = ascii.Convertor(stream_size=config.CAPTURE_RESIZE, size=config.RENDER_CHARS, contrast=config.RENDER_CONTRAST)
RASTERIZER = raster.TextImage(config.RASTER_FONT)
STATUS_GEN = status_generator()
THREADS = []
QUIT_LOCK = Semaphore(0)
STATE = State()

@set_callback(STATE, 'onready')
def ready(e):
    screen.status('Ready.', clear=True)
    CAMERA.start_preview()
    return True

@set_callback(STATE, 'oncapturing')
def beforecapture(e):
    pass

@set_callback(STATE, 'oncapture')
def capture_image(e):
    stream = CAMERA.capture()
    screen.status('Processing...')
    CAMERA.stop_preview()
    text = OUTPUT_CONVERTOR.convert(stream)
    screen.output(text, center=True)
    if e.output:
        STATE.trigger('output', text=text, share=e.share)
    else:
        STATE.idle()

@set_callback(STATE, 'onidle')
def idle(e):
    sleep(3)
    STATE.done()

@set_callback(STATE, 'onoutput')
def output_image(e):
    text = e.text
    share = e.share
    image = RASTERIZER.draw_image(text, footer=output.footer_line())
    image = raster.save_image(image).getvalue()
    try:
        output.save_image(image)
        if share:
            try:
                screen.status('Printing...', newline=False)
                output.printjob(image)
            except Exception as e:
                print(e)
            try:
                screen.status('Sending to Twitter...')
                output.tweet(image, text=next(STATUS_GEN))
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        # raise e
    STATE.idle()

def quit():
    screen.status('Quitting.')
    CAMERA.stop()
    # XXX This is needed to release capture
    for thread in THREADS:
        try:
            thread.stop()
        except Exception as e:
            print('Error stopping the thread: {}. Feel free to ignore that.'.format(e))
        THREADS.remove(thread)
    QUIT_LOCK.release()

ACTIONS_MAP = {
    'c': Observable.to_async(lambda: STATE.capture(output=True,share=True), Scheduler.new_thread),
    't': Observable.to_async(lambda: STATE.capture(output=False,share=True), Scheduler.new_thread),
    's': Observable.to_async(lambda: STATE.capture(output=True,share=False), Scheduler.new_thread),
    'p': CAMERA.toggle_preview,
    'q': quit,
}

def run_action(key):
    if key in ACTIONS_MAP:
        # print('running action: ', key)
        ACTIONS_MAP[key]()
    else:
        print('unknown action: ', key)

def main():
    mo, clicks = observe_mouse(config.INPUT_CAPTURE_MOUSE)
    clicks = clicks.map(lambda click: 'c')
    ko, strokes = observe_keyboard(config.INPUT_CAPTURE_KEYBOARD)
    THREADS.extend((mo, ko))

    obs = Observable.merge(clicks, strokes)

    if config.INPUT_READCH:
        gcho, ch = observe_getch()
        THREADS.append(gcho)
        obs = obs.merge(ch)

    obs.subscribe(Observable.to_async(run_action), lambda e: print(e))
    STATE.done()
    # Block on semaphore and keep the rest of threads do the thingy
    QUIT_LOCK.acquire()

try:
    main()
except Exception as e:
    quit()
    raise e
