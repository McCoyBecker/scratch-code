with open("/Users/mccoybecker/Documents/GitHub/scratch-code/numbers.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
print(data)

max = 0
for i in range(len(data)-12):
    product = 1
    for j in range(i,13+i):
        product = product * int(data[j])
    if product > max:
        max = product

print(max)