import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

faculty = []

for _ in range(n):
    lst = list(map(int, input().split()))
    faculty.append(lst)

max_area = 0


moves = [(1,0), (-1,0), (0,1), (0,-1)]

twos = []
for i in range(n):
    for j in range(m):
        if faculty[i][j]==2:
            twos.append((i,j))


def get_area():
    global max_area
    tmp = [row[:] for row in faculty]
    q = deque(twos)
    while q:
        h, w = q.popleft()
        for dh, dw in moves:
            new_h = h+dh
            new_w = w+dw
            if 0<=new_h<n and 0<=new_w<m and tmp[new_h][new_w]==0:
                tmp[new_h][new_w]=2
                q.append((new_h, new_w))
                
    
    area = 0
    for i in range(n):
        area +=tmp[i].count(0)
    
    max_area = max(area, max_area)




def backtrack(wall):
    if wall==3:
        get_area()
        return

    for i in range(n):
        for j in range(m):
            if faculty[i][j]==0:
                faculty[i][j] = 1
                backtrack(wall+1)
                faculty[i][j]=0
    

backtrack(0)
print(max_area)