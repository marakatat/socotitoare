import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

# Enables the Media Keys extension for volume control
keyboard.extensions.append(MediaKeys())

# --- Matrix Configuration ---
# Cols: COL0=D27, COL1=D26, COL2=D4
# Rows: ROW0=D29, ROW1=D28 
# Diodes point from Col to Row (COL2ROW)
keyboard.col_pins = (board.D27, board.D26, board.D4)
keyboard.row_pins = (board.D29, board.D28)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- Rotary Encoder Configuration ---
# Encoder pins: A=D2, B=D1
# The encoder switch is in the matrix at (ROW0, COL2)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.D2, board.D1, None, False),)

# --- RGB Configuration ---
# SK6812 LEDs on D3
# Mapping: Key 0->LED 0 ... Key 4->LED 4
rgb = RGB(pixel_pin=board.D3, num_pixels=5, val_limit=100, hue_default=0, sat_default=255, val_default=100)
keyboard.extensions.append(rgb)

# --- Coordinate Mapping ---
# Reorders logical keys to match LED order: SW1, SW2, SW3, SW4, Enc
# Matrix Scan Order (Cols D27, D26, D4; Rows D29, D28):
# 0: R0-C0 (SW1) -> Map 0
# 1: R0-C1 (SW2) -> Map 1
# 2: R0-C2 (Enc) -> Map 4 (Last)
# 3: R1-C0 (SW3) -> Map 2
# 4: R1-C1 (SW4) -> Map 3
# 5: R1-C2 (Empty)-> Map 5
keyboard.coord_mapping = [
    0,  # SW1
    1,  # SW2
    4,  # Enc
    2,  # SW3
    3,  # SW4
    5   # Empty
]

# --- Keymap ---
# Logical Order: SW1, SW2, SW3, SW4, Enc, Empty
keyboard.keymap = [
    [
        KC.N7,    # SW1
        KC.N8,    # SW2
        KC.N4,    # SW3
        KC.N5,    # SW4
        KC.MUTE,  # Enc Switch
        KC.NO,    # Empty
    ]
]

# Encoder Rotation Map
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),),
]

if __name__ == '__main__':
    keyboard.go()

