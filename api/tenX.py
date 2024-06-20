from PIL import Image
import math

PIXEL_CONST = 1677721600


def ten_digit_list(n: int) -> list[int]:
    limit = pow(10, 9)

    def one_in_start(n: int) -> int:
        """makes a 9 digit number or less 10 digit number by adding 1 in starting"""
        """Example:
                567 becomes 1000000567 (a 10 digit number)"""
        return 1 * pow(10, 9) + n if n < pow(10, 8) else n

    return [one_in_start(n % limit)] + ten_digit_list(n // limit) if n > limit else [n]


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


def pixel(n: int) -> tuple[int, int, int, int]:
    """Converts an integer to a pixel representation"""
    assert n < PIXEL_CONST, f"Number should be less than {PIXEL_CONST}"

    a = n
    b = a // 100
    g = b // 256
    r = g // 256

    return (r % 256, g % 256, b % 256, a % 100)


def unpixel(pixel: tuple[int, int, int, int]) -> int:
    """Returns the numeric value of a pixel"""

    assert sum(pixel) < 255 + 255 + 256 + 100, "Invalid pixel"

    r, g, b, a = pixel
    return ((r * 256 + g) * 256 + b) * 100 + a



def pixelize(n) -> list[tuple[int, int, int, int]]:
    return [pixel(i) for i in ten_digit_list(n)]


def unpixelize(pixels: list[tuple[int, int, int, int]]) -> list[int]:
    return [unpixel(pixel) for pixel in pixels]


def imagine(rgba: list[tuple[int, int, int, int]], filepath="image.png"):
    image = Image.open("image.png")  # open image

    width = len(rgba[0])
    height = len(rgba)

    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), rgba[y][x])

    image.save(filepath)
