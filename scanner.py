from PIL import Image
import numpy as np


def convert_color(pixel, threshold=127.5):
    if sum(pixel) / 3 > threshold:
        return 1
    else:
        return 0


def scan_image(filename='chance.png', show=False):

    # open the image and get dimensions
    im = Image.open(filename)
    in_data = im.load()
    xmin, ymin, xmax, ymax = im.getbbox()

    # convert image to black and white
    output = Image.new('1', (xmax, ymax))
    for x in range(xmax):
        for y in range(ymax):
            output.putpixel((x, y), convert_color(in_data[x, y]))

    # optionally show the image for testing
    if show: output.show()

    # returns a 1-D array of 0s and 1s
    return np.array(output.getdata())


if __name__ == '__main__':
    scan_image('chance.png', True)
