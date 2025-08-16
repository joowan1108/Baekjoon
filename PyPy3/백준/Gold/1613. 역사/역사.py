import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
"""
플로이드 적용해서 start -> end 경로 있으면 -1
end -> start 경로 있으면 1
둘다 없으면 0
"""

n, k = map(int, input().split())
distances = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(k):
  s,e = map(int, input().split())
  distances[s][e] = 1

for mid in range(1,n+1):
  for start in range(1,n+1):
    for end in range(1,n+1):
      new_dist = distances[start][mid] + distances[mid][end]
      if new_dist < distances[start][end]:
        distances[start][end] = new_dist


s = int(input())
for _ in range(s):
  a,b = map(int, input().split())
  if distances[a][b]>0 and distances[a][b]!=INF:
    print(-1)
  elif distances[b][a]>0 and distances[b][a] != INF:
    print(1)
  else:
    print(0)
    