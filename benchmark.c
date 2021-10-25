#include <stdio.h>
#include <time.h>
#include "isprime.h"

int main() {
    clock_t t=clock();
    int limit=250001;
    int numPrimes=0;
    for (int i=2; i<limit; i++)
        numPrimes+=isPrime(i);

    t=clock()-t;
    printf("%d primes found from %d iters in %f seconds.", numPrimes, limit, ((float)t)/CLOCKS_PER_SEC);
}
