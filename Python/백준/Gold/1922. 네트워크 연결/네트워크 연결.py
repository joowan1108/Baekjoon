import sys
input = sys.stdin.readline

"""
모든 정점들을 최소한의 weight로 연결해야 하므로 MST를 구하는 문제임을 알 수 있다.

"""

n = int(input())
m = int(input())


edges = []
for _ in range(m):
  a,b,c = map(int, input().split())
  edges.append((a,b,c))

edges.sort(key=lambda x: x[2])

parents = [i for i in range(n+1)]

total_min = 0

def find(a):
  if parents[a] == a:
    return a
  else:
    return find(parents[a])

  

def union(a,b):
  parent_a = find(a)
  parent_b = find(b)
  #사이클 형성한다면
  if parent_a == parent_b:
    return 0

  #사이클 형성하지 않는다면 부모 update
  else:
    if parent_a > parent_b:
      parents[parent_a] = parent_b
    else:
      parents[parent_b] = parent_a
    return c
    
total_min = 0

for a,b,c in edges:
  total_min += union(a,b)

print(total_min)
  
  
    
    
    
  
  

      
  















