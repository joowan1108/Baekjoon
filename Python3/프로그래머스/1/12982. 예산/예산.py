def solution(d, budget):
    d.sort()
    idx = 0
    result = 0
    while budget>0:
        if idx==len(d):
            break
        if budget >= d[idx]:
            budget-=d[idx]
            result+=1
            idx+=1
        
        else:
            break
            
    return result