def series(limit, digits):
    sum = 0
    for i in range(1,limit+1):
        sum += i**i
        sum % (10**digits)
    return(sum % (10**digits))

if __name__ == "__main__":
    limit = 1000
    digits = 10
    print(series(limit,digits))