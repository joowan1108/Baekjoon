def solution(want, number, discount):
    wanted = dict()
    for i in range(len(want)):
        wanted[want[i]] = number[i]
    
    ans = 0
    for i in range(0,len(discount)-9):
        dis = dict()
        is_true = True
        for j in range(i,i+10):
            if discount[j] in dis:
                dis[discount[j]]+=1
            else:
                dis[discount[j]]=1
        if dis == wanted:
            ans+=1
    return ans
            
            
        
        