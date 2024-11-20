import sys
from itertools import permutations
 
input = sys.stdin.readline
 
n,m = map(int, input().split())
 
lst = list(map(int, input().split()))
lst.sort()

combs = permutations(lst, m)
for comb in combs:
	for c in comb:
		print(c, end=' ')
	print()
