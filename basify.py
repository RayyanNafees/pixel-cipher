from math import log, ceil
import string
from unicodedata import digit
from cipher import pixel
import numpy as np

#* NOTE THAT math.log CAN GET THE POWER OF INTEGER OF ANY BASE

strify = lambda arr: ''.join(str(i) for i in arr)
pixelise = lambda digits: [pixel(d) for d in digits]

def isiterable(sequence):
    try:
        for i in sequence: return True
    except:
        return False

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
    
    assert base<=10, 'Not yet developed for higher bases'

    pow_dict = {}

    while n:
        
        power = int(log(n, base)) # 6
        
        mul = n//base**power
        
        pow_dict[power] = mul

        n -=  (base**power)*mul # n = 4

    return pow_dict


def to_printable_base(n: int, base: int=11) -> dict[int, int]:
  
    base_chars = string.printable
    assert base<= (len(base_chars)), 'Base out of range'

    pow_dict = {}

    while n:
        
        power = int(log(n, base)) # 6
        
        mul = n//base**power    # value
        _mul = base_chars[mul]  # digit representation
        
        pow_dict[power] = _mul

        n -=  (base**power)*mul # n = 4

    return pow_dict


to_base_ascii = lambda n, base: to_printable_base(n, base, ''.join(chr(i) for i in range(0, 65536)))

to_base_unicode = lambda n, base: to_printable_base(n, base, ''.join(chr(i) for i in range(0, 1114111)))


def to_anybase(n: int, base: int=37, base_chars=string.printable, char_func=None):

    functional = bool(char_func)

    if not functional:
        assert base<= (len(base_chars)), 'Base out of range'


    pow_dict = {}

    while n:
        
        power = int(log(n, base)) # 6
        
        mul = n//base**power    # value

        if not functional:
            _mul = base_chars[mul]  # digit representation from chars
        else:
            _mul = char_func(mul)  # digit representation as out of func from a val
        
        pow_dict[power] = _mul

        n -=  (base**power)*mul # n = 4

    return pow_dict



def from_printable_base(n: int, base: int=37) -> dict[int, int]:
    '''Reverse of to_multibase

    Args:
        n (int): Converted integer
        base (int, optional): Base it was converted from. Defaults to 37.

    Returns:
        dict[int, int]: Returns the power values for it
    '''
    pass


def digitify(pow_dict: dict[int, int], base: int=2, formatter=strify, char_func=None) -> str:

    strlen = max(pow_dict.keys())
    dig_arr = [0]*(strlen+1)

    for power, digit in pow_dict.items():
        
        if base<=10: # numeric digit
            if digit:

                dig_arr[(strlen- power)] = digit  
                # same as strarr[power] = '1'
                # then doing reverse(strarr)
                # Adds number from start using negatie indices

        elif base <= len(string.printable): # string digit
            if string.printable.index(digit):
                dig_arr[(strlen- power)] = digit

        elif char_func:
            dig_arr[(strlen-power)] = char_func(digit)


    return formatter(dig_arr)

#! NEEDED to DEBUG ----------------

to_base_pixel = lambda n: digitify(to_anybase(n, 16777216, None, pixel), 16777216)

to_base_pixel2=lambda n: digitify(to_anybase(n, 16777216, range(16777216) ), 16777216, lambda n: n, pixelise)

#! Most crucial func ------------

binify = lambda n, base=2: digitify(tobase(n, base), base)
multify = lambda n, base=11: digitify(to_printable_base(n, base), base)

test = lambda n=1000, base=11: print(n == int(str(multify(n, base)),base))

test()