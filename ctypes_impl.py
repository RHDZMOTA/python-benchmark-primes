from ctypes import CDLL

lib = CDLL("./libisprime.so")


def is_prime(num: int) -> int:
    return lib.isPrime(num)
