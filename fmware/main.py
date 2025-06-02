import board
import busio


from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.scanners import DiodeOrientation

from kmk.modules.encoder import EncoderHandler

from kmk.extensions.RGB import RGB

from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

print(dir(board))


keyboard = KMKKeyboard()

# confgiure macros and keymap
macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


PASTE = KC.MACRO(Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD))

COPY = KC.MACRO(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD))

CUT = KC.MACRO(Press(KC.LCMD), Tap(KC.X), Release(KC.LCMD))

DEL_LINE = KC.MACRO(
    Press(KC.LCMD), Press(KC.SHIFT), Tap(KC.K), Release(KC.SHIFT), Release(KC.LCMD)
)

PREV_PAGE = KC.MACRO(Press(KC.LALT), Tap(KC.LEFT), Release(KC.LALT))

NEXT_PAGE = KC.MACRO(Press(KC.LALT), Tap(KC.RIGHT), Release(KC.LALT))

keyboard.keymap = [[PREV_PAGE, PASTE, NEXT_PAGE], [COPY, DEL_LINE, CUT]]


# configure rotary encoder
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    board.D10,
    board.D9,
    board.D3,
)
encoder_handler.map = [(KC.VOLD, KC.VOLU, KC.MUTE)]


# configure single led
rgb = RGB(pixel_pin=board.D6, num_pixels=1)
keyboard.extensions.append(rgb)

rgb.set_rgb_fill((255, 0, 0))  # Set the color to red

# configure oled 1306ssd display
driver = SSD1306(i2c=busio.I2C(board.GP_SCL, board.GP_SDA))

display = Display(
    display=driver,
    width=128,
    height=32,
    flip=False,
    brightness=1,
    dim_time=20,
    dim_target=0.2,
    off_time=60,
    powersave_dim_time=10,  # time in seconds to reduce screen brightness
    powersave_dim_target=0.1,  # set level for brightness decrease
    powersave_off_time=30,  # time in seconds to turn off screen
)

display.entries = [TextEntry(text="This works!", x=0, y=0)]

keyboard.extensions.append(display)


if __name__ == "__main__":
    keyboard.go()
