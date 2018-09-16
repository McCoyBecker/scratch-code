read_in = open("/Users/mccoybecker/Documents/GitHub/scratch-code/numbers.txt", "r")
sum = 0
for line in read_in:
    sum += int(line)
print(sum)