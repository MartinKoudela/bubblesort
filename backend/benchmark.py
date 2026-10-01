import time
from dataclasses import dataclass

from backend.algorithms import ALGORITHMS


@dataclass
class SortResult:
    algorithm: str
    numbers: list[int]
    seconds: float


def run_sort(algorithm: str, numbers: list[int]) -> SortResult:
    if algorithm not in ALGORITHMS:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    data = list(numbers)
    start = time.perf_counter()
    ALGORITHMS[algorithm](data)
    end = time.perf_counter()
    return SortResult(algorithm=algorithm, numbers=data, seconds=end - start)
