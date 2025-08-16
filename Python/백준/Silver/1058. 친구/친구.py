import sys
import heapq

input = sys.stdin.readline

"""
2친구가 가장 많은 사람은 최단 경로가 2 이하인 애들

플로이드 워셜로 최단경로가 1,2인 것들의 최대 개수 구하면 된다

"""
INF = sys.maxsize

n = int(input())

#연결된 애들 표시
distances = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
  distances[i][i] = 0
  
for f in range(1,n+1):
  friends = input().rstrip()
  for i in range(n):
    if friends[i] == 'Y':
      distances[f][i+1] = 1


for mid in range(1, n+1):
  for start in range(1, n+1):
    for end in range(1, n+1):
      if distances[start][end] > distances[start][mid] + distances[mid][end]:
        distances[start][end] = distances[start][mid] + distances[mid][end]

max_count = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if i != j and distances[i][j] <= 2:
            count += 1
    max_count = max(max_count, count)

print(max_count)

  
  
    
    
    
    


    
    
  
      