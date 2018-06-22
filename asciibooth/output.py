# encoding: UTF-8
import time
from . import config
from os import path
import twitter
import subprocess

def footer_line():
    date = time.strftime("%d/%m/%Y %H.%M:%S")

    return config.RASTER_FOOTER, date

def save_image(image):
    fname = time.strftime("%Y-%m-%d_%H-%M-%S")
    fpath = path.join(config.RASTER_OUTPUT, fname) + '.' + config.RASTER_FORMAT
    open(fpath, 'wb').write(image)

    return fpath

def print_params(options):
    def assign(k, v):
        if v is None:
            option = "-o {}".format(k)
        else:
            option = "-o {}={}".format(k, v)
        return option
    args = [assign(k, v) for k, v in options.items()]
    return ' '.join(args)

PRINT_ARGS = print_params(config.PRINTER_OPTIONS)
def printjob(image):
    stdin = subprocess.Popen(["lpr", PRINT_ARGS], stdin=subprocess.PIPE).stdin
    stdin.write(image)
    stdin.close()

def tweet_text():
    pass

def tweet(image, text=''):
    t_auth = twitter.OAuth(**config.TWITTER_AUTH)
    t = twitter.Twitter(auth=t_auth)
    t_upload = twitter.Twitter(domain='upload.twitter.com', auth=t_auth)
    img_id = t_upload.media.upload(media=image)["media_id_string"]
    t.statuses.update(status=text, media_ids=img_id)
