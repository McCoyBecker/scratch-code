n = 28124
abundant_numbers = []
for i in range(n):
    divisors = [d for d in range(2, int(i/2)+1) if i % d == 0]
    if sum(divisors) > i:
        abundant_numbers.append(i)

abundant_sums = set([(i+j) for j in abundant_numbers for i in abundant_numbers])
non_abundant_sums = [i for i in range(n) if i not in abundant_sums]
print(sum(non_abundant_sums))

