def backtrack(dungeons, energy, visited, cnt, min_):
    ans = cnt
    for i in range(len(dungeons)):
        if visited[i]==True:
            continue
        if visited[i] == False and energy >= dungeons[i][0]:
            visited[i]=True
            ans = max(ans, backtrack(dungeons, energy-dungeons[i][1], visited, cnt+1, min_))
            visited[i]=False
    return ans

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    min_ = min([s[0] for s in dungeons])
    ass =  backtrack(dungeons, k, visited, 0, min_)
    return ass
    
