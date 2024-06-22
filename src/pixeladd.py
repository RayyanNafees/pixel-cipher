import math

DIGIT_LENGTH = 1000


def get(array: bytes, index: int) -> int | None:
    if index < 0 or index >= len(array):
        return None
    return array[index]


def num_len(n: int) -> int:
    return math.floor(math.log10(n)) + 1


def add_two_pixels(a: int, b: int | None) -> int:
    assert (
        a + (b or 0) < 2 * DIGIT_LENGTH
    ), f"Each pixel should be less than ${DIGIT_LENGTH}"

    i = DIGIT_LENGTH

    if b is None:
        return pow(i, 2) + (a * i)  # 1255000

    return (a * i + b) % (i * i)


def sep_two_pixels(n: int) -> tuple[int, int | None]:
    assert n < 2 * pow(DIGIT_LENGTH, 2), f"{n} is not a valid pixel number"

    if not n // pow(DIGIT_LENGTH, 2):
        return n // DIGIT_LENGTH, n % DIGIT_LENGTH

    return (n - pow(DIGIT_LENGTH, 2)) // DIGIT_LENGTH, None


def add_three_pixels(a: int, b: int, c: int) -> int:
    assert (
        a + b + c < 3 * DIGIT_LENGTH
    ), f"Each pixel should be less than ${DIGIT_LENGTH}"

    return (a * DIGIT_LENGTH + b) * DIGIT_LENGTH + c


def sep_three_pixels(n: int) -> tuple[int, int, int | None]:

    if not n // pow(DIGIT_LENGTH, 3):
        return (
            (n % pow(DIGIT_LENGTH, 3)) // pow(DIGIT_LENGTH, 2),
            (n % pow(DIGIT_LENGTH, 2)) // pow(DIGIT_LENGTH, 1),
            (n % pow(DIGIT_LENGTH, 1)) // pow(DIGIT_LENGTH, 0),
        )

    return (
        (n - pow(DIGIT_LENGTH, 3)) // pow(DIGIT_LENGTH, 2),
        (n - pow(DIGIT_LENGTH, 3)) % pow(DIGIT_LENGTH, 2) // DIGIT_LENGTH,
        None,
    )


def add_n_pixel(pixels: list[int]) -> int:
    n = len(pixels)
    return sum(pixels[i] * pow(DIGIT_LENGTH, n-i-1) for i in range(n))


def sep_n_pixel(n: int, pixel: int) -> list[int]:
    return [
        (pixel % pow(DIGIT_LENGTH, i)) // pow(DIGIT_LENGTH, i - 1)
        for i in range(n, 0, -1)
    ]
