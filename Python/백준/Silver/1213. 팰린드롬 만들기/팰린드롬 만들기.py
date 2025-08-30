import sys
from collections import Counter, deque
input = sys.stdin.readline

"""
알파벳들을 사전순으로 나열
이들의 빈도수를 계산 counter
빈도가 2보다 크거나 같다면 2보다 작아질 때까지 앞뒤에 추가
"""

string = list(input().rstrip())
counter = Counter(string)
string.sort()
front = deque()
end = deque()
ones = set()

for s in string:
  while counter[s] >= 2:
    counter[s] -= 2
    front.append(s)
    end.appendleft(s)
  if counter[s] == 1:
    ones.add(s)
if len(ones) <= 1:
  print(''.join(front + deque(ones) + end))
else:
  print("I'm Sorry Hansoo")

  
    


    
        
    
  


  
    
  



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  