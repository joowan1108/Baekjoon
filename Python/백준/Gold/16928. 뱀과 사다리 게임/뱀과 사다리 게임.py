import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

dist = [0 for _ in range(101)]
stairs = dict()
snakes = dict()
for _ in range(n):
	stair_start, stair_end = map(int, input().split())
	stairs[stair_start] = stair_end
	

for _ in range(m):
	snake_start, snake_end = map(int, input().split())
	snakes[snake_start] = snake_end
	

def nextMoves(cur):
	return cur+1, cur+2, cur+3, cur+4, cur+5, cur+6
		
	
def bfs():
	q = deque()
	visited = [False]*(101)
	visited[1]=True
	q.append(1)
	while q:
		tmp = q.popleft()
		for move in nextMoves(tmp):
			if(move<=100 and not visited[move]):
				if move in snakes:
					move = snakes[move]
				elif move in stairs:
					move = stairs[move]
				if not visited[move]:
					q.append(move)
					visited[move]=True
					dist[move]=dist[tmp]+1
					
bfs()
print(dist[100])
				
		
	
	

	
	
	
		
	
