import cython


def is_prime(n: cython.int):
    i: cython.int
    for i in range(2, (n // 2) + 1):
        if not (n % i):
            return 0
    return 1
