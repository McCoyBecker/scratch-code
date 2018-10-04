import numpy as np

def triangle(n):
    return(n*(n+1)/2)

def pentagonal(n):
    return(n*(3*n-1)/2)

def hexagonal(n):
    return(n*(2*n-1))

def k_in_n(n):
    return((-1+int(np.sqrt(1-4*n+12*(n**2))))/2)

print(k_in_n(50))
