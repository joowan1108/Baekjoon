import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
m,n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

normal_move = [(1,0),(-1,0),(0,1),(0,-1)]
horse_move = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]


#각 층은 horse move를 사용한 횟수이다.
visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(31)]

start_h, start_w = 0,0
target_h, target_w = n-1, m-1


q = deque([(start_h, start_w,0)])
visited[0][start_h][start_w] = 0
ans = -1


while q:
    h,w,c = q.popleft()
    #도달했을 떄 처리 방법
    if h==n-1 and w==m-1:
        ans = c + visited[c][h][w]
        break
    
    for dh, dw in normal_move:
        new_h, new_w = h+dh, w+dw
        if 0<=new_h<n and 0<=new_w<m and graph[new_h][new_w]==0 and visited[c][new_h][new_w] == -1:
            q.append((new_h,new_w,c))
            visited[c][new_h][new_w] = visited[c][h][w]+1

    #horse move를 사용한다면
    if c<k:
        for dh, dw in horse_move:
            new_h, new_w = h+dh, w+dw
            if 0<=new_h<n and 0<=new_w<m and graph[new_h][new_w]==0 and visited[c+1][new_h][new_w]==-1:
                q.append((new_h,new_w,c+1))
                visited[c+1][new_h][new_w] = visited[c][h][w]

print(ans)


