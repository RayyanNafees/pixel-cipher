import math
import sys
from PIL import Image

Image.frombytes("RGB", (0, 0), bytes())

sys.set_int_max_str_digits(0)
# sys.setrecursionlimit(5000)

PIXEL_CONST = 1677721600
limit = pow(10, 6)
suplimit = pow(10, 7)
sublimit = pow(10, 5)


def one_in_start(n: int) -> int:
    return 1 * limit + n if n < sublimit else n


def six_digit_list(n: int) -> list[int]:
    try:
        return (
            [one_in_start(n % limit)] + six_digit_list(n // limit) if n > limit else [n]
        )
    except RecursionError:
        sys.setrecursionlimit(sys.getrecursionlimit() * 10)

        return [one_in_start(n % limit)] + six_digit_list(n // limit) if n > limit else [n]


def characterize(n: int) -> str:
    return "".join(chr(i) for i in six_digit_list(n))


def numlen(n: int) -> int:
    return math.floor(math.log10(n)) + 1


def unsix_digit_list(list_of_6s: list[int]) -> int:
    digit = 0

    def last(n):
        return n == len(list_of_6s) - 1

    for n, i in enumerate(list_of_6s):
        factor = pow(limit, n)

        if numlen(i) >= limit and not last(n):
            digit += (i - limit) * factor
        else:
            digit += i * factor

    return digit


def integerize(chars: str) -> int:
    return unsix_digit_list([ord(char) for char in chars])


def int_to_chars(intfile, charfile):
    with open(intfile) as ifile:
        n = int(ifile.read())

    with open(charfile, "w", encoding="utf-8") as ofile:
        ofile.write(characterize(n))


def chars_to_int(charfile, intfile):
    with open(charfile, encoding="utf-8") as ifile:
        chars = ifile.read()

    with open(intfile, "w") as ofile:
        ofile.write(str(integerize(chars)))
