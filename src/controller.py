"""
LED CONTROLLER

Consumes multiple led modules, receives the generated LED data from each 
module, combines them into one 300 pixel wide signal (representing the 
whole LED strip) and writes the information to the LED strips.

I might want to think about generalizable ways in which I can interact with 
modules, the most straight forewards being POLLING, however, data pre-generation
and working with shared queue-dequeues is something to look at lateron.

At first we will probably hard code all the different parts.


NOTE:
I noticed that, when manually filling the pixel array with a certain colour via 
the `pixels.transit` function, the colour isn't the same everywhere on the strip.
In fact, the colour has a gradient. Might be worth looking in to.



 -= Brendan Mesters =-
https://github.com/BrendanMesters
-=-=-=-=-=-=-=-=-=-=-=-=-
"""

import board
import neopixel
import time



# COLOUR DEFINITIONS
magenta = (126, 000, 129)
cyan = (000,126,129)
purple = (126, 10, 40)
vibes = (126, 40, 10)

scalar = 0.25


def main():
    # Variable definitions
    pixels = neopixel.NeoPixel(board.D18, 300)


    # Main loop
    colour = list( map(
        lambda v: int(v * scalar),
        vibes
    ))

    # The byte representation of the colours is GRB, not RGB, thats why we need to look at 1-i % 3 as opposed to i % 3
    pixel_set = [colour[(1-i) % 3] for i in range(900)]
    buffer = bytearray(pixel_set)
    pixels._transmit(buffer)



if __name__ == "__main__":
    main()