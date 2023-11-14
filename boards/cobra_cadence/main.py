from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

split = Split(split_flip=False, split_type=SplitType.UART, data_pin=keyboard.data_pin, data_pin2=keyboard.data_pin2, uart_flip=False)
keyboard.modules.append(split)

keyboard.keymap = [
    [   # Base
        KC.ESC,                                                                KC.N0,
        KC.Q, KC.W, KC.D,  KC.F,   KC.G,      KC.Y,   KC.U,    KC.R,  KC.L,    KC.J,
        KC.A, KC.S, KC.E,  KC.T,                      KC.N,    KC.I,  KC.O,    KC.H,
        KC.Z, KC.X, KC.C,  KC.V,   KC.B,      KC.P,   KC.M,    KC.K,  KC.COMM, KC.DOT,
                    KC.N1, KC.SPC, KC.TAB,    KC.ENT, KC.BSPC, KC.DEL
    ]
]

if __name__ == '__main__':
    keyboard.go()
