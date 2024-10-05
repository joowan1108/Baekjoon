import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    length, target = map(int, input().split())
    q = deque(map(int, input().split()))
    order = 1
    while True:
        max_prior = max(q)
        temp=q.popleft()
        #조사받는게 최대값일 때
        if(temp==max_prior):
            #조사받는게 target이면 끝
            if(target==0):
                break
            #조사받는게 target이 아니면 하나가 없어지므로 조사받는 순번 당겨짐
            else:
                order+=1
                target-=1
        #조사 받는게 최대가 아닐 때
        else: 
    #target가 조사받는데 target이 최대가 아니면 순번 밀리기
            if(target==0):
                q.append(temp)
                target=(len(q)-1)
            else:
                #target가 아니면 target 조사받는 순번 당겨짐
                q.append(temp)
                target-=1
    
    print(order)
        
        
        
        
                    
                    
        
    