from math import log
import string
from types import FunctionType
from functools import partial

# * NOTE THAT math.log CAN GET THE POWER OF INTEGER OF ANY BASE



def pixel(n):
    '''Converts an integer to a pixel representation'''
    b = n
    g = n//256
    r = g // 256

    return (r % 256, g % 256, b % 256)

def pixelise(digits): return [pixel(d) for d in digits]

def strify(arr): return ''.join(str(i) for i in arr)


def isiterable(sequence):
    '''Checks whether a sequence is iterable or not'''

    try:
        iter(sequence)
    except TypeError:
        return False
    else:
        return True


def tobase(n, base=3):
    '''Converts integers till any base till base-10

    Args:
        n (int): integer to be converted
        base (int, optional): The base to convert the integer to (<=10). Defaults to 3.

    Returns:
        dict[int, int]: Returns the powers mapped to the digits to 
                        place there while writing the num
                        to be used in digitifying, the rest placevalues default to 0
    '''

    assert base <= 10, 'Not yet developed for higher bases'

    pow_dict = {}

    while n:

        power = int(log(n, base))  # 6

        mul = n//base**power

        pow_dict[power] = mul

        n -= (base**power)*mul  # n = 4

    return pow_dict


def to_printable_base(n: int, base: int = 11) -> dict[int, int]:
    '''Converts an integer to base_printable

    Args:
        n (int): The integer to convert
        base (int, optional): The base to convert it to (till base printable). Defaults to 11.

    Returns:
        dict[int, int]: A dictionary of powers to character representation for the int
    '''
    base_chars = string.printable
    assert base <= (len(base_chars)), 'Base out of range'

    pow_dict = {}

    while n:

        power = int(log(n, base))  # 6

        mul = n//base**power    # value
        _mul = base_chars[mul]  # digit representation

        pow_dict[power] = _mul

        n -= (base**power)*mul  # n = 4

    return pow_dict


# to_base_ascii = lambda n, base: to_printable_base(n, base, )


def to_anybase(n: int, base: int = 37, base_chars: str = string.printable, char_func=None):
    '''Convert an integer to any base with the provided char repr array or func that returns char repr

    Args:
        n (int): The integer to convert
        base (int, optional): The base to raise the integer to. Defaults to 37.
        base_chars (str, optional): The list of char repr indiced by their num value. Defaults to string.printable.
        char_func (function, optional): A function that returns the char repr from the supplied num value. Defaults to None.

    Returns:
        _type_: _description_
    '''
    functional = bool(char_func)

    if not functional:
        assert base <= (len(base_chars)), 'Base out of range'

    pow_dict = {}

    while n:

        power = int(log(n, base))  # 6

        mul = n//base**power    # value

        if not functional:
            _mul = base_chars[mul]  # digit representation from chars
        else:
            # digit representation as out of func from a val
            _mul = char_func(mul)

        pow_dict[power] = _mul

        n -= (base**power)*mul  # n = 4

    return pow_dict


base_ascii = partial(to_anybase, base_chars=''.join(chr(i)
                     for i in range(0, 65536)))

base_unicode = partial(to_anybase, base_chars=''.join(chr(i)
                       for i in range(0, 1114111)))


#! So much vulnerability in this
def from_anybase(n: int, base: int = 37, base_chars=string.printable, num_func=None) -> int:
    '''Reverse of to_any_base func

    Args:
        n (int): C0onverted number
        base (int, optional): It's base. Defaults to 37.
        base_chars (list, optional): Base characters used. Defaults to string.printable.
        num_func (function, optional): Fucntion to give numeric value from a char. Defaults to None.

    Returns:
        int: Returns the integer it was converted from
    '''
    assert base <= len(
        base_chars), 'Not enough characters to reperesent higher int base'

    strn = str(n)
    mul: FunctionType = num_func or base_chars.index
    num_arr = ((base**_pow)*mul(ch) for _pow, ch in enumerate(reversed(strn)))

    return sum(num_arr)


def digitify(pow_dict: dict[int, int], base: int = 2, formatter=strify, char_func=None) -> str:
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

    return formatter(dig_arr)

#! NEEDED to DEBUG ----------------


to_base_pixel = partial(to_anybase, base=16777216,
                        base_chars=None, char_func=pixel)
to_base_pixels = partial(to_anybase, base=16777216, base_chars=range(16777216))


def pixelify(n): return digitify(to_base_pixel(n), 16777216)


def pixelify2(n): return digitify(
    to_base_pixels(n), 16777216, lambda n: n, pixelise)


#! Most crucial funcs above ------------


def binify(n, base=2): return digitify(tobase(n, base), base)
def multify(n, base=11): return digitify(to_printable_base(n, base), base)


def test(n=1000, base=11): return print(n == int(str(multify(n, base)), base))

# test()
