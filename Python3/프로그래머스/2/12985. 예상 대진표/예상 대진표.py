def solution(n,a,b):
    plays = 0
    while a!=b:
        a = (a+1)//2
        b = (b+1)//2
        plays+=1
        
    return plays
        
        