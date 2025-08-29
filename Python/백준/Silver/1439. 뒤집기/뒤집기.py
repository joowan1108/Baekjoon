import sys
input = sys.stdin.readline

"""
이어지는 0을 하나의 0으로
이어지는 1을 하나의 1로 축소

그 다음 각 숫자들이 나온 횟수 중 최솟값이 최소 횟수
"""

s = input().rstrip()

n = len(s)
dict = {'0': 0, '1': 0}
past = s[0]
for i in range(1,n):
  if past == s[i]:
    continue
  else:
    dict[past]+=1
    past = s[i]
  if i==n-1:
    dict[s[i]]+=1
dict[past]+=1

print(min(dict['0'], dict['1']))
    
  



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  