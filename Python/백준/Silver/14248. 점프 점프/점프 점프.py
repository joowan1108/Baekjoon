import sys
from collections import defaultdict, deque
input = sys.stdin.readline

avails = 1

n = int(input())
jumps = list(map(int, input().split()))
start = int(input())

def valid_jump(num):
  if num>n or num<1:
    return False
  return True

graph = defaultdict(list)

for i in range(1,n+1):
  first = i+jumps[i-1]
  second = i-jumps[i-1]
  if valid_jump(first):
    graph[i].append(first)
  if valid_jump(second):
    graph[i].append(second)


def bfs(s):
  global avails
  q = deque()
  visited = set()
  q.append(s)
  visited.add(s)
  while q:
    node = q.popleft()
    for adj_node in graph[node]:
      if adj_node not in visited:
        visited.add(adj_node)
        q.append(adj_node)
        avails+=1

bfs(start)
print(avails)

        
  
    

    
  

