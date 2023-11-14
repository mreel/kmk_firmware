from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split, SplitType
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()

# Enable necessary modules
split = Split(split_flip=False, split_type=SplitType.UART, data_pin=keyboard.data_pin, data_pin2=keyboard.data_pin2, uart_flip=False)
holdtap = HoldTap()
#holdtap.tap_time = 300
keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.modules.append(holdtap)

# Custom keycodes
_______ = KC.TRNS
MO_NUM = KC.MO(1)
KC.LOPT = KC.LALT
KC.ROPT = KC.RALT

## Holdtap
T_LSFT = KC.HT(KC.T, KC.LSFT)
E_LCMD = KC.HT(KC.E, KC.LCMD)
S_LOPT = KC.HT(KC.S, KC.LALT)
A_LCTL = KC.HT(KC.A, KC.LCTL)
N_RSFT = KC.HT(KC.N, KC.RSFT)
I_RCMD = KC.HT(KC.I, KC.RCMD)
O_ROPT = KC.HT(KC.O, KC.RALT)
H_RCTL = KC.HT(KC.H, KC.RCTL)

keyboard.keymap = [
    [   # Base
        KC.ESC,                                                                            MO_NUM,
        KC.Q,    KC.W,    KC.D,    KC.F,    KC.G,      KC.Y,    KC.U,    KC.R,    KC.L,    KC.J,
        A_LCTL,  S_LOPT,  E_LCMD,  T_LSFT,                      N_RSFT,  I_RCMD,  O_ROPT,  H_RCTL,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,      KC.P,    KC.M,    KC.K,    KC.COMM, KC.DOT,
                          KC.N1,   KC.SPC,  KC.TAB,    KC.ENT,  KC.BSPC, KC.DEL
    ],

    [   # Numbers
        _______,                                                                           _______,
        _______, KC.N7,   KC.N8,   KC.N9,   _______,   _______, _______, _______, _______, _______,
        KC.N0,   KC.N4,   KC.N5,   KC.N6,                       _______, _______, _______, _______,
        _______, KC.N1,   KC.N2,   KC.N3,   _______,   _______, _______, _______, _______, _______,
                          _______, _______, _______,   _______, _______, _______
    ]
]

if __name__ == '__main__':
    keyboard.go()
