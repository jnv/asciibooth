import aalib
from PIL import Image

# def prepare_image(stream, vsize):
#     print(vsize)
#     return Image.open(stream).convert('L').resize(vsize)

# def convert_stream(stream, width=80, height=40):
#     screen = aalib.AsciiScreen(recommended_width=width, recommended_height=height)
#     image = prepare_image(stream, screen.virtual_size)
#     screen.put_image((0, 0), image)
#     return screen.render()

# def convertor(width, height):
#     return partial(convert_stream, width=width, height=height)

class Convertor:
    def __init__(self, stream_size, size=(80, 40), contrast=100):
        width, height = size
        self.stream_size = stream_size
        self.screen = aalib.AsciiScreen(width=width, height=height)
        self.vsize = self.screen.virtual_size
        self.contrast = contrast

    def prepare_image(self, stream):
        return Image.frombytes(data=stream.getvalue(), mode='RGB', size=self.stream_size).convert('L')

    def convert(self, stream):
        screen = self.screen
        image = self.prepare_image(stream)
        screen.put_image((0, 0), image)
        text = screen.render(dithering_mode=aalib.DITHER_FLOYD_STEINBERG, contrast=self.contrast)
        return text
