from PIL import Image
import numpy as np

''' 
pixels should be of the form
the width and height of the image depends on these

[
   [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
   [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
   [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
   [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)]
]
'''

def pixel(num: int) -> tuple[int]:
    assert num < 16777216, 'Number should be less than 16777216'

    b= num
    g = num//256
    r = g //256

    return (r%256, g%256, b%256)


def visualise(pixels: tuple[int] =[], path: str ='new.png', dptype=np.uint8):
    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=dptype)

    #TODO: matrix = np.asmatrix(array)
    #TODO: find a way to convert em to matrix

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save(path)
