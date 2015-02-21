import sys, termios

# From http://docs.python.org/faq/library#how-do-i-get-a-single-keypress-at-a-time
def getchgen():
    fd = sys.stdin.fileno()
    oldattr = termios.tcgetattr(fd)
    # oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    newattr = termios.tcgetattr(fd)
    newattr[3] &= ~termios.ICANON
    newattr[3] &= ~termios.ECHO
    def getch():
        try:
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            c = sys.stdin.read(1)
            return c
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldattr)

    def reset():
        termios.tcsetattr(fd, termios.TCSADRAIN, oldattr)


    return getch, reset
