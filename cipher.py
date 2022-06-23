from PIL import Image
import numpy as np

def pixel(num: int):
    assert num <= 16777216, 'Number should be less than 16777216'

    b= num
    g = num//256
    r = g //256

    return (r%256, g%256, b%256)


def visualise(pixels: list =[], path: str ='new.png', dptype=np.uint8):
    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=dptype)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save(path)
