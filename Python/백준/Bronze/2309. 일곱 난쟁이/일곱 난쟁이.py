from itertools import combinations

height = []
for _ in range(9):
    height.append(int(input()))
r=7

combinations_iter = combinations(height, r)
for lst in combinations_iter:
    if(sum(lst)==100):
        for s in sorted(lst):
            print(s)
        break;