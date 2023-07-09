"""
Compresses the integers of a File data into .fib
"""
from os.path import basename
from conv import file_to_int


def fibonacci():
    """Yields a Fibonacci Sequence"""

    prev2, prev = 0, 1

    while True:
        yield prev
        prev = prev2 + prev
        prev2 = prev - prev2


def quot_rem_cycles(dividend: int, divisor: int) -> list[int]:
    """returns The quoteient, remainder, cycles of dividing the dividend by divisor"""
    count = 0
    while dividend >= divisor:
        dividend //= divisor
        count += 1

    return [count - 1, dividend, count]


def fibify(big_int: int) -> list[int]:
    """Returns the Fibanacci Remainder & Fibonacci Cycles
    used to compress the big_int by constantly dividing"""

    count = 0
    for cycles, divisor in enumerate(fibonacci()):
        big_int //= divisor
        if big_int <= divisor:
            count = cycles
            break

    remainder = big_int
    cycles = count
    return [remainder, cycles]


def fib_compress(file_path: str, out_path: str = "fib.csv") -> None:
    '''Comrpesses a file with Fibonacci Division'''
    int_data = file_to_int(file_path)
    remainder, cycles = fibify(int_data)

    with open(out_path, 'w', encoding='utf8') as fib_file:
        print('name,seq,cycles,rem', file=fib_file)
        print(f'{basename(file_path)},fib,{cycles},{remainder}', file=fib_file)


def csv_to_cycles_rem(file_path: str) -> list | None:
    '''Parses the Cyccles & Remainder from the CSV file'''
    with open(file_path, encoding='utf8') as csv:
        algo, cycles, rem = csv.readlines()[1].split(',')

        if algo == 'fib':
            return [int(cycles), int(rem)]

# Defib: Fibonacci Multiplier to N + reminder


def defib(cycles: int, remainder: int) -> int:
    '''Regenerates the int data of a file based on fibonacci cycles and remainder'''
    mul = 1
    for current_cycle, fib_term in enumerate(fibonacci()):
        mul *= fib_term
        if current_cycle == cycles:
            return mul + remainder
