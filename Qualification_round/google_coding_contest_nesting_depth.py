import numpy as np

def nest(array):
    for k, sample in enumerate(array):
        left = 0
        output = ""
        for num in sample:
            if left < num:
                output += ("(" * (num - left)) + str(num)
                left = num
            elif left > num:
                output += (")" * (left - num)) + str(num)
                left = num
            else:
                output += str(num)
        output += ")" * left
        print("Case #{}: {}".format(k+1, output))

n = int(input())
array = []
for i in range(n):
    line = input()
    array.append(map(int, list(line)))
nest(array)







