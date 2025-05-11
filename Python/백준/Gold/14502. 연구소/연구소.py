import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n,m = map(int, input().split())

faculty = []

for _ in range(n):
    lst = list(map(int, input().split()))
    faculty.append(lst)

max_area = 0


moves = [(1,0), (-1,0), (0,1), (0,-1)]

zeros = []
twos = []
for i in range(n):
    for j in range(m):
        if faculty[i][j]==0:
            zeros.append((i,j))
        elif faculty[i][j]==2:
            twos.append((i,j))




#wall을 설치해야 하는 곳 후보들
combs = combinations(zeros, 3)

#각 후보들에 wall 설치해서 bfs하고 max_area를 계속 갱신
def spread_virus(tmp):
    q = deque(twos)
    while q:
        h,w = q.popleft()
        for dh, dw in moves:
            new_h = h+dh
            new_w = w+dw
            if 0<=new_h<n and 0<=new_w<m and tmp[new_h][new_w]==0:
                tmp[new_h][new_w]=2
                q.append((new_h, new_w))

    return tmp

#0의 개수 확인
def get_area(tmp):
    global max_area
    cnt=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                cnt+=1
    max_area = max(max_area, cnt)


def place_wall():
    for c1, c2, c3 in combs:
        x1, y1 = c1[0], c1[1]
        x2, y2 = c2[0], c2[1]
        x3, y3 = c3[0], c3[1]
        
        tmp_faculty = [row[:] for row in faculty]

        tmp_faculty[x1][y1]=1
        tmp_faculty[x2][y2]=1
        tmp_faculty[x3][y3]=1
    
        tmp_faculty = spread_virus(tmp_faculty)
        get_area(tmp_faculty)
        


place_wall()

print(max_area)

    