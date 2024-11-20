import sys
from itertools import combinations

input = sys.stdin.readline

n,m = map(int, input().split())

lst = [i for i in range(1,n+1)]
nCm = combinations(lst, m)

combination_lst = list(nCm)
for com in combination_lst:
	for c in com:
		print(c, end=' ')
	print()
