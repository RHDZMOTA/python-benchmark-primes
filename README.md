# Python Simple Prime Test

This repository attempts to answer the question:
> Is Python too slow?

* Short answer: Yes.
* Long answer: Still yes. But you got options!

## Benchmark: prime number test

Consider a simple function to test if a number is prime:
> Given a number `n` find if there's a divisor in the first `n/2` numbers.

Of course, we can come with a better prime-testing solution, but we won't.
This solution is exactly what we need: inefficient and cpu-intensive.

The goal: Compare the python implementation to a pure C solution.

C implementation:

```c
int isPrime(int num) {
    for(int i=2; i<=num/2; i++)
	    if (!(num%i))
            return 0;
    return 1;
}
```

This translates to python as:

```python
def is_prime(n: int) -> int:
    for i in range(2, (n // 2) + 1):
        if not (n % i):
            return 0
    return 1
```

## Benchmark results

..add results..

## Installation

These tests were performed using `python 3.7.5`. We recommend creating a virtualenv and
installing the dependencies:

```commandline
$ pip install -r requirements.txt
```

## Setup

We need to compile the `c` code and the `numba` implementation. For this, simple run:

```commandline
$ bash build.sh --c
```
* The expected output is a `bencharkc` file.
* Alternatively: `gcc -o benchmarkc benchmark.c`

```commandline
$ bash build.sh --py-numba
```
* The expected output is a `numba_impl.*` file.
* Alternatively: `python numba_source.py`

## Run the benchmarks

Run benchmarks individually:
* C: `bash run.sh --c`
* Python Numba: `bash run.sh --py-numba`
* Python Naive: `bash run.sh --py-naive`

