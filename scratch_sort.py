import time

def naive_sort(input):
    start_time = time.time()
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i] < input[j]:
                input[i], input[j] = input[j], input[i]
    return((input, time.time() - start_time))

input = [3,2,1,4,10,3,5,11,15,19,24]
print(naive_sort(input))