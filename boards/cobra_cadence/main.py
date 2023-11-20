from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.split import Split, SplitType
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.modules.tapdance import TapDance

from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
# Layers
NUM = 1
NAV = 2

# Enable necessary modules & extensions ------------
## Config
split = Split(split_flip=False, split_type=SplitType.UART, data_pin=keyboard.data_pin, data_pin2=keyboard.data_pin2, uart_flip=False)

holdtap = HoldTap()
holdtap.tap_time = 200

tapdance = TapDance()
tapdance.tap_time = 175

## Modules
keyboard.modules.append(tapdance)
keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.modules.append(holdtap)

## Extensions
keyboard.extensions.append(MediaKeys())
# --------------------------------------------------

# Custom keycodes ----------------------------------
_______ = KC.TRNS
MO_NUM = KC.MO(NUM)
KC.LOPT = KC.LALT
KC.ROPT = KC.RALT


## Holdtap
### Home row mods
T_LSFT = KC.HT(KC.T, KC.LSFT, prefer_hold=False)
E_LCMD = KC.HT(KC.E, KC.LCMD, prefer_hold=False)
S_LOPT = KC.HT(KC.S, KC.LALT, prefer_hold=False)
A_LCTL = KC.HT(KC.A, KC.LCTL, prefer_hold=False)
N_RSFT = KC.HT(KC.N, KC.RSFT, prefer_hold=False)
I_RCMD = KC.HT(KC.I, KC.RCMD, prefer_hold=False)
O_ROPT = KC.HT(KC.O, KC.RALT, prefer_hold=False)
H_RCTL = KC.HT(KC.H, KC.RCTL, prefer_hold=False)

## Tapdance
TAB_ALF = KC.TD(KC.TAB, KC.HT(KC.LGUI(KC.SPC), KC.MEH))

## Layers
SPC_NUM = KC.TD(KC.SPC, KC.TT(NUM))
ENT_NAV = KC.HT(KC.ENT, KC.MO(NAV))
# --------------------------------------------------

# Keymap -------------------------------------------
keyboard.keymap = [
    [   # Base
        KC.ESC,                                                                            KC.MPLY,
        KC.Q,    KC.W,    KC.D,    KC.F,    KC.G,      KC.Y,    KC.U,    KC.R,    KC.L,    KC.J,
        A_LCTL,  S_LOPT,  E_LCMD,  T_LSFT,                      N_RSFT,  I_RCMD,  O_ROPT,  H_RCTL,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,      KC.P,    KC.M,    KC.K,    KC.COMM, KC.DOT,
                          KC.N1,   SPC_NUM, TAB_ALF,   KC.BSPC, ENT_NAV, KC.DEL
    ],

    [   # Numbers
        _______,                                                                           _______,
        _______, KC.N7,   KC.N8,   KC.N9,   _______,   _______, _______, _______, _______, _______,
        KC.N0,   KC.N4,   KC.N5,   KC.N6,                       _______, _______, _______, _______,
        _______, KC.N1,   KC.N2,   KC.N3,   _______,   _______, _______, _______, _______, _______,
                          _______, _______, _______,   _______, _______, _______
    ],

    [   # Navigation
        _______,                                                                           _______,
        _______, _______, _______, _______, _______,   _______, _______, _______, _______, _______,
        _______, _______, _______, _______,                     KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
        _______, _______, _______, _______, _______,   _______, _______, _______, _______, _______,
                          _______, _______, _______,   _______, _______, _______
    ]
]
# --------------------------------------------------

if __name__ == '__main__':
    keyboard.go()

'''
[   # lorem
        _______,                                                                           _______,
        _______, _______, _______, _______, _______,   _______, _______, _______, _______, _______,
        _______, _______, _______, _______,                     _______, _______, _______, _______,
        _______, _______, _______, _______, _______,   _______, _______, _______, _______, _______,
                          _______, _______, _______,   _______, _______, _______
    ]
'''