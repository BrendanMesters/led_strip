# A file full of helper functions used in multiple places

# Gamma Correction
def gamma_correct_colour(rgb_tuple, brightness=1.0):
    """
    Adjust the given RGB tuple for Neopixel display using gamma correction and brightness scaling.

    Args:
    rgb_tuple (tuple): The RGB tuple with values from 0 to 255.
    brightness (float): A brightness factor between 0.0 and 1.0.

    Returns:
    tuple: Adjusted RGB tuple with values from 0 to 255.
    """
    # Gamma correction factor (commonly between 2.0 to 2.8 for LEDs)
    gamma = 2.2

    # Maximum value for an 8-bit color component
    max_val = 255

    # Ensure brightness is within range (range goes from 0 to 2)
    brightness = max(0, min(brightness, 2))

    # Apply gamma correction and scale to [0, 255]
    corrected = tuple(
        int(max_val * (brightness * ((c / max_val) ** gamma))) for c in rgb_tuple
    )
    return corrected


# Translate colours
def parse_colour(col, intensity):
    colours = {
        "magenta": (126, 000, 129),
        "purple": (126, 10, 40),
        "cyan": (000, 126, 129),
        "vibes": (185, 109, 58),  # (126,  40,  10),
        "off": (000, 000, 000),
    }
    colour = colours.get(col, (0, 0, 0))
    return gamma_correct_colour(colour, float(intensity))
