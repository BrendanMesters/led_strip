import time
from datetime import datetime
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 300)
pixels.brightness = 0.04

#pixels.fill((80, 80, 80))
"""
i = 0
while i < 300-7:
    pixels[i+0] = (255, 0, 0)
    pixels[i+1] = (0, 255, 0)
    pixels[i+2] = (0, 0, 255)
    pixels[i+3] = (255, 255, 0)
    pixels[i+4] = (255, 0, 255)
    pixels[i+5] = (0, 255, 255)
    pixels[i+6] = (255, 255, 255)
    i += 7
for i in range(300):
    pixels[i] = [180, 60, 30]
while True:
    for i in range(100):
        pixels.brightness = i/100
        pixels.show()
        time.sleep(0.02)

"""

# returns a greycode of 2^n bits
def get_gray(n):
    if n == 1:
        return [(), (0,)]
    else:
        oldval = get_gray(n-1)
        retval = oldval + oldval[::-1]
        #print(f"in gray code{n} we have preretval {retval}")
        for i in range((2**(n-1)), 2**n):
            retval[i] = retval[i] + (n-1,)
    return retval



def main():
    now = datetime.now()
    six_gray = get_gray(6)
    five_gray = get_gray(5)
    #the pi seems to grab GMT and we're GMT +1
    my_time = (now.hour + 1, now.minute, now.second)
    print(f"The time in greycode is \n {five_gray[my_time[0]]} hours ({my_time[0]})" +
                                    f"\n {six_gray[my_time[1]]} minutes ({my_time[1]}) " +
                                    f"\n {six_gray[my_time[2]]} seconds ({my_time[2]})" )

    hour_colour = (255, 0, 0)
    minute_colour = (0, 255, 0)
    second_colour = (0, 0, 255)
    divide_colour = (255, 255, 255)
    while True:
        time.sleep(0.1)
        now = datetime.now()
        six_gray = get_gray(6)
        five_gray = get_gray(5)
        my_time = (now.hour + 1, now.minute, now.second)

        # [0-4][5][6-11][12][13-18] == Hours |white| minutes |white| seconds
        
        hours = [hour_colour if i in five_gray[my_time[0]] else (0, 0, 0) for i in range(5)]
        minutes = [minute_colour if i in six_gray[my_time[1]] else (0, 0, 0) for i in range(6)]
        seconds = [second_colour if i in six_gray[my_time[2]] else (0, 0, 0) for i in range(6)]
        retval = hours + [divide_colour] + minutes + [divide_colour] + seconds

        for i, c in enumerate(retval):
            pixels[i] = c



    while True:
        time.sleep(0.1)
        #print(f"The time in greycode is \n {five_gray[my_time[0]]} hours ({my_time[0]})" +
                                    #f"\n {six_gray[my_time[1]]} minutes ({my_time[1]}) " +
                                    #f"\n {six_gray[my_time[2]]} seconds ({my_time[2]})" )

        now = datetime.now()
        my_time = (now.hour + 1, now.minute, now.second)
        # [0-4][5][6-11][12][13-18] == Hours |white| minutes |white| seconds
        leds_on = [4-v for v in five_gray[my_time[0]]] + [5] + [11-v for v in six_gray[my_time[1]] ] + [12] + [18-v for v in six_gray[my_time[2]] ]
        print(leds_on)
        print ([v + 11 for v in six_gray[my_time[0]] ])


        for i in range(20):
            if (i in leds_on):
                pixels[i] = (255, 0, 0) if (i < 5) else (255, 255, 255) if (i == 5)  else (0, 255, 0) if (i < 12) else (255, 255, 255) if (i == 12) else (0, 0, 255)
            else:
                pixels[i] = (0,0,0)
        #for v in five_gray[my_time[0]]:
            #pixels[v] = (255, 0, 0)
        #for v in six_gray[my_time[1]]:
            #pixels[5 + v] = (0, 255, 0)
        #for v in six_gray[my_time[2]]:
            #pixels[11 + v] = (0, 0, 255)

        #for c, v in enumerate(five_gray[my_time[0]] + six_gray[my_time[1]] + six_gray[my_time[1]] ):
            #if (v):
                #pixels[c] = (255, 0, 0) if (c < 6) else (0, 255, 0) if (c < 11) else (0, 0, 255)
            

if __name__ == "__main__":
    main()

