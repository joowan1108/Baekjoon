import sys
import heapq
import copy
inf = int(1e9)

input = sys.stdin.readline

n,m,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
students = [0 for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e,t))

def find_path(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start]=0
    while q:
        dist, node = heapq.heappop(q)
        if(distance[node] < dist):
            continue
        for nod in graph[node]:
            new_dist = dist + nod[1]
            if(new_dist<distance[nod[0]]):
                distance[nod[0]] = new_dist
                heapq.heappush(q,(new_dist, nod[0]))


for i in range(1, n+1):
    distance = [inf]*(n+1)
    find_path(i)
    students[i] = distance[x]

distance = [inf]*(n+1)
find_path(x)

for i in range(1,n+1):
    students[i]+=distance[i]
    
for i in range(1,n+1):
    if(students[i]==inf):
        students[i]=0

print(max(students))

    


    
