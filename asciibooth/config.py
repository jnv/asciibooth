# encoding: UTF-8
from os import path, environ

# Project's root directory for access to images dir and fonts
BASE_PATH=path.realpath(path.join(path.dirname(__file__), '..'))


## Input options
# Whether to capture mouse/keyboard – no other application will receive input
INPUT_CAPTURE_MOUSE=True
INPUT_CAPTURE_KEYBOARD=True
# Read characters from TTY; useful for interaction through SSH
# If you run application directly on Pi and set INPUT_CAPTURE_KEYBOARD, set this one to False
INPUT_READCH=True
# FIXME: Unused
# INPUT_THROTTLE=1000


## ASCII conversion
# Contrast for AAlib conversion
RENDER_CONTRAST = 56
# Number of columns and lines for ASCII output
RENDER_CHARS = (80, 40)

## Camera capture
# based on 7x14 font:ratio is 1x2
# Photo resolution
CAPTURE_RESOLUTION = (1600, 1400)
#CAPTURE_RESOLUTION = (RENDER_CHARS[0]*5, RENDER_CHARS[1]*10)
# Target photo size for conversion by AAlib; this is done in GPU
CAPTURE_RESIZE = tuple(i * 2 for i in RENDER_CHARS)
#CAPTURE_RESIZE = (RENDER_CHARS[0], RENDER_CHARS[1]*2)

## Raster image rendering
# Font to be used in the resulting picture; must be a converted raster font in `pil` format for Pillow
#RASTER_FONT = path.join(BASE_PATH, 'fonts', '6x12.pil')
RASTER_FONT = path.join(BASE_PATH, 'fonts', '7x13.pil')

# Target directory for rasterized images
RASTER_OUTPUT = path.join(BASE_PATH, 'images')
RASTER_FORMAT = 'png'
# Left part of the image footer
RASTER_FOOTER = "@NMIselfie // New Media Inspiration 2015"

## Printing
# These options will be passed to `lpr` command as -o
# use value None if the option has no parameters
PRINTER_OPTIONS = {
    'scaling': 50,
    'position': 'center',
    'media': 'A4',
    'orientation-requested': 3
}

## Twitter credentials; by default, env variables are used
TWITTER_AUTH = {
    'token': environ.get('TWITTER_TOKEN'),
    'token_secret': environ.get('TWITTER_TOKEN_SECRET'),
    'consumer_key': environ.get('TWITTER_CONSUMER_KEY'),
    'consumer_secret': environ.get('TWITTER_CONSUMER_SECRET')
}

## Tweet message control
# what is the chance that random message will be added to the tweet, after the last tweet contained a message?
TWEET_CHANCE_INITIAL = 0
# increase of random message being added with every tweet
TWEET_CHANCE_INCREMENT = 0.25
# Fixed part of the message; usually a hashtag
TWEET_FIXED = "#asciibooth"
# Pool of messages to be used in a tweet
# must be an array (notice splitlines at the end of the string)
TWEET_MESSAGES = """\
Smile, you are in the Cloud
You have been digitized!
NSA is proud of you…
Better apply some filters!
No to sem neviděl.
Better than the real life
Almost real life resolution
Say A Say S say C and double I
Red eyes correction applied.
ASCII in my soul…
+10 SWAG added
I have found your character.
meh.
Lucky numbers: -5, ¾, 2015
New Media? Not for me…
Encoded belle
We heard you like letters…
Whoa.
""".splitlines()
