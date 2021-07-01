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
Runtime: 752 ms, faster than 90.35% of Python3 online submissions for Count Primes.
Memory Usage: 103.4 MB, less than 32.59% of Python3 online submissions for Count Primes.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [False] * 2 + [True] * (n-2)
        i = 2
        while i*i < n:
            if is_prime[i]:
                is_prime[i*i:n:i] = [False] * len(is_prime[i*i:n:i])
            i += 1
        return sum(is_prime)