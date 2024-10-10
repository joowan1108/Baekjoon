import sys
from collections import deque

input = sys.stdin.readline
moves = [(0,1),(0,-1),(1,0),(-1,0)]

#탐색하는 영역이 작기 때문에 속도가 더 빠른 bfs 사용
def bfs(x,y, farm, n, m):
    q = deque()
    q.append((x,y))
    while q:
        a,b = q.popleft()
        for dx, dy in moves:
            aa = a+dx
            bb = b+dy
            if(aa>=0 and aa<n and bb>=0 and bb<m):
                if(farm[aa][bb]==1):
                    q.append((aa,bb))
                    farm[aa][bb]=0
    return farm 
    
t = int(input())
for _ in range(t):
    cnt=0
    m,n,k = map(int, input().split())
    
    farm = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int, input().split())
        farm[y][x]=1
    
    for i in range(n):
        for j in range(m):
            if(farm[i][j]==1):
                farm=bfs(i,j, farm, n,m)
                cnt+=1
    
    print(cnt)
    
    
    
    
    