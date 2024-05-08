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
import sys
import time
from daemonize import Daemonize
import atexit
import signal

from queue import Queue

import board
import neopixel




background_colour= (126, 40, 10)
scalar = 1
pixels = None



scale_colour = lambda s, rgb: (int(rgb[0]*s), int(rgb[1]*s), int(rgb[2]*s))



def led_thread(com_que: Queue):
    """
    This function is supposed to be the running thread
    for the led controller.
    It should manage its own time spend running, keeping
    in mind that it has to manage the led strip in accordance
    to the requests received over the queue.
    """
    print("started")
    while true:
        # Check for exit request.
        if false:
            break
        print("asdkl;ghasdljfhasdg")
        set_leds_colour("magenta")
        time.sleep(1)
        set_leds_colour("cian")
        time.sleep(1)
        set_leds_colour("off")
        time.sleep(1)

        



def set_leds(led_inputs: list):
    """ Displays a list of k 3-pairs of numbers (in RGB format) into the led strip. """
    global pixels
    if pixels is None:
        pixels = neopixel.NeoPixel(board.D18, 300)
    pixel_set = [led_inputs[(1-i) % 3] for i in range(900)]
    buffer = bytearray(pixel_set)
    pixels._transmit(buffer)

def turn_leds_off():
    """ Turns off the led strip """
    set_leds([0 for _ in range(900)])

def set_leds_colour(input_c: str, scalar=1.0):
    """ Flushes the led strip with the given colour, if it is known """
    # COLOUR DEFINITIONS
    magenta =   (126, 000, 129)
    purple =    (126,  10,  40)
    cyan =      (000, 126, 129)
    vibes =     (126,  40,  10)
    off =       (000, 000, 000)

    
    # If a known colour is given that colour is chosen
    if input_c == "magenta": background_colour = magenta
    elif input_c == "cyan": background_colour = cyan
    elif input_c == "purple": background_colour = purple
    elif input_c == "vibes": background_colour = vibes
    elif input_c == "off": background_colour = off
    else: 
        print(f"Colour \"{input_c}\" not known, please provide a valid colour")
        return


    set_leds(scale_colour(scalar, background_colour))
    



def main():
    # Main loop
    scaled_colour = list( map(
        lambda v: int(v * scalar),
        background_colour
    ))

    # The byte representation of the colours is GRB, not RGB, thats why we need to look at 1-i % 3 as opposed to i % 3
    set_leds(scaled_colour)

    while True:
        time.sleep(10000000)
        
    exit_handler()






def parse_input():
    
    # COLOUR DEFINITIONS
    magenta =   (126, 000, 129)
    purple =    (126,  10,  40)
    cyan =      (000, 126, 129)
    vibes =     (126,  40,  10)
    off =       (000, 000, 000)

    global background_colour
    global scalar

    for v in sys.argv[1:]:
        # If a known colour is given that colour is chosen
        if v == "magenta": background_colour = magenta
        elif v == "cyan": background_colour = cyan
        elif v == "purple": background_colour = purple
        elif v == "vibes": background_colour = vibes
        elif v == "off": background_colour = off
        else:
            try:
                scalar = float(v)
            except:
                print(f"value {v} can not be interpreted as either a colour, nor a scalar value")

def exit_handler():
    turn_leds_off()

if __name__ == "__main__":
    # Makes sure the leds are turned off uppon program being quit or
    # SSH connection being dropped
    atexit.register(exit_handler)
    signal.signal(signal.SIGHUP, exit_handler)

    parse_input()
    main()
