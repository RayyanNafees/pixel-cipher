from math import log, ceil
import string
from unicodedata import digit

#* NOTE THAT math.log CAN GET THE POWER OF INTEGER OF ANY BASE

strify = lambda arr: ''.join(str(i) for i in arr)


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


def till_multibase(n: int, base: int=11) -> dict[int, int]:
  
    base_chars = string.printable
    assert base<= (len(base_chars)), 'Base out of range'

    pow_dict = {}

    while n:
        
        power = int(log(n, base)) # 6
        
        mul = n//base**power
        _mul = base_chars[mul]
        
        pow_dict[power] = _mul

        n -=  (base**power)*mul # n = 4

    return pow_dict


def digitify(pow_dict: dict[int, int], base: int=2, formatter=strify) -> str:
    print(pow_dict)

    strlen = max(pow_dict.keys())
    dig_arr = [0]*(strlen+1)

    for power, digit in pow_dict.items():
        
        if base<=10: # numeric digit
            if digit:

                dig_arr[(strlen- power)] = digit  
                # same as strarr[power] = '1'
                # then doing reverse(strarr)
                # Adds number from start using negatie indices

        else: # string digit
            if string.printable.index(digit):
                dig_arr[(strlen- power)] = digit

    return formatter(dig_arr)

binify = lambda n, base=2: digitify(tobase(n, base), base)
multify = lambda n, base=11: digitify(till_multibase(n, base), base)

test = lambda n=1000, base=11: print(n == int(str(multify(n, base)),base))

test()