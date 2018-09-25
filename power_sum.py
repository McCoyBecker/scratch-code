import math

n = 10000
divisor_sum_list = []
for i in range(n):
    divisors = [d for d in range(2, int(i/2)+1) if i % d == 0]
    divisors.append(1)
    divisor_sum_list.append(sum(divisors))

amicable_list = []
for i in range(len(divisor_sum_list)):
    for j in range(len(divisor_sum_list)):
        if (i == divisor_sum_list[j] and j == divisor_sum_list[i] and i != j):
            amicable_list.append(i)
            amicable_list.append(j)

amicable_list = set(amicable_list)
print(amicable_list)
print(sum(amicable_list))