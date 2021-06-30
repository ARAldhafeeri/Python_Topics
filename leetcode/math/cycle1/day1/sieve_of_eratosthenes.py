"""
The sieve of Eratosthenes is one of the most efficient ways to find all primes
 smaller than n when n is smaller than 10 million or so.
 ref (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

The algorthim is quite simple:
- we create a list of numbers from 2 - n
- while creating the list we mark all numbers that are divisible by 2
- we move to our next unmarked number 3
- then for all unmarked numbers -> we mark all numbers which are multiples of 3
e.g ; 9,  27, 
- also we mark all numbers that are greater than or eqal to 3^2
- we move to our next unmarked number 5 and mark all numbers that are multiple of 5
or greater than or eqal to the squre of 5
"""

"""
1 year ago sol :
faster than 62.66%
running time 1644 ms
"""

import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        l=[i for i in range(n)]
        
        for i in range(2,n):
                if l[i]==True:
                    continue
                factor=2
                while(i*factor<n):
                    l[factor*i]=True
                    factor+=1
        output=[]
        for i in range(2,n):
            if l[i]!=True:
                output.append(i)
        return len(output)


"""
this year sol:
using sieve of eratosthenes algorthim

"""

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            print p,