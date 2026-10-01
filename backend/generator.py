import random


def generate_numbers(count: int, low: int, high: int) -> list[int]:
    if count < 0:
        raise ValueError("count must be >= 0")
    if low > high:
        low, high = high, low
    return [random.randint(low, high) for _ in range(count)]
