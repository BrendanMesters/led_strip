"""
CLOCK MODULE

Generates an array of 3-pairs representing the RGB value of neopixels
to represent a clock

Values for the different parts of the clock pixels can be provided,
if they are not provided then default values are used

Colour values can also be changed while the CLOCK MODULE is running.



TODO:
- Create pixel generation
- Create colour change functions
- Create callback for the values
- Allow UTC offsets to be provided

long term
- Work with queue-dequeue
- figure out how to get pre-generated clock values to work with an appropriate interrupt to indicate the change of values.


 -= Brendan Mesters =-
https://github.com/BrendanMesters
-=-=-=-=-=-=-=-=-=-=-=-=-
"""

import time
from datetime import datetime



# returns a greycode of 2^n bits as
def get_gray(n):
    """
    Generate the greycode for 2^n bits, as a list of the 1 indexes
    """
    if n == 1:
        return [(), (0,)]
    else:
        oldval = get_gray(n-1)
        retval = oldval + oldval[::-1]
        for i in range((2**(n-1)), 2**n):
            retval[i] = retval[i] + (n-1,)
    return retval



def get_clock(GMT_offset = 1, hour_colour = (255, 0, 0), minute_colour = (0, 255, 0), second_colour = (0, 0, 255), divide_colour = (255, 255, 255)):
    """
    Generate the current clock representation in greycode form.
    
    """
    now = datetime.now()
    six_gray = get_gray(6)
    five_gray = get_gray(5)
    my_time = (now.hour + GMT_offset, now.minute, now.second)

    # [0-4][5][6-11][12][13-18] == Hours |white| minutes |white| seconds
    
    hours = [hour_colour if i in five_gray[my_time[0]] else (0, 0, 0) for i in range(5)]
    minutes = [minute_colour if i in six_gray[my_time[1]] else (0, 0, 0) for i in range(6)]
    seconds = [second_colour if i in six_gray[my_time[2]] else (0, 0, 0) for i in range(6)]
    retval = hours + [divide_colour] + minutes + [divide_colour] + seconds

    return retval
    
