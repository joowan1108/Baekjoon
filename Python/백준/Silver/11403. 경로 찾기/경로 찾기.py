import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

g = []
for _ in range(n):
	g.append(list(map(int, input().split())))

for k in range(n):
	for a in range(n):
		for b in range(n):
			if(g[a][k]+g[k][b]==2):
				g[a][b]=1
				

for i in range(n):
	for j in range(n):
		print(g[i][j], end=' ')
	print()


	
