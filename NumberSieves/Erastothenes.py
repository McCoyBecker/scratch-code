from math import sqrt
    
def FindPrimes(limit):
    isPrime = {}
    
    isPrime[1] = False
    for i in range(2, limit + 1):
        isPrime[i] = True
    
    checkLimit = int(sqrt(limit)) + 1
    for i in range(2, checkLimit):
        if isPrime[i]:
            for factor in range(2, limit + 1):
                j = i * factor
                if (j > limit): break
                isPrime[j] = False

    primes = []
    for i in range(1, limit + 1):
        if isPrime[i]:
            primes.append(i)

    return primes

def main():

    Limit = input("Search for primes up to what number?: ")
    print(FindPrimes(Limit))

main()
