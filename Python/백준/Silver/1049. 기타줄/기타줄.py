import sys
input = sys.stdin.readline

n,m = map(int, input().split())
six = sys.maxsize
one = sys.maxsize
for _ in range(m):
  a,b = map(int, input().split())
  six = min(six, a)
  one = min(one, b)

"""
6 package가 one * 6으로 사는 것보다 싸다면 
일단 6으로 최대한 다 채우고 나머지를 살 때 ones로 사는게 나은지 package로 사는게 나은지 비교

6 package가 one * 6보다 비싸다면 다 ones로 채우기
"""
cost = 0
if six < one*6:
  cnt = n // 6
  n -= cnt * 6
  cost = six*cnt
  #one으로 사는게 더 싸다면
  if one*n < six:
    cost += one*n
  else:
    cost += six

else:
  cost = n*one

print(cost)
    

    
        
    
  


  
    
  



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  