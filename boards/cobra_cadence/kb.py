import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
    row_pins = (board.D5, board.D8, board.D9, board.D10)

    diode_orientation = DiodeOrientation.COL2ROW

    data_pin = board.D7
    data_pin2 = board.D6

    coord_mapping = [
         0,                                     24,
         5,  1,  2,  3,  4,     20, 21, 22, 23, 29,
        10,  6,  7,  8,             26, 27, 28, 34,
        15, 11, 12, 13,  9,     25, 31, 32, 33, 39,
                17, 18, 19,     35, 36, 37
    ]