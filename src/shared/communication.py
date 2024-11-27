from enum import Enum


class SetColour:
    def _translate_colour(col):
        colours = {
            "magenta" =   (126, 000, 129),
            "purple" =    (126,  10,  40),
            "cyan" =      (000, 126, 129),
            "vibes" =     (126,  40,  10),
            "off" =       (000, 000, 000)
        }
        return colours.get(col)

    def __init__(self, colour=None, rgb = (256, 256, 256)):
        self.rgb = rgb
        t_col = self._translate_colour(colour)
        if t_col is not None:
            self.rgb = t_col


class SetIntensity:

    def __init__(self, intensity = 1.0):
        self.intensity = intensity

