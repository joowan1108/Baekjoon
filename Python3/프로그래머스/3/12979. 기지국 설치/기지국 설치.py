def solution(n, stations, w):
    s_idx = 0
    idx = 1
    cnt = 0
    
    while idx<=n:
        if s_idx < len(stations) and stations[s_idx]+w>= idx >= stations[s_idx]-w:
            idx = stations[s_idx]+w+1
            s_idx+=1
        else:
            cnt+=1
            idx+=2*w+1
    
    return cnt
            
            