import sys

input = sys.stdin.readline

n = int(input())

towers = list(map(int, input().split()))

res = [0]*n
remain = [(towers[-1],n-1)]

for i in range(n-1,-1,-1):
    while remain and remain[-1][0] < towers[i]:
        res[remain[-1][1]] = i+1
        remain.pop()
    remain.append((towers[i], i))

for r in res:
    print(r, end=' ')

