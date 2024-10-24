import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

campus = []

h = 0
w = 0
tmp = 0
for _ in range(n):
	row = input().rstrip()
	campus.append(row)
	for i in range(len(row)):
		if(row[i]=='I'):
			w = i
			tmp=1
	if(tmp!=1):
		h+=1

#h,w = 도연이의 위치
cnt = 0
moves = [(-1,0), (1,0), (0,-1), (0,1)]
def bfs(start_h, start_w):
	global cnt
	q = deque()
	visited = [[False]*(m) for _ in range(n)]
	q.append((start_h, start_w))
	visited[start_h][start_w]=True
	while q:
		h_, w_ = q.popleft()
		for move_h, move_w in moves:
			new_h = h_ + move_h
			new_w = w_ + move_w
			if(0<=new_h<n and 0<=new_w<m and visited[new_h][new_w]==False and campus[new_h][new_w]!='X'):
				visited[new_h][new_w]=True
				q.append((new_h, new_w))
				if(campus[new_h][new_w]=='P'):
					cnt+=1
					


bfs(h,w)
if(cnt==0):
	print('TT')
else:
	print(cnt)
	
