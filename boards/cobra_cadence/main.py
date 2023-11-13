from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

split = Split(split_flip=False, split_type=SplitType.UART, data_pin=keyboard.data_pin, data_pin2=keyboard.data_pin2, uart_flip=False)
keyboard.modules.append(split)

keyboard.keymap = [
    [KC.ESC, KC.W, KC.D, KC.F, KC.G, KC.Y, KC.U, KC.R, KC.L, KC.N0,
     KC.Q, KC.S, KC.E, KC.T, KC.B, KC.P, KC.N, KC.I, KC.O, KC.J,
     KC.A, KC.X, KC.C, KC.V, KC.NO, KC.NO, KC.M, KC.K, KC.COMM, KC.H,
     KC.Z, KC.NO, KC.N1, KC.SPC, KC.N2, KC.N3, KC.ENT, KC.BSPC, KC.NO, KC.DOT]
]

if __name__ == '__main__':
    keyboard.go()
