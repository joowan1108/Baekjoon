import sys
input = sys.stdin.readline

n,l = map(int, input().split())

places = list(map(int, input().split()))
places.sort()
"""
places a,b가 있을 때 a+l-1<=b이어야 다 커버가 된다. 
"""

tmp = places[0]
coverage = tmp + l -1

tapes = 1
for i in range(1, n):
  
  if coverage < places[i]:
    tmp = places[i]
    coverage = tmp + l - 1
    tapes+=1

print(tapes)

