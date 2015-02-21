from PIL import Image, ImageFont, ImageDraw, ImageColor, ImageOps
from io import BytesIO
def each_line(text):
    for line in text.splitlines():
        yield line

class TextImage:
    def __init__(self, font_path, background='#000000', foreground='#ffffff'):
        self.font = ImageFont.load(font_path)
        self.background = ImageColor.getrgb(background)
        self.foreground = ImageColor.getrgb(foreground)
        self.line_space = 2
        self.border = 10
        _, self.line_height = self.font.getsize('Mj')

    def text_size(self, line_space, text=None, lines=None):
        if lines is None:
            lines = text.splitlines()

        width, _ = self.font.getsize(lines[0])
        lcount = len(lines)
        height = lcount*self.line_height + lcount+line_space

        return width, height

    def draw_footer(self, texts, width, foreground, background):
        size = (width, self.line_height)
        left, right = texts

        image = Image.new('RGB', size, background)
        draw = ImageDraw.Draw(image)

        # calculate X coordinate for the right text
        rwidth, _ = draw.textsize(right, self.font)
        rx = width - rwidth

        draw.text((0,0), left, font = self.font, fill = foreground)
        draw.text((rx, 0), right, font = self.font, fill = foreground)

        del draw

        return image

    def draw_text(self, text):
        lines = text.splitlines()
        size = self.text_size(line_space=self.line_space, lines=lines)
        image = Image.new('RGB', size, self.background)
        draw = ImageDraw.Draw(image)

        ls_half = self.line_space / 2
        text_y = ls_half

        for line in lines:
            draw.text((0, text_y), line, font = self.font, fill = self.foreground)
            text_y += self.line_height + ls_half
        del draw

        return image

    def merge_images(self, top, bottom):
        top_w, top_h = top.size
        bot_w, bot_h = bottom.size
        size = (top_w, top_h + bot_h)
        bot_pos = (0, top_h)

        merged_im = Image.new('RGB', size)
        merged_im.paste(top, (0, 0))
        merged_im.paste(bottom, bot_pos)

        return merged_im

    def draw_image(self, text, footer, greyscale=True):
        im_text = self.draw_text(text)
        # im_text.show()
        footer_width, _ = im_text.size
        footer_bg = self.foreground
        im_footer = self.draw_footer(footer, footer_width, foreground=self.background, background=footer_bg)
        # im_footer.show()

        im_text = ImageOps.expand(im_text, border=self.border,fill=self.background)
        im_footer = ImageOps.expand(im_footer, border=self.border,fill=footer_bg)

        merged = self.merge_images(im_text, im_footer)

        if greyscale:
            return merged.convert('L')
        else:
            return merged

def save_image(image, format='PNG'):
    stream = BytesIO()
    image.save(stream, format=format)
    stream.seek(0)

    return stream

if __name__ == '__main__':
    import os
    font_path = os.path.join(os.path.dirname(__file__), '..', 'fonts', '7x13.pil')
    ti = TextImage(font_path=font_path)
    text = "\nBrownAAAjjjjj.\nAAAAAAAAAAAAAAAAAAAAAA.\naa"
    # print(ti.text_size(text))
    ti.draw_image(text, footer=('hello', 'world')).show()

