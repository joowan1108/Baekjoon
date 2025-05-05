from collections import deque

moves = [(-1,0), (1,0), (0,1), (0,-1)]

def solution(maps):
    visited = set()
    start = (0,0,1)
    q = deque([start])
    visited.add(start)
    
    while q:
        h,w,l = q.popleft()
        if h==len(maps)-1 and w==len(maps[0])-1:
            return l
        for move in moves:
            dh, dw = move
            new_h, new_w = h+dh, w+dw
            if new_h<0 or new_h>=len(maps) or new_w<0 or new_w >= len(maps[0]):
                continue
            if (new_h, new_w) not in visited and maps[new_h][new_w]==1:
                q.append((new_h, new_w, l+1))
                visited.add((new_h, new_w))
    return -1  