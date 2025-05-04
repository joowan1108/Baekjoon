def find(parent, i):
    if parent[i]==i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    root1 = parent[x]
    root2 = parent[y]
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    elif rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root1] = root2
        rank[root2] += 1

def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])
    parents = [i for i in range(n)]
    rank = [0]*n
    min_cost = 0
    nodes_num = 0
    
    for cost in costs:
        if nodes_num==n-1:
            break
        x,y,c = cost[0], cost[1], cost[2]
        x_root = find(parents, x)
        y_root = find(parents, y)
        if x_root != y_root:
            union(parents, rank, x_root, y_root)
            min_cost+=c
            nodes_num+=1
    return min_cost
            
    
    

    