from math import sqrt, log10

def Fibonacci(n):
    return(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

for i in range(1,1000):
    print(int(log10(Fibonacci(i))+1))