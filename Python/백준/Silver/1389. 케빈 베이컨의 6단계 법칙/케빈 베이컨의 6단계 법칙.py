import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
	a,b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

def bfs(start):
	q = deque([start])
	visited = set()
	visited.add(start)
	distance = [0 for _ in range(n+1)]
	while q:
		node = q.popleft()
		for s in graph[node]:
			if(s not in visited):
				q.append(s)
				visited.add(s)
				distance[s]=distance[node]+1
	return sum(distance)

result = []
for i in range(1, n+1):
	result.append(bfs(i))

print(result.index(min(result))+1)


	
	
	
				
				
		
	

	
	


		