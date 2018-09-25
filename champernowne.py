champ_str = "0."
for i in range(1000000):
    champ_str = champ_str + str(i)

product = 1
for j in [1,10,100,1000,10000,100000,1000000]:
    product = product*int(champ_str[j+2])

print(product)