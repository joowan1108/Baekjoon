import sys
from collections import deque
input = sys.stdin.readline

"""
작업 순서라는 문제가 topological sort를 떠올리게 했다.
topological sort

"""

T = int(input())
answers = []
for _ in range(T):
  n, k = map(int, input().split())
  times = [0] + list(map(int,input().split()))
  indegree = [0] * (n+1)
  graph = [[] for _ in range(n+1)]
  for _ in range(k):
    x,y = map(int, input().split())
    indegree[y] += 1
    graph[x].append(y)
  goal = int(input())

  q = deque()
  dp = [-1]*(n+1)
  for i in range(1,n+1):
    if indegree[i] == 0:
      q.append(i)
      dp[i] = times[i]
  
  while q:
    node = q.popleft()
    for adj in graph[node]:
      indegree[adj]-=1
      dp[adj] = max(dp[adj], dp[node] + times[adj])
      if indegree[adj] == 0:
        q.append(adj)

  answers.append(dp[goal])
for ans in answers:
  print(ans)

    