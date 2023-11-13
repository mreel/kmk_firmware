import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
    row_pins = (board.D5, board.D8, board.D9, board.D10)

    diode_orientation = DiodeOrientation.COL2ROW

    data_pin = board.D7
    data_pin2 = board.D6