import sys
from itertools import combinations_with_replacement
 
input = sys.stdin.readline
 
n,m = map(int, input().split())
 
lst = [i for i in range(1,n+1)]
nHm = combinations_with_replacement(lst, m)
 
products = list(nHm)
for pro in products:
	for p in pro:
		print(p, end=' ')
	print()
