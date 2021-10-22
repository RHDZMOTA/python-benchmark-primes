from numba.pycc import CC

cc = CC("numba_impl")


@cc.export("is_prime", "i4(i4)")
def is_prime(n: int) -> int:
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return 0
    return 1


if __name__ == "__main__":
    cc.compile()
