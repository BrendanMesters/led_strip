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

# from lights import pride
from daemonize import Daemonize
import atexit
import signal
import socket

from queue import Queue

import board
import neopixel

from pride import do_the_gay
from shared import gamma_correct_colour, parse_colour


background_colour = (126, 40, 10)
scalar = 1
pixels = None
NUM_PIXELS = 300


# Led colour setting
def set_leds(led_inputs: list):
    """
    Displays a list of k 3-pairs of numbers (in RGB format) into the led strip.
    NOTE: the values SHOULD BE GAMMA CORRECTED, as this is not done in this function
    """
    global pixels
    if pixels is None:
        pixels = neopixel.NeoPixel(board.D18, NUM_PIXELS)
    extended_led_input = [led_inputs[i % len(led_inputs)] for i in range(NUM_PIXELS * 3)]
    GRB_pixels = [extended_led_input[(i-(i%3)) + ((1-i)%3)] for i in range(NUM_PIXELS * 3)]
    buffer = bytearray(GRB_pixels)
    pixels._transmit(buffer)


# Handle Web messages
def handle_web_messages(server_socket):
    conn, addr = server_socket.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            command = data.decode().split(" ")
            # I want to call functions first, as those might be offloaded
            # to different threads, while the colour command is not currently yet
            if command[0] == "FUNCTION":
                print(f"{command[0]} {command[1]}")
                fun = command[1]
                if fun == "GAY":
                    pixels = do_the_gay()
                    print(pixels)
                    set_leds(pixels)
                pass
            elif command[0] == "COLOUR":
                print(f"{command[0]} {command[1]} {command[2]}")
                rgb = parse_colour(command[1], command[2])
                set_leds(rgb)
                pass


# Combine data and render
def combine_and_render():
    """
    This function should gather data returned by the different threads
    who generate parts of the lightstrip output.
    It should combine these parts in correspondance with a certain type of logic
    It should then render those on the actual led strip.
    """
    pass


def main():
    # Main loop
    scaled_colour = list(map(lambda v: int(v * scalar), background_colour))

    # The byte representation of the colours is GRB, not RGB, thats why we need to look at 1-i % 3 as opposed to i % 3
    set_leds(scaled_colour)

    # setup internal communication socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 65432))
    server_socket.listen()

    while True:
        # message receiving loop
        handle_web_messages(server_socket)

        # Lights logic
        combine_and_render()

    exit_handler()


def exit_handler():
    set_leds((0, 0, 0))


if __name__ == "__main__":
    # Makes sure the leds are turned off uppon program being quit or
    # SSH connection being dropped
    atexit.register(exit_handler)
    signal.signal(signal.SIGHUP, exit_handler)

    main()
