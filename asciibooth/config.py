# encoding: UTF-8
from os import path, environ

BASE_PATH=path.realpath(path.join(path.dirname(__file__), '..'))
CAPTURE_FORMAT = 'rgb'
DECODE_MODE = 'RGB'
RENDER_CONTRAST = 56
RENDER_CHARS = (80, 40)
INPUT_CAPTURE_MOUSE=True
INPUT_CAPTURE_KEYBOARD=True
INPUT_READCH=True # Read characters from TTY; useful for interaction through SSH
# Throttle mouse clicks
INPUT_THROTTLE=1000
# based on 7x14 font:ratio is 1x2
# capture larger photo and resize it in GPU
# CAPTURE_RESOLUTION = (RENDER_CHARS[0]*5, RENDER_CHARS[1]*10)
CAPTURE_RESOLUTION = (1600, 1400)
CAPTURE_RESIZE = tuple(i * 2 for i in RENDER_CHARS)
# CAPTURE_RESIZE = (800, 800)
# CAPTURE_RESIZE = (RENDER_CHARS[0], RENDER_CHARS[1]*2)

# RASTER_FONT = path.join(BASE_PATH, 'fonts', '6x12.pil')
RASTER_FONT = path.join(BASE_PATH, 'fonts', '7x13.pil')

RASTER_OUTPUT = path.join(BASE_PATH, 'images')
RASTER_FORMAT = 'png'
RASTER_FOOTER = "@NMIselfie // New Media Inspiration 2015"

TWITTER_AUTH = {
    'token': environ['TWITTER_TOKEN'],
    'token_secret': environ['TWITTER_TOKEN_SECRET'],
    'consumer_key': environ['TWITTER_CONSUMER_KEY'],
    'consumer_secret': environ['TWITTER_CONSUMER_SECRET']
}
PRINTER_OPTIONS = {
    'scaling': 50,
    'position': 'center',
    'media': 'A4',
    'orientation-requested': 3
}

TWEET_FIXED = "#NMI15 #SNMselfie"
TWEET_MESSAGES = """\
Smile, you are in the Cloud
You have been digitized!
Human character detected
NSA is proud of you…
Better apply some filters!
No to sem neviděl.
Better than the real life
Almost real life resolution
Say A Say S say C and double I
Red eyes correction applied.
Check out this new filter on Hipstagram.
ASCII in my soul…
+10 SWAG added
I have found your character.
meh.
Lucky numbers: -5, ¾, 2015
New Media? Not for me…
Encoded belle
We heard you like letters…
Whoa.
This is not the photo you are looking for.
I still prefer EBCDIC though.
Stop touching yourself.
Consciousness upload in progress…
Black and white
You are just a bunch of symbols to me.
I don't like your character.
The character… that I have!
Reply, Star and Retweet!
That's how @Raspberry_Pi sees you.
Instagram? So old school…  @NMIselfie is trendy now!
Look, there's something on your face!
Sort this one out @pixelsorter.
Check this out, @a_quilt_bot!
I think @JPGglitchbot can improve this one.
I think @badpng can improve this one.
Hey @Lowpolybot, check this one out.
Do I see blurry or is it from @imgblur?
.@badpng will help you with that.
And now for @imgshredder!
But will it blend? @imgblender
Let's see what @plaidbot can make out of this one.
Needs more cowbell, @ClipArtBot.
.@pixelsorter Likes This.
Let's see how you will look in the evening, right @imgblur?
We can improve it thoug. @ClipArtBot?
This resolution is too damn high! Fix it @Lowpolybot!
#ascii #aalib #raspberryPi
#nofilter #retro #lowres #asciiart
<SwagOutOfRangeError>
<IndexError: ASCII characters depleted.>
<IOError: lp on fire>
""".splitlines()
