import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
  n,m,w = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  for _ in range(m):
    s,e,t = map(int, input().split())
    graph[s].append((e,t))
    graph[e].append((s,t))
    
  for _ in range(w):
    s,e,t = map(int, input().split())
    graph[s].append((e,-t))

  
  distances = [int(1e9)] * (n+1)
  cycle = False

  for checks in range(n+1):
    for mid in range(1,n+1):
      for end,cost in graph[mid]:
        if distances[end] > distances[mid] + cost:
          distances[end] = distances[mid] + cost
          # n번째 check에도 이 경우가 발생한다면 음의 순환 존재
          if checks == n:
            cycle = True
  if cycle:
    print("YES")
  else:
    print("NO")
            