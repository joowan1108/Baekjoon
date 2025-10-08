import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

combs = combinations_with_replacement(nums,m)
combs = list((combs))
combs_set = set()

for i in range(len(combs)):
  if combs[i] not in combs_set:
    for c in combs[i]:
      print(c, end=' ')
    print()
    combs_set.add(combs[i])


  
  

  

    




  
  

