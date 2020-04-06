from itertools import permutations

goal = 10
dimension = 3

def printLatin(n):
    k = n + 1
    output = []
    for i in range(1, n + 1, 1):
        temp = k
        while (temp <= n):
            output.append(temp)
            temp += 1
        for j in range(1, k):
            output.append(j)
        k -= 1
    return [output[i:i + n] for i in range(0, len(output), n)]

m = list(enumerate(printLatin(dimension)))
l = list(permutations(range(dimension)))
sums = []
for j in l:
    new_matrix = []
    sum = 0
    for p in j:
        for element in m:
            if (element[0]) == p:
                new_matrix.append(element[1])
    print(new_matrix)
    for i, row in enumerate(new_matrix):
        sum += row[i]
    sums.append(sum)
if goal in sums:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
