import sys
from collections import deque

input = sys.stdin.readline
"""
각 노드 부모 정보로 graph를 형성할 수 있다.

dfs를 해서 지우려는 노드에 닿았다면 그 부분은 탐색 안함

dfs를 해서 이동한 노드에서 다른 노드로 이동할 수 없다면 그 노드는 leaf node

"""

n = int(input())

parents = list(map(int, input().split()))

remove = int(input())

start = 0
graph = [[] for _ in range(n)]
for i in range(len(parents)):
  if parents[i] >= 0:
    graph[parents[i]].append(i)
  elif parents[i] == -1:
    start = i
    

visited = set()
leafs = 0


def dfs(s,r):
  global leafs
  if r==s:
    return
  visited.add(s)

  leaf = True
  for e in graph[s]:
    if e not in visited and e!=r:
      leaf = False
      dfs(e,r)

  if leaf:
    leafs+=1
  #print(f"leaf: {s}는 {leaf}")


dfs(start, remove)

print(leafs)
