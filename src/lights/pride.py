# This file will have some helper funcitons to generate various pride flag patterns.

from shared import gamma_correct_colour

# returns a large prideflag logo
def do_the_gay(num_pixels=300):
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
        # pride_flag[(int(i / 3)) % len(pride_flag)][i % 3] for i in range(num_pixels * 3)
        pride_flag[(int(i / 3)) % len(pride_flag)][i % 3] for i in range(len(pride_flag) * 3)
    ]
    return pixel_set
