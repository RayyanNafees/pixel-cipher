import math
import numpy as np
from PIL import Image
import sys

sys.set_int_max_str_digits(10000)
# import basify
BYTE_CONST = 2.408116385911179

# reference: https://stackoverflow.com/questions/46923244/how-to-create-image-from-a-list-of-pixel-values-in-python3


def mid_factor(n) -> tuple[int, int]:
    """Gives the best factor of rows x columns to keep the 2d array squaric

    Args:
        n (int): Length of the array

    Returns:
        tuple[int]: Factors of rows and columns
    """
    factors = [(i, n // i) for i in range(2, n) if not n % i]

    return factors[len(factors) // 2]


def matrix(arr: list[tuple[int]], order: tuple[int, int]) -> list[list[object]]:
    """Converts a list of objects to a matrix of the specified order

    Args:
        arr (list[object]): The list of objects to be converted to matrix
        order (tuple[int,int]): The order of the matrix (rows, columns)

    Returns:
        list[list[object]]: A list of {rows} lists with {columns} objects representing the matrix
    """

    rows, cols = order
    assert rows * cols == len(
        arr
    ), f"Matrix of order ({rows}x{cols}) be created with the provided data"

    mat = []
    while arr:
        mat.append(arr[:cols])
        arr = arr[cols:]

    return mat


def pixel(n: int) -> tuple[int, int, int]:
    """represents a number as a pixel character

    Args:
        num (int): Numeric value of the pixel

    Returns:
        tuple[int]: A list of RGB Value
    """
    assert n < 16777216, "Number should be less than 16777216"

    b = n
    g = n // 256
    r = g // 256

    return (r % 256, g % 256, b % 256)


def unpixel(rgb: tuple[int, int, int]) -> int:
    """Returns the numeric value of a pixel

    Args:
        rgb (tuple[int]): A tuple of (r,g,b) value

    Returns:
        int: The numeric value of the pixel as an integer
    """

    # print(rgb)
    r, g, b = rgb
    assert sum(rgb) < 255 + 255 + 256, "Invalid pixel"

    return (r * 256 + g) * 256 + b


def visualize(pixels: list[tuple[int]], path: str = "new.png"):
    """Converts an array of pixel value to real image

    Args:
        pixels (tuple[int], optional): Array of pixel values. Defaults to [].
        path (str, optional): Path to the new file. Defaults to 'new.png'.
    """
    img = matrix(pixels, mid_factor(len(pixels)))

    # Convert the pixels into an array using numpy
    array = np.array(img, dtype=np.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save(path)


def getrgb(imgpath: str) -> list[tuple[int]]:
    """Returns the rgb values from an image the specified path

    Args:
        imgpath (str): Image path to get pixels of

    Returns:
        list[tuple[int]]: List of rgb value tuple (r,g,b)
    """
    im = Image.open(imgpath)
    pixels = im.load()
    width, height = im.size
    if pixels is None:
        raise Exception("error while getting image pixels")

    return [pixels[x, y] for x in range(width) for y in range(height)]


def file_to_int(path: str) -> int:
    """Converts bytes inside a file to integers

    Args:
        path (str): Path to the file

    Returns:
        int: The bytes of the file as integers
    """
    with open(path, "rb") as file:
        bins = file.read()

    return int.from_bytes(bins, byteorder="big")


def int_to_file(num: int, path: str) -> None:
    """Makes the file from integeral value of its bytes

    Args:
        n (int): Integer Value
        path (str): Path to the file
    """
    intlen = len(str(num))
    bytelen = math.floor(intlen / BYTE_CONST)

    # print(intlen, f(intlen))

    byts = num.to_bytes(bytelen, byteorder="big")

    with open(path, "wb") as b:
        b.write(byts)
