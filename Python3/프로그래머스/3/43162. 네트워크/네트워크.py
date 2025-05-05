def dfs(computers, visited, node):
    visited[node]=True
    for i,connected in enumerate(computers[node]):
        if not visited[i] and connected==1:
            dfs(computers, visited, i)
        

def solution(n, computers):
    visited = [False]*n
    ans = 0
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            ans+=1
    return ans
        
    