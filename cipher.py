import math
import numpy as np
from PIL import Image
# import basify
VAL = 2.408116385911179

def mid_factor(n):
    '''Gives the best factor of rows x columns to keep the 2d array squaric

    Args:
        n (_type_): Length of the array

    Returns:
        _type_: Factors of rows and columns
    '''
    factors = [(i, n//i) for i in range(2,n) if not n%i]
    return factors[len(factors)//2]


def pixel(n: int) -> tuple[int]:
    '''represents a number as a pixel character

    Args:
        num (int): Numeric value of the pixel

    Returns:
        tuple[int]: A list of RGB Value
    '''
    assert n < 16777216, 'Number should be less than 16777216'

    b = n
    g = n//256
    r = g // 256

    return (r % 256, g % 256, b % 256)


def visualise(pixels: list[tuple[int]], path: str = 'new.png'):
    '''Converts an array of pixel valuea to real image

    Args:
        pixels (tuple[int], optional): Array of pixel values. Defaults to [].
        path (str, optional): Path to the new file. Defaults to 'new.png'.
        dptype (_type_, optional): Numpy Array dptype. Defaults to np.uint8.
    '''
    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)
    array2d = np.reshape(array, mid_factor(len(array)))

    # np.reshape(array, len(array) )

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array2d)
    new_image.save(path)


def file_to_int(path: str) -> int:
    '''Converts bytes inside a file to integers

    Args:
        path (str): Path to the file

    Returns:
        int: The bytes of the file as integers
    '''
    with open(path, 'rb') as file:
        bins = file.read()

    return int.from_bytes(bins, byteorder='big')


def int_to_file(num: int, path: str) -> None:
    '''Makes the file from integeral value of its bytes

    Args:
        n (int): Integer Value
        path (str): Path to the file
    '''
    intlen = len(str(num))

    f = lambda n: math.floor(n/2.408116385911179)

    # print(intlen, f(intlen))

    byts = num.to_bytes(f(intlen), byteorder='big')

    with open(path, 'wb') as b:
        b.write(byts)


test = lambda file, ext:  int_to_file(file_to_int(f'{file}.{ext}'), f'{file}2.{ext}')


# test('cipher', 'js')
