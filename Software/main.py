import board

import digitalio 


from kmk.modules.oneshot import OneShot




from kb import KMKKeyboard, isRight

from storage import getmount



from kmk.keys import KC

from kmk.modules.layers import Layers

from kmk.modules.split import Split, SplitSide, SplitType

from kmk.modules.mouse_keys import MouseKeys

from kmk.extensions.media_keys import MediaKeys

from kmk.handlers.sequences import simple_key_sequence





keyboard = KMKKeyboard()

keyboard.tap_time = 100



layers = Layers()



split_side = SplitSide.RIGHT if isRight else SplitSide.LEFT



data_pin = board.GP1 if split_side == SplitSide.LEFT else board.GP0

data_pin2 = board.GP0 if split_side == SplitSide.LEFT else board.GP1



split = Split(

    split_side=split_side,

    split_type=SplitType.UART,

    split_flip=False,

    data_pin=data_pin,

    data_pin2=data_pin2

)

keyboard.modules = [layers, split, MouseKeys(),MediaKeys(),OneShot()]





# Select line 

SEL_LINE = simple_key_sequence(

        (

                KC.END,

                KC.LSHIFT(KC.HOME)

        )

)






LOWER =KC.LT(1,KC.OS(KC.MO(1),tap_time=1000))

RAISE =KC.LT(2,KC.OS(KC.MO(2),tap_time=1000))



OS_LCTL = KC.OS(KC.LCTL, tap_time=None)
keyboard.keymap = [

    [  #QWERTY

        KC.ESC,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\

        KC.MB_LMB,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\

                   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH,\

                                   KC.LCTL, KC.OS(KC.LSFT),   LOWER,  KC.SPACE,     KC.ENT,   RAISE,  KC.LALT, KC.TAB

    ],

    [  #LOWER

        KC.MB_RMB,   KC.N1,          KC.N2,           KC.N3,           KC.N4,           KC.N5,                           KC.N6,               KC.N7,           KC.N8,     KC.N9,    KC.N0,            KC.DEL,\

        KC.NO,       KC.LCTL(KC.A),  KC.LCTL(KC.S),   KC.NO,           SEL_LINE,        KC.HOME,                         KC.AUDIO_VOL_UP,     KC.LEFT,         KC.UP,     KC.RIGHT, KC.NO,            KC.GRAVE,  \

                     KC.LCTL(KC.Z),  KC.LCTL(KC.X),   KC.LCTL(KC.C),   KC.LCTL(KC.V),   KC.END,                          KC.AUDIO_VOL_DOWN,   KC.AUDIO_MUTE,   KC.DOWN,   KC.NO,    KC.LCTL(KC.SLSH),\
 
                                     KC.LCTL,         KC.LSFT,         KC.NO,           KC.SPACE,                        KC.ENT,              RAISE,           KC.LALT,   KC.RSFT

    ],

    [  #RAISE

        KC.MB_RMB, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                        KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,  KC.DEL,\

        KC.MB_MMB, KC.F2,     KC.F5,   KC.F9,  KC.NO,  KC.SLASH,                       KC.MINS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,  KC.GRV,\

                   KC.F12,    KC.F11,  KC.F10, KC.NO,  KC.COLON,                       KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS,\

                           KC.LCTL, KC.LSFT,   LOWER,  KC.SPACE,                       KC.ENT,   RAISE,  KC.LALT, KC.TILD

    ]

]



if __name__ == '__main__':

    keyboard.go()

