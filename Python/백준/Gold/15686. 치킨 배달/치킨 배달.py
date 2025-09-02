import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())

"""
13Cm으로 어떤 치킨집을 골라야 하는지에 대한 경우의 수를 구함

각 집들의 치킨 거리를 구하여 저장

모든 경우의 수에 대해 도시의 치킨 거리를 구해 그 최솟값을 답으로 함
"""

maps = []
for _ in range(n):
  maps.append(list(map(int, input().split())))

houses = []
chickens =[]
for i in range(n):
  for j in range(n):
    if maps[i][j] == 1:
      houses.append((i,j))
    elif maps[i][j] == 2:
      chickens.append((i,j))

combs = combinations(chickens, m)


ans = sys.maxsize

for comb in combs:
  city_dist = 0
  #각 집의 치킨 거리 구하기
  for house_h, house_w in houses:
    min_dist = sys.maxsize
    #치킨 거리
    for chicken_h, chicken_w in comb:
      min_dist = min(min_dist, abs(house_h-chicken_h) + abs(house_w-chicken_w))
    #각 집의 치킨 거리를 도시 치킨 거리에 합치기
    city_dist += min_dist
  #각 경우의 수의 도시 치킨 거리의 최소값 구하기
  ans = min(ans, city_dist)
print(ans)

      
      



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  