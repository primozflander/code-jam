import numpy as np

def calculate_sum_row_col(test_table, k):
    n = len(test_table)
    sum = 0
    repeated_col = 0
    repeated_row = 0
    for i, row in enumerate(test_table):
        repeated_row += int(len(row) != len(set(row)))
        sum += row[i]
    test_table_transposed = np.array(test_table).transpose()
    for col in test_table_transposed:
        repeated_col += int(len(col) != len(set(col)))
    print("Case #{}: {} {} {}".format(k,sum,repeated_row,repeated_col))

n = int(input())
for i in range(n):
    d = int(input())
    array = []
    for j in range(d):
        line = input()
        array.append(list(map(int,line.strip().split(" "))))
    calculate_sum_row_col(array,i+1)






