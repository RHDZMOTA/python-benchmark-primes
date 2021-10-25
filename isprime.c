#include <stdio.h>

int isPrime(int num) {
    for(int i=2; i<=num/2; i++)
	    if (!(num%i))
            return 0;
    return 1;
}

