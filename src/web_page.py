# A simple script to calculate BMI
from pywebio.input import input, FLOAT, select
from pywebio.output import put_text

def bmi():
    colour = select(
            "What colour do you want the lights to be?",
            [
                    'magenta',
                    'purple',
                    'cyan',
                    'vibes',
                    'other',
                    'off'
            ]
        )
    if colour == 'other':
        hex_colour = input("Please provide the hexcode of the desired colour (example ab01ef)")
        success = False
        while not success:
            try:
                hex_colour = int(hex_colour, 16)
                success = True
            except:
                hex_colour = input("Please provide a VALID hexcode (example ab01ef)")



if __name__ == '__main__':
    bmi()
