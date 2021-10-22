import sys
import time
import importlib

from typing import Callable


def benchmark(func: Callable, iters: int):
    start = time.time()
    num_primes = 0
    for i in range(2, iters):
        num_primes += func(i)
    print(f"{num_primes} primes found from {limit} iterations in {round(time.time() - start, 4)} seconds.")


if __name__ == "__main__":
    _, module, function_name, limit = sys.argv
    function = getattr(importlib.import_module(module), function_name)
    benchmark(func=function, iters=int(limit))
