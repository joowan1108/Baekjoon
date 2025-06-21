



import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))

res = [-1]*(n)

not_found = [(A[0],0)]

for i in range(1,n):
    while not_found:
        if A[i] > not_found[-1][0]:
            num, idx = not_found.pop()
            res[idx] = A[i]
        else:
            break
    not_found.append((A[i], i))

for r in res:
    print(r, end=" ")
