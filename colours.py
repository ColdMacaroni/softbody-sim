##
# colors.py
# Some colours that can be easily accessed

from pygame import Color
from random import randint

class RGB:
    WHITE = Color(0xFF, 0xFF, 0xFF)
    BLACK = Color(0x00, 0x00, 0x00)
    RED = Color(0xFF, 0x00, 0x00)
    GREEN = Color(0x00, 0xFF, 0x00)
    BLUE = Color(0x00, 0x00, 0xFF)
    LIGHT_GRAY = Color(0xDD, 0xDD, 0xDD)

    def random():
        return Color(randint(0x00, 0xFF), randint(0x00, 0xFF), randint(0x00, 0xFF))

