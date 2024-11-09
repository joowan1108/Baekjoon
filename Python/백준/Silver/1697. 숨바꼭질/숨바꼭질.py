import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

max_val = max(n, k) * 2 + 1
visited = [False] * (max_val + 1)
path = [float('inf')] * (max_val + 1)

def getMoves(temp):
    return temp-1, temp+1, temp*2

def bfs(start):
    visited[start] = True
    path[start] = 0
    q = deque()
    q.append(start)
    while q:
        tmp = q.popleft()
        for pos in getMoves(tmp):
            if 0 <= pos <= max_val and not visited[pos]:
                visited[pos] = True
                path[pos] = path[tmp] + 1
                q.append(pos)

if(n==k):
	print(0)
else:
	bfs(n)
	print(path[k])
