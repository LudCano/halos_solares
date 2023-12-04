import matplotlib.pyplot as plt
import colorsys

def wavelength_to_rgb(wavelength):
    """
    Convert a wavelength in nanometers to an RGB color.
    """
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 750:
        gamma = 0.8
        intensity_max = 255
        factor = 0

        if wavelength < 440:
            red = -(wavelength - 440) / (440 - 380)
            green = 0.0
            blue = 1.0
        elif wavelength < 490:
            red = 0.0
            green = (wavelength - 440) / (490 - 440)
            blue = 1.0
        elif wavelength < 510:
            red = 0.0
            green = 1.0
            blue = -(wavelength - 510) / (510 - 490)
        elif wavelength < 580:
            red = (wavelength - 510) / (580 - 510)
            green = 1.0
            blue = 0.0
        elif wavelength < 645:
            red = 1.0
            green = -(wavelength - 645) / (645 - 580)
            blue = 0.0
        else:
            red = 1.0
            green = 0.0
            blue = 0.0

        # Adjust intensity
        if wavelength < 420:
            factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
        elif wavelength < 645:
            factor = 1.0
        else:
            factor = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)

        red = int(intensity_max * (red * factor)**gamma)
        green = int(intensity_max * (green * factor)**gamma)
        blue = int(intensity_max * (blue * factor)**gamma)

        return red, green, blue
    else:
        raise ValueError("Wavelength should be in the range 380nm to 750nm")

def plot_colors(wavelengths):
    """
    Plot scatter points with colors corresponding to the given wavelengths.
    """
    colors = [wavelength_to_rgb(w) for w in wavelengths]
    normalized_colors = [(r / 255, g / 255, b / 255) for r, g, b in colors]

    plt.scatter(range(len(wavelengths)), [0] * len(wavelengths), color=normalized_colors)
    plt.title('Colors at Various Wavelengths')
    plt.xticks(range(len(wavelengths)), wavelengths)
    plt.xlabel('Wavelength (nm)')
    plt.yticks([])
    plt.show()


def get_colores(lst):
    colors = [wavelength_to_rgb(w) for w in lst]
    normalized_colors = [(r / 255, g / 255, b / 255) for r, g, b in colors]
    return normalized_colors    

# Example usage:
#wavelength_list = [450, 500, 550, 600]  # List of wavelengths in nm
#plot_colors(wavelength_list)
