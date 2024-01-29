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
SYM = 2
FUN = 3
GAM = 4
NAV = 5

# Enable necessary modules & extensions ------------
## Config
split = Split(split_flip=False, split_type=SplitType.UART, data_pin=keyboard.data_pin, data_pin2=keyboard.data_pin2, uart_flip=False)

holdtap = HoldTap()
holdtap.tap_time = 200

tapdance = TapDance()
tapdance.tap_time = 200

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
KC_ALF = KC.LGUI(KC.SPC)
KC_BWRD = KC.LALT(KC.BSPC)


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

### Layers
SPC_NUM = KC.HT(KC.SPC, KC.TT(NUM))
ENT_NAV = KC.LT(NAV, KC.ENT)
BSPC_SM = KC.LT(SYM, KC.BSPC)
DEL_FUN = KC.LT(FUN, KC.DEL)
LAY_GAM = KC.TG(GAM)

## Tapdance
#\\ TAB_ALF = KC.TD(KC.TAB, KC.HT(KC.LGUI(KC.SPC), KC.MEH))


# --------------------------------------------------

# Keymap -------------------------------------------
keyboard.keymap = [
    [   # Base (0)
        KC.ESC,                                                                            LAY_GAM,
        KC.Q,    KC.W,    KC.D,    KC.F,    KC.G,      KC.Y,    KC.U,    KC.R,    KC.L,    KC.J,
        A_LCTL,  S_LOPT,  E_LCMD,  T_LSFT,                      N_RSFT,  I_RCMD,  O_ROPT,  H_RCTL,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,      KC.P,    KC.M,    KC.K,    KC.COMM, KC.DOT,
                          KC_ALF,  SPC_NUM, KC.TAB,   BSPC_SM, ENT_NAV, DEL_FUN
    ],

    [   # Numbers (1)
        _______,                                                                           _______,
        _______, KC.N7,   KC.N8,   KC.N9,   _______,   _______, _______, _______, _______, _______,
        _______, KC.N4,   KC.N5,   KC.N6,                       KC.RSFT, KC.RCMD, KC.RALT, KC.RCTL,
        KC.N0,   KC.N1,   KC.N2,   KC.N3,   _______,   _______, _______, _______, _______, _______,
                          _______, _______, _______,   KC_BWRD, _______, _______
    ],

    [   # Symbols (2)
        _______,                                                                           _______,
        KC.GRV,  KC.LBRC, KC.RBRC, KC.EXLM, KC.AMPR,   _______, _______, _______, _______, _______,
        KC.SCLN, KC.LPRN, KC.RPRN, KC.SLSH,                     KC.RSFT, KC.RCMD, KC.RALT, KC.RCTL,
        KC.PAST, KC.MINS, KC.EQL,  KC.BSLS, KC.CIRC,   _______, _______, _______, _______, _______,
                          KC.HASH, KC.AT,   KC.PERC,   _______, _______, _______
    ],

    [   # Function (3)
        _______,                                                                           _______,
        _______, KC.F7,   KC.F8,   KC.F9,   _______,   _______, _______, _______, _______, _______,
        _______, KC.F4,   KC.F5,   KC.F6,                       KC.RSFT, KC.RCMD, KC.RALT, KC.RCTL,
        _______, KC.F1,   KC.F2,   KC.F3,   _______,   _______, _______, _______, _______, _______,
                          KC.F10,  KC.F11,  KC.F12,    _______, _______, _______
    ],

    [   # Gaming (4))
        _______,                                                                           _______,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,      _______, _______, _______, _______, _______,
        KC.LCTL, KC.A,    KC.S,    KC.D,                        _______, _______, _______, _______,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,      _______, _______, _______, _______, _______,
                          _______, KC.SPC,  _______,   _______, _______, _______
    ],

    [   # Navigation (5)
        _______,                                                                           _______,
        _______, _______, _______, _______, _______,   _______, _______, _______, _______, _______,
        KC.RCTL, KC.LALT, KC.LCMD, KC.LSFT,                     KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
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