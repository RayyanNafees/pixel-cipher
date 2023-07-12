from fib import fibonacci, file_to_int


def cycle_quo_rem(big_int: int) -> list[int]:
    '''returns the fibonacci cycles and remainder'''
    prev_term = 0
    for current_cycle, term in enumerate(fibonacci()):
        if term == 1:
            continue
        if not big_int//term:
            return [current_cycle-1, big_int//prev_term, big_int % prev_term]
        prev_term = term


def defib(cycles: int, quotient: int, remainder: int):
    '''Generates the actual integer from the Fibonacci Cycles & remainder'''
    for cyc, term in enumerate(fibonacci()):
        if cyc == cycles:
            return term*quotient+remainder

num = file_to_int('algo.pdf')
cycle, quo, rem = cycle_quo_rem(num)
print(f'Cycle: {cycle} \nRem: {rem}')
print("Actual: ", num==defib(cycle,quo,rem))

print('Sub: ', len(str(num))-len(f"{cycle},{quo},{rem}"))