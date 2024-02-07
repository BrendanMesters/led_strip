import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 300)

pixels.fill((80, 80, 80))
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
