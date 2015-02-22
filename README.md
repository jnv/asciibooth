# ASCII Booth

Raspberry Pi photo booth which converts a photo to text characters, prints out the result and sends it to Twitter.

## Requirements

* [Raspberry Pi](http://www.raspberrypi.org/) (Tested on 1st gen B and B+)
* [Raspberry Pi Camera](http://www.raspberrypi.org/products/camera-module/)
* (Optional) Printer (anything supported by CUPS on Linux)
* [Raspbian](http://www.raspbian.org/) (Tested with [official version](http://www.raspberrypi.org/downloads/)) with a graphical environment (X server) enabled (Tested with wheezy)

## Setup

Either clone or [download](https://github.com/jnv/asciibooth/archive/master.zip) the repository to your Raspberry Pi.

Once it is cloned and extracted, run `install.sh` script in a terminal. This will:

* Updates APT cache and upgrades packages to latest versions,
* install Python 3, PIP, build dependencies and a few packages available via repository,
* install remaining packages via Pip from `requirements.txt`

## Executing

You can run the application as a Python module. `cd` into the directory where you have cloned or extracted the repository and run:

```
python3 -m asciibooth
```

(This will execute file `asciibooth/__main__.py`).

`./run.sh` script is provided for a production usage. It will execute `mrxvt` virtual terminal application with a configuration file `mrxvtrc`; this gives us a greater control over the terminal look.

### Executing via SSH

If you are connected to your Pi via SSH, the application will try to grab an input from the X server, but fail. This can be easily fixed by running the following line after logging in:

```
export DISPLAY=:0
```

## Usage

After initialization the application starts the camera preview on a connected display, waiting for a user's input to take a photo.

The captured photo is saved to `images/` folder in PNG format, and sent to Twitter and default printer (via `lpr` command). The converted picture is shown for a short time in the terminal output.

### Control

Use the following keyboard keys:

* `q` – quits the application
* `p` – toggles camera preview
* `t` – takes a test photo photo without saving or sending it out
* `s` – takes and saves the photo without sending it out
* `c` – captures the photo, saves it, and sends it out to Twitter and a printer

Left and right mouse button behaves the same way as the `c` key. The basic idea is that you will unplug the keyboard and keep just the mouse in the photobooth.

Same keyboard commands can be sent via an SSH session from the terminal. Note that this may lead to a duplication of input commands if you run the terminal directly on Pi and keyboard capture is disabled (see below).

### Input Capture

By default, mouse and keyboard capture is enabled for X server. All keyboard and mouse events are sent _only_ to the application, thus you can't use desktop normally. Note that this may leave your desktop unresponsive if the application is killed abruptly – using `q` command is strongly recommended. This behaviour can be disabled in configuration file (see below).

## Configuration

The configuration is stored in a Python script `asciibooth/config.py`. See the comments in the corresponding file.

The following configuration constants control the input behaviour:

* `INPUT_READCH` – use `getch` to read input from terminal; required for control via SSH
* `INPUT_CAPTURE_MOUSE` – capture the mouse; no other application (including desktop) will receive mouse clicks while the asciibooth is running
* `INPUT_CAPTURE_KEYBOARD` – capture the keyboard; no other application (including desktop) will keyboard input while the asciibooth is running

### Twitter Credentials

To send pictures to Twitter, [register a new Twitter application](https://apps.twitter.com/) with read and write permissions. Once created, in “Keys and Access Tokens” generate an access token for your account.

You need 4 tokens: _consumer key_, _consumer secret_, _access token_, and _access token secret_. You can either fill in these details in `TWITTER_AUTH` section of the configuration file.

By default the Twitter credentials are read from the following _environment variables_:

* `TWITTER_CONSUMER_KEY` (consumer key)
* `TWITTER_CONSUMER_SECRET` (consumer secret)
* `TWITTER_TOKEN` (access token)
* `TWITTER_TOKEN_SECRET` (access token secret)

**Note:** These tokens can be used to control your Twitter account. Do not share them with anyone unauthorized and don't commit them to a repository.

### Tweet Messages

A tweet with a photo may contain a text – part can be constant (e.g. a hashtag) and part can be random. Random message may be omitted in most cases to prevent repetition.

The following configuration options control tweets' text:

* `TWEET_FIXED` – fixed part of the tweet, usually a hashtag
* `TWEET_MESSAGES` – array of messages from which a random message will be chosen randomly; are messages are used before recycling and no message will be repeated consecutively

The following variabless control the chance of using the text:

* `TWEET_CHANCE_INITIAL` – what is the chance that random message will be added to the tweet, after the last tweet contained a message?
  * `0` by default: there is 0% chance that message will contain a random message
* `TWEET_CHANCE_INCREMENT` – increase of random message being added with every tweet
  * `0.25` by default: chance of adding a message raises by 25% with every tweet (i.e. message will be sent at least every 4th tweet)

## Development Notes

[`.direnv`](http://direnv.net/) script is provided for a virtualenv support; the environment will be created in `env/` dir. Pip is installed separately into the environment, because `virtualenv` doesn't allow linking to a `pip` corresponding to the alternative Python version.

The script assumes these applications are available on your system:

* Python 3.2 available as `python3.2`; for Ubuntu, you can use an excellent [Dead Snakes](https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes) repository.
  * Python 3.2 is the default version of Python 3 in Raspbian Wheezy
* `virtualenv` executable 

## Projects Used

* [AA-lib](http://aa-project.sourceforge.net/), _the_ image to ASCII conversion library started by Jan Hubicka in 1997 (!); see also the [BB demo](https://www.youtube.com/watch?v=FLlDt_4EGX4).
  * [python-aalib](http://jwilk.net/software/python-aalib) by Jan Wilk
* [RxPY](https://github.com/ReactiveX/RxPY) from the [ReactiveX](http://reactivex.io/) project
* [picamera](https://picamera.readthedocs.org/) for camera manipulation (the major reason why this thing is in Python)
* [PyUserInput](https://github.com/SavinaRoja/PyUserInput) for grabbing the input from the X server
* [Pillow](https://pillow.readthedocs.org/) for image manipulation
* [fysom](https://github.com/mriehl/fysom) for state management
* [Python Twitter Tools](http://mike.verdone.ca/twitter/) for Twitter communication
* [blessings](https://github.com/erikrose/blessings) for output formatting

## TODO

* Use Rx for all components; currently this is just a fancier way to pass events across threads.
* Use AsyncIO once Jessie is stable (or we'll switch to a different OS)
