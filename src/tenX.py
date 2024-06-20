from typing import TypeVar
from PIL import Image
import numpy as np
import math
import sys
sys.set_int_max_str_digits(0)

PIXEL_CONST = 1677721600
T = TypeVar('T')

def pixelize(n: int) -> list[tuple[int, int, int, int]]:

    def pixel(n: int) -> tuple[int, int, int, int]:
        """Converts an integer to a pixel representation"""
        assert n < PIXEL_CONST, f"Number should be less than {PIXEL_CONST}"

        a = n
        b = a // 100
        g = b // 256
        r = g // 256

        return (r % 256, g % 256, b % 256, a % 100)

    def one_in_start(n: int) -> int:
        """makes a 9 digit number or less 10 digit number by adding 1 in starting"""
        """Example:
                567 becomes 1000000567 (a 10 digit number)"""
        return 1 * pow(10, 9) + n if n < pow(10, 8) else n

    def ten_digit_list(n: int) -> list[int]:
        limit = pow(10, 9)

        return [one_in_start(n % limit)] + ten_digit_list(n // limit) if n > limit else [n]


    return [pixel(i) for i in ten_digit_list(n)]


def unpixelize(pixels: list[tuple[int, int, int, int]]) -> int:

        
    def unten_digit_list(list_of_10s: list[int]) -> int:
        digit = 0
        limit = pow(10, 9)

        def numlen(n: int) -> int:
            return math.floor(math.log10(n)) + 1

        def last(n):
            return n == len(list_of_10s) - 1

        for n, i in enumerate(list_of_10s):
            factor = pow(limit, n)

            if numlen(i) >= limit and not last(n):
                digit += (i - limit) * factor
            else:
                digit += i * factor

        return digit

    def unpixel(pixel: tuple[int, int, int, int]) -> int:
        """Returns the numeric value of a pixel"""

        assert sum(pixel) < 255 + 255 + 256 + 100, "Invalid pixel"

        r, g, b, a = pixel
        return ((r * 256 + g) * 256 + b) * 100 + a


    return unten_digit_list([unpixel(pixel) for pixel in pixels])


def squarray(array: list[T]) -> list[list[T]]:
    side_len = math.sqrt(len(array))
    row_len = math.floor(side_len)
    length = math.ceil(side_len)

    return [array[n * row_len : (n + 1) * row_len] for n in range(length)]

def unsquarray(array: list[list[T]]) -> list[T]:
    return [item for sublist in array for item in sublist]

def imagify(rgba: list[list[tuple[int, int, int, int]]]) -> Image.Image:
    # image = Image. # open image
    array = np.array(rgba, dtype=np.uint8)

    image = Image.fromarray(array)
    return image
   

def unimagify(image: Image.Image) -> list[list[tuple[int, int, int, int]]]:
    # image.load()
    width, height = image.size

    rgba = [[image.getpixel((x, y)) for x in range(width)] for y in range(height)]

    return rgba


def int_to_image(n: int) -> Image.Image:
    pixels = pixelize(n)

    return imagify(squarray(pixels))
    
def image_to_int(image: Image.Image) -> int:
    return unpixelize(unsquarray(unimagify(image)))


def imagine(intfile:str, imgfile:str):
    with open(intfile) as ifile:
        n = int(ifile.read())

    return int_to_image(n).save(imgfile)

def unimagine(imgfile:str, intfile:str):
    with open(imgfile, 'rb') as ifile:
        image = Image.open(ifile)
    
    image.load()
    n = image_to_int(image)

    with open(intfile, 'w') as ofile:
        ofile.write(str(n))