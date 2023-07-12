'''
Module docstrings
'''

from string import printable
import sys
sys.set_int_max_str_digits(10000)


def file_to_int(path: str) -> int:
    '''docstring'''
    with open(path, "rb") as file:
        bytez = file.read()

    return int.from_bytes(bytez, "big")


def int_to_bytes(intdata: int) -> bytes:
    '''docstring'''
    bits = (intdata.bit_length() + 7) // 8
    bytez = intdata.to_bytes(bits, "big")
    return bytez


def int_to_file(intdata: int, filepath: str) -> None:
    '''docstring'''
    bytez = int_to_bytes(intdata)
    with open(filepath, "wb") as file:
        file.write(bytez)


def intfile_to_mediafile(intpath: str, mediapath: str) -> None:
    '''docstring'''
    with open(intpath, encoding='utf8') as file:
        int_to_file(int(file.read()), mediapath)


def mediafile_to_intfile(filepath: str, savepath: str) -> None:
    '''docstring'''
    bytez = open(filepath, "rb", encoding='utf8').read()
    intz = int.from_bytes(bytez, "big")
    with open(savepath, 'w', encoding='utf8') as savefile:
        print(intz, file=savefile)


def to_int(intstr: str, chars: str) -> int:
    '''docstring'''
    base = len(chars)

    def ind(char):
        return chars.find(char)

    dec_encoding = (ind(i) * (base**n) for n, i in enumerate(intstr[::-1]))
    return sum(dec_encoding)


def safe_to_int(intstr: str, chars) -> int:
    '''docstring'''
    if isinstance(chars, int):
        assert chars <= len(
            printable
        ), f"integer conversions only supported till base {len(printable)}\
(not base {chars})"
        chars = printable[:chars]

    assert all(
        [i in chars for i in intstr]
    ), "The supplied number has characters not in base i"

    return to_int(intstr, chars)


def highpow(base: int, num: int) -> int:
    '''docstring'''
    expo = 0
    while base**expo <= num:
        expo += 1
    return expo - 1


def highmul(base: int, num: int) -> int:
    '''docstring'''
    mul = 0
    while base * mul <= num:
        mul += 1
    return mul - 1


def highpowmul(base: int, num: int):
    '''docstring'''
    # divs = [base**i for i in reversed(range(highpow(base, num)+1))]
    pows = reversed(range(highpow(base, num) + 1))

    while num:
        for _pow in pows:
            _d = base**_pow
            div = highmul(_d, num)
            num -= _d * div
            yield div


def to_bin(num: int) -> str:
    '''docstring'''
    pows = {i: 0 for i in range(highpow(2, num), -1, -1)}

    while num:
        for _pow in pows:
            div = 2**_pow
            if div <= num:
                pows[_pow] = 1
                num -= div
    return "".join(str(i) for i in pows.values())


def to_tri(num: int) -> str:
    '''docstring'''
    base = 3
    powmul = highpowmul(base, num)
    return "".join(str(v) for v in powmul)


def to_base(num: int, chars: str) -> str:
    '''docstring'''
    base = len(chars)  # chars = ''.join(str(i) for i in range(base))
    powmul = highpowmul(base, num)
    return "".join(chars[v] for v in powmul)


def safe_to_base(num: int, chars: str) -> str:
    '''docstring'''
    if isinstance(chars, int):
        assert chars <= len(
            printable
        ), f"integer conversions only supported till base {len(printable)}\
(not base {chars})"
        chars = printable[:chars]

    assert all(
        [i in chars for i in str(num)]
    ), "The supplied number has characters not in base i"

    return to_base(num, chars)


UNICODE = 1114111
ASCII = 65536


# def toB65K():
#     pass


# def toB1M():
#     pass
