def collatz(n, counter):
    if n == 1:
        return(counter)
    if n % 2 == 0:
        return(collatz(n/2, counter + 1))
    if n % 2 == 1:
        return(collatz(3*n+1, counter + 1))

if __name__ == "__main__":
    limit = 1000000
    max = 0
    index = 0
    for i in range(1,limit):
        if max < collatz(i, 0):
            index = i
            max = collatz(i,0)
    print(max)
    print(index)