import numpy as np

def solve(activities, k):
    enumerated_activities = enumerate(activities)
    sorted_activities = sorted(enumerated_activities, key=lambda x: x[1])

    person = ["J", "C"]
    p_index = False
    start = None
    end = None
    occupied = [0, 0]
    result = []
    for i, act in sorted_activities:
        if start == None:
            occupied[p_index] = act[1]
            result.append((i, person[p_index]))
            start = act[0]
            end = act[1]
        else:
            if act[0] < end and occupied[not p_index] <= act[0]:
                p_index = not p_index
                occupied[p_index] = act[1]
                result.append((i, person[p_index]))
                start = act[0]
                end = act[1]
            elif act[0] >= end:
                occupied[p_index] = act[1]
                result.append((i, person[p_index]))
                start = act[0]
                end = act[1]
            else:
                return "Case #{}: {}".format(k+1, "IMPOSSIBLE")
        # print(occupied)
    return "Case #{}: {}".format(k+1, "".join([person for i, person in sorted(result)]))

# activities = [[360,480],[420,540],[600,660]]
# activities = [[0,1440],[1,3],[2,4]]
# activities = [[99,150],[1,100],[100,301],[2,5],[150,250]]
# activities = [[0,720],[720,1440]]
# activities = [[0,1],[0,720],[1,5], [5,1000], [720,900]]

n = int(input())
for i in range(n):
    d = int(input())
    array = []
    for j in range(d):
        line = input()
        array.append(list(map(int,line.strip().split(" "))))
    print(solve(array, i))
# print(solve(activities, 1))




