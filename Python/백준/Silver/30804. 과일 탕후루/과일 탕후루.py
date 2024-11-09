import sys
from collections import defaultdict


input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))

start, end = 0,0
contained_fruits = defaultdict(int)
contained_fruits[fruits[start]]=1

contained_kinds = set()
contained_kinds.add(fruits[start])

result = 0

while end<n:
	if len(contained_kinds)<=2:
		result = max(result, end-start+1)
		end+=1
		if end<n:
			contained_fruits[fruits[end]]+=1
			contained_kinds.add(fruits[end])
	else:
		contained_fruits[fruits[start]]-=1
		if contained_fruits[fruits[start]]==0:
			contained_kinds.remove(fruits[start])
		start+=1
		
print(result)
		
	
	