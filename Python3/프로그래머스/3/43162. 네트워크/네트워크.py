def find(parents, comp):
    if parents[comp]!=comp:
        parents[comp] = find(parents, parents[comp])
    return parents[comp]
    

def union(parents, rank, comp1, comp2):
    root1 = find(parents, comp1)
    root2 = find(parents, comp2)
    
    if root1 != root2:
        if rank[root1]<rank[root2]:
            parents[root1] = root2
        elif rank[root1] == rank[root2]:
            parents[root1] = root2
            rank[root2]+=1
        else:
            parents[root2] = root1
    

def solution(n, computers):
    parents = [i for i in range(n)]
    rank = [0]*n
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                union(parents, rank, i, j)
    
    for i in range(len(parents)):
        parents[i] = find(parents, i)
    network = set(parents)
    return len(network)
    
    

    
    