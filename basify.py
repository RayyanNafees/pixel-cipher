from math import log

#* NOTE THAT math.log CAN GET THE POWER OF INTEGER OF ANY BASE


def binary(n=68, base=2) -> dict:
    
    pow_dict = {}

    while n:
        power = int(log(n, base)) # 6
        pow_dict[power] = 1
        n -=  base**power # n = 4

    return pow_dict

def digitify(pow_dict: dict, base: int=2) -> str:
    strlen = max(pow_dict.keys())
    strarr = ['0']*strlen

    for power, digit in pow_dict.items():
        if digit:
            strarr[-(strlen- power)] = '1'  # same as strarr[power] = '1'; then doing reverse(strarr)
            # Adds number from start using negatie indices

    return ''.join(strarr)


binify = lambda n, base=2: digitify(binary(n, base), base)