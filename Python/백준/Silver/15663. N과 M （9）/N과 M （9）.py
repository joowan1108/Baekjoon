import sys
from itertools import permutations
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))

combs = permutations(nums, m)
combs = list(set(combs))
combs.sort()
for comb in combs:
  for c in comb:
    print(c, end=' ')
  print()


  
  

  

    




  
  

