import sys
input = sys.stdin.readline

n = int(input())
liqs = list(map(int, input().split()))
liqs.sort()

min_sum = int(3e9)
answer = []



for fixed in range(n-2):
  left = fixed+1
  right = n-1
  while left < right:
    tmp = liqs[fixed] + liqs[left] + liqs[right]
    if abs(tmp) <= min_sum:
      min_sum = abs(tmp)
      answer = [liqs[fixed], liqs[left], liqs[right]]
    if tmp < 0:
      left+=1
    elif tmp > 0:
      right-=1
    else:
      answer.sort()
      print(*answer)
      sys.exit()
answer.sort()
print(*answer)
    
    
    
  
    
        
        
    

        
      
    
    
  

  
