"""
a module that creates ascii art from images
"""

# Import an image processing tool
from PIL import Image
import numpy as np
from colorize import bold

def main():
    """
    main process that converts image and prints ascii art
    """
    # initalise images
    # initalize color numpy arrays
    red = np.array((255, 0, 0))
    black = np.array((0, 0, 0))
    green = np.array((0, 255, 0))
    yellow = np.array((255, 255, 0))
    blue = np.array((0, 0, 255))
    purple = np.array((255, 0, 255))
    cyan = np.array((0, 255, 255))
    white = np.array((255, 255, 255))

    # initalize list of numpy array colors
    colors = [red, green, blue, cyan, yellow, purple, white, black]
    # initalize list of color strings
    str_clrs = ['red', 'green', 'blue', 'cyan', 'yellow', 'purple', 'white', 'black']

    images = {
        "python": Image.open("python.jpg"),
    }
    # enter choice
    choice = input("enter name of character: ")
    image = images[choice]
    # Define the ASCII characters
    asci = ['\u1D77', '\u25AE', u'\u213B']
    # initialize
    text = ''
    len_chars = len(asci)
    step = 255/len_chars
    value, value2 = 0, step
    x_pos, y_pos, z_pos = 0, 0, 0
    # open and resize the image
    scale = image.height/350
    image = image.resize((int(image.width / scale), int(image.height / scale)))
    image = image.resize((int(image.width / 1), int(image.height / 2.3)))

    # For every pixel in the image...
    while y_pos < image.height:
        # Find its brightness
        brightness = sum(image.getpixel((x_pos, y_pos))) / len_chars
        # find its color
        color = image.getpixel((x_pos, y_pos))
        # make value1 numpy array out of the color rgb
        color_array = np.array(color)
        # initalise the subtracted arrays list
        subtracted_arrays = []

        # find the color the current pixel is closest to
        for item in colors:
            difference = np.abs(item - color_array)
            difference = sum(difference)
            subtracted_arrays.append(difference)

        minpos = subtracted_arrays.index(min(subtracted_arrays))
        color = str_clrs[minpos]

        # Depending on its brightness, assign it an ASCII character
        while z_pos < len_chars:
            #print(value1, brightness, value2)
            if value <= brightness <= value2:
                #print(characters[z_pos])
                text += bold(color, asci[z_pos])
                break
            # increment variables
            value += step
            value2 += step
            z_pos += 1
        # reset window and idx
        z_pos = 0
        value = 0
        value2 = step
        # next pixel same line
        x_pos += 1
        # new line
        if x_pos == image.width - 1:
            text += '\n'
            y_pos += 1
            x_pos = 0
    # finally print the output
    print("\033c")
    print(text)

if __name__ == '__main__':
    main()
