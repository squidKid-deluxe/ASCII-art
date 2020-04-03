# Import an image processing tool
from PIL import Image
# Decide what image to convert, and make it 1/3 the size
#image = [Image.open](https://Image.open)
import time




images = {
"python": Image.open("python.jpg"),
}

# run all images in loop
# for k,v in images.items():
# image = v

# enter choice
choice = input("enter number: ")
image = images[choice]
# Define the ASCII characters
characters = [' ', '.', ':', 'x', '#']
# initialize
text = ''
len_chars = len(characters)
step = 255/len_chars
a, b = 0, step
x, y, z = 0, 0, 0
# open and resize the image
scale = image.height/350
image = image.resize((int(image.width / scale), int(image.height / scale)))
image = image.resize((int(image.width / 1), int(image.height / 2.3)))
# For every pixel in the image...
while y < image.height:
    # Find its brightness
    brightness = sum(image.getpixel((x, y))) / len_chars
    # Depending on its brightness, assign it an ASCII character
    while z < len_chars:
        #print(a, brightness, b)
        if a <= brightness <= b:
            #print(characters[z])
            text += characters[z]
            break
        # increment variables
        a += step 
        b += step
        z += 1
    # reset window and idx
    z = 0
    a = 0
    b = step
    # next pixel same line
    x += 1
    # new line
    if x == image.width - 1:
        text += '\n'
        y += 1
        x = 0
# finally print the output
print("\033c")
print(text)
# pause between images if loop
time.sleep(2)
