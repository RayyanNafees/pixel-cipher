'''
Library full of generator functions only to improve efficiency while base conversion
'''
from math import log, log10
import string
from functools import partial
from typing import Any, Callable, Union, Iterator


def pixel(n):
    '''Converts an integer to a pixel representation'''
    b = n
    g = n//256
    r = g // 256

    return (r % 256, g % 256, b % 256)


def pixelise(digits: list[int]) -> Iterator[int, int, int]:
    '''Yields pixelised digits

    Args:
        digits (list[int]): The array of digits to pixelise

    Yields:
        tuple[int]: All the digits converted to their rgb
    '''
    for dig in digits:
        yield pixel(dig)


'''Checks whether a sequence is iterable or not'''
def isiterable(sequence): return ('__iter__' in dir(sequence))


def tobase(n: int, base: int = 3) -> Iterator[int, int]:
    '''Yields a power, value pair for base conversion

    Args:
        n (int): The digit to convert
        base (int, optional): The base to convert the int to. Defaults to 3.

    Yields:
        Iterator[int, int]: A pair of power, digit tuple to
    '''
    assert base <= 10, 'Not yet developed for higher bases'

    while n:

        power = int(log(n, base))  # 6

        mul = n//base**power

        yield power, mul
        n -= (base**power)*mul  # n = 4


def to_printable_base(n: int, base: int = 11) -> Iterator[int, int]:
    '''Converts an integers with letters in string.printable

    Args:
        n (int): The integer to convert
        base (int, optional): The base to raise the integer to. Defaults to 11.

    Yields:
        Iterator[int, int]: THe set of power, character pair to yield
    '''
    base_chars = string.printable
    assert base <= (len(base_chars)), 'Base out of range'

    while n:

        power = int(log(n, base))  # 6

        mul = n//pow(base, power)    # value
        _mul = base_chars[mul]  # digit representation

        yield power, _mul

        n -= pow(base, power)*mul  # n = 4


def to_anybase(n: int, base: int = 37, base_chars: str = string.printable,
               char_func: Callable[[int], str] = None) -> Iterator[int, int]:
    '''Converts an integer to any base with the specified char representation

    Args:
        n (int): The integer to raise to a higher base
        base (int, optional): The base of the new integer. Defaults to 37.
        base_chars (str, optional): A list of digits indiced to their value. Defaults to string.printable.
        char_func (Callable[[int], str], optional): A callable that returns \
                    a digit from the specified numeric value. Defaults to None.

    Yields:
        Iterator[int, int]: A tuple of power, digit value
    '''
    functional = bool(char_func)

    if not functional:
        assert base <= (len(base_chars)), 'Base out of range'

    while n:

        power = int(log(n, base))  # 6

        mul = n//pow(base, power)    # value

        if not functional:
            _mul = base_chars[mul]  # digit representation from chars
        else:
            # digit representation as out of func from a val
            _mul = char_func(mul)

        yield power, _mul

        n -= pow(base, power)*mul  # n = 4


base_ascii = partial(to_anybase, base=65536, base_chars=None, char_func=chr)

base_unicode = partial(to_anybase, base=1114111,
                       base_chars=None, char_func=chr)

base_pixel = partial(to_anybase, base=16777216,
                     base_chars=None, char_func=pixel)


def from_anybase(n: Union[int, str, list[int]], base: int = 37, base_chars=string.printable,
                 num_func: Callable[[str], int] = None) -> int:
    '''Reverse of to_any_base func

    Args:
        n (int): C0onverted number
        base (int, optional): It's base. Defaults to 37.
        base_chars (list, optional): Base characters used. Defaults to string.printable.
        num_func (function, optional): Fucntion to give numeric value from a char. Defaults to None.

    Returns:
        int: Returns the integer it was converted from
    '''
    if not num_func:
        assert base <= len(
            base_chars), 'Not enough chars to represent higher int base'

    if isinstance(n, int) and num_func:

        numlen = int(log10(n))+1

        # Tells the digit in a number n at an indice i from back
        # https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python
        def dig(n,i): return n//pow(10, i) %10

        mul = num_func

        # num_arr = (pow(base, _pow)*mul(ch)
        #            for _pow, ch in enumerate(reversed(strn)))

        num_arr = (pow(base, _pow) * mul(dig(n, _pow))
                   for _pow in range(numlen))

        # i = 0
        # sm = 0
        # while i < numlen:
        #     sm += pow(base, i)*dig(n, i)
        #     return sum

        return sum(num_arr)

    strn = str(n) if isinstance(n, int) else n
    mul: Callable[[str], int] = num_func or base_chars.index
    num_arr = (pow(base, _pow)*mul(ch)
               for _pow, ch in enumerate(reversed(strn)))

    return sum(num_arr)


def digitify(pow_dict: dict[int, int], base: int = 2, formatter=None, char_func=None) -> str:
    '''Converts a dict of powers to char repr to a digit for tat power

    Args:
        pow_dict (dict[int, int]): A dict mapping powers to char reprs
        base (int, optional): The base of the integer. Defaults to 2.
        formatter (function, optional): The format func the array of digits is passed from. Defaults to strify.
        char_func (function, optional): The func to return the char repr in case pow_dict not given. Defaults to None.

    Returns:
        str: Returns the digit so formed ussually a string
    '''
    strlen = max(pow_dict.keys())
    dig_arr = [0]*(strlen+1)

    for power, digit in pow_dict.items():

        if base <= 10:  # numeric digit
            if digit:

                dig_arr[(strlen - power)] = digit
                # same as strarr[power] = '1'
                # then doing reverse(strarr)
                # Adds number from start using negatie indices

        elif base <= len(string.printable):  # string digit
            if string.printable.index(digit):
                dig_arr[(strlen - power)] = digit

        elif char_func:
            dig_arr[(strlen-power)] = char_func(digit)

    return formatter(dig_arr) if formatter else dig_arr


#! Try compressing these

# path = ("C:\\Users\\nafee\\OneDrive\\Pictures\\sadasd.png")


# pixelize(path, 'large.png')