# This file will have some helper funcitons to generate various pride flag patterns.

from shared import gamma_corrected_colour

# returns a large prideflag logo
def do_the_gay():
    pride_flag = [
        (228, 3, 3),
        (255, 140, 0),
        (255, 237, 0),
        (0, 128, 38),
        (36, 64, 142),
        (73, 29, 82),
    ]
    for i in range(len(pride_flag)):
        pride_flag[i] = gamma_correct_colour(pride_flag[i])
    pixel_set = [
        pride_flag[(int(i / 3)) % len(pride_flag)][(1 - i) % 3] for i in range(900)
    ]
    buffer = bytearray(pixel_set)
    pixels._transmit(buffer)
