import sys
from collections import deque

input = sys.stdin.readline

"""
플로이드 워셜 써서 각 distances의 최대값들을 구함

그 최대값들의 최솟값은 후보 점수이고 그 점수를 가진 사람이 후보 
"""
n = int(input())
INF = sys.maxsize

graph = [[] for _ in range(n+1)]
distances = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  distances[i][i] = 0
  
while True:
  a,b = map(int, input().split())
  if a==-1:
    break
  graph[a].append(b)
  graph[b].append(a)
  distances[a][b] = 1
  distances[b][a] = 1

for mid in range(1,n+1):
  for start in range(1,n+1):
    for end in range(1,n+1):
      if distances[start][mid] + distances[mid][end] < distances[start][end]:
        distances[start][end] = distances[start][mid] + distances[mid][end]



for i in range(n+1):
  distances[i][0] = 0

  
max_distances = []
min_dist = INF

for i in range(1, n+1):
  max_dist = max(distances[i])
  min_dist = min(min_dist, max_dist)
  max_distances.append((i, max_dist))

candidates = []
candidate_score = min_dist
candidate_num = 0

for person in max_distances:
  if person[1] == min_dist:
    candidate_num+=1
    candidates.append(person[0])

print(f"{candidate_score} {candidate_num}")

for candidate in candidates:
  print(candidate, end=' ')

    
    
  
      