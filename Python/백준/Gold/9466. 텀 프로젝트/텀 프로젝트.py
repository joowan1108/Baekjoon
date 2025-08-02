import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0]*(n+1)
    lst = list(map(int, input().split()))
    for i in range(1,n+1):
        graph[i] = lst[i-1]

    visited = [False]*(n+1)
    cycled = 0

    def dfs(start):
        global cycled
        track.append(start)
        visited[start]=True
        new_start = graph[start]
        #사이클 형성한다면
        if visited[new_start]:
            for i in range(len(track)):
                if track[i] == new_start:
                    cycled += len(track[i:])
        #사이클 형성 안 한다면
        else:
            dfs(new_start)

    #모든 노드에 대해서 dfs해서 cycle 알아내자.
    for start in range(1,n+1):
        if visited[start] == False:
            track = []
            dfs(start)
    
    print(n-cycled)

