import numpy as np
from numpy.linalg import inv

def generating_function(n):
    sum = 0
    for i in range(0,11):
        sum += ((-1)**i)*(n**i)
    return(sum)

sequence = [generating_function(j) for j in range(1,11)]
powers = [j for j in range(0,11)]
vector = np.array([sequence[0], sequence[1]])

print(vector)
print(powers)

polynomial_base = np.array([[1, 1], [1, 2]])
inverse = inv(polynomial_base)
print(np.matmul(inverse, vector))