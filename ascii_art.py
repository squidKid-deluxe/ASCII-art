"""
a module that creates ascii art from images
"""

# Import an image processing tool
from PIL import Image
from json import dumps, loads
from subprocess import call
from time import sleep

def main(file):
    """
    main process that converts image and prints ascii art
    """
    # enter choice
    choice = file
    try:
        image = Image.open(choice)
    except:
        print("Invalid file.")
        exit()
    # initialize
    text = ''
    x_pos, y_pos = 0, 0
    # open and resize the image
    scale = image.width/200
    image = image.resize((int(image.width / scale), int(image.height / scale)))
    image = image.resize((int(image.width / 1), int(image.height / 2.3)))

    # For every pixel in the image...
    while y_pos < image.height:
        # find its color
        color = image.getpixel((x_pos, y_pos))
        # Add a colored space to the text
        text += f"\033[48;2;{color[0]};{color[1]};{color[2]}m \033[0m"
        # next pixel same line
        x_pos += 1
        # go to the next line if we have reached the end of a pixel row
        if x_pos == image.width - 1:
            text += '\n'
            y_pos += 1
            x_pos = 0
    # finally return the output
    return text
        

if __name__ == '__main__':
    print("Get ready...")
    sleep(2)
    print("\033c")

    asci = main("python.jpg")

    for _ in range(10):
        call("xdotool key ctrl+minus".split())

    print(asci)
    sleep(3.5)
    print('\033c')
    call("xdotool key ctrl+0".split())
    print("\033cWow, Huh?")
