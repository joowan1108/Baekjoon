import sys
import heapq

inf = int(1e9)
input = sys.stdin.readline
test = int(input())

def dijkstra(graph):
        global times
        global c
        q = []
        heapq.heappush(q, (0,c))
        times[c]=0
        while q:
            time, comp = heapq.heappop(q)
            if(times[comp] < time):
                continue
            for computer, cost in graph[comp]:
                new_time = cost + time
                if(new_time<times[computer]):
                    times[computer] = new_time
                    heapq.heappush(q, (new_time, computer))

                    
for _ in range(test):
    n,d,c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int, input().split())
        graph[b].append((a,s))

    times = [inf for _ in range(n+1)]
    dijkstra(graph)
    comp_cnt = 0
    for i in range(1, n+1):
        if times[i]!=inf:
            comp_cnt+=1
        else:
            times[i]=0
    times[0]=0
    print("{} {}".format(comp_cnt, max(times)))
    
                
