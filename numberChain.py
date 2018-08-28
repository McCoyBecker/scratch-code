def numberChain(number):
    chainNum = number
    while not (chainNum == 1 or chainNum == 89):
        chainNum = sum(list(map(lambda x: x**2, [int(i) for i in str(chainNum)])))
    return chainNum

if __name__ == "__main__":
    Counter_89 = 0
    Counter_1 = 0
    
    for i in range(1,10000000):
        if numberChain(i) == 89:
            Counter_89 += 1
        else:
            Counter_1 += 1
        print(i)

    print(Counter_89)
