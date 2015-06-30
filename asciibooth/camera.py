import io
# import time
import picamera
from . import config

class Camera:
    def __init__(self):
        self.camera = picamera.PiCamera(resolution=config.CAPTURE_RESOLUTION)
        self.preview_alpha = 200

    def capture(self):
        stream = io.BytesIO()
        self.camera.capture(stream, 'rgb', resize=config.CAPTURE_RESIZE)
        stream.seek(0)
        return stream

    def toggle_preview(self):
        if self.camera.preview is None:
            self.start_preview()
        else:
            self.stop_preview()

    def start_preview(self, alpha=255):
        self.camera.start_preview(hflip = True)
        self.camera.preview.alpha = alpha

    def stop_preview(self):
        self.camera.stop_preview()

    def stop(self):
        self.camera.close()
