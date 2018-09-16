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

def RotateString(input):
    return(input[1:] + input[0])

def CircularPrimeTest(input, primes):

    string_rep = str(input)
    rotated = RotateString(string_rep)

    if int(string_rep) not in primes:
            return(0)

    for j in string_rep:
        if int(j) % 2 == 0 and input != 2:
            return(0)

    while rotated != string_rep:
        if int(rotated) not in primes:
            return(0)
        rotated = RotateString(rotated)
    print(input)
    return(1)

if __name__ == "__main__":
    counter_list = []
    test_up_to = 1000000
    primes = FindPrimes(test_up_to)
    for j in primes:
        counter_list.append(CircularPrimeTest(j, primes))
    print(sum(counter_list))
