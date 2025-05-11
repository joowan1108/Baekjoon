import heapq

moves = [(1,0), (-1,0), (0,1), (0,-1)]

def solution(land, height):
    visited = [[False]*len(land[0]) for _ in range(len(land))]
    q = []
    heapq.heappush(q, (0, 0, 0))
    total = 0
    while q:
        cost, h, w = heapq.heappop(q)
        if visited[h][w]==True:
            continue
        
        visited[h][w]=True
        total+=cost
        for dh, dw in moves:
            new_h = h + dh
            new_w = w + dw
            if 0<=new_h<len(land) and 0<=new_w<len(land[0]) and not visited[new_h][new_w]:
                actual_cost = abs(land[new_h][new_w] - land[h][w])
                if actual_cost > height:
                    heapq.heappush(q, (actual_cost, new_h, new_w))
                else:
                    heapq.heappush(q, (0, new_h, new_w))
        
    return total     
        