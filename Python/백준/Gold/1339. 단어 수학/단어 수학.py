import sys
input = sys.stdin.readline

"""
자릿수를 가장 많이 가져가는 알파벳부터 큰 수를 부여하면 된다 --> greedy
"""

n = int(input())
cur = 9
alphabets = dict()
nums = []
for _ in range(n):
  nums.append(input().rstrip())

for num in nums:
  length=len(num)-1
  for nu in num:
    if nu in alphabets:
      alphabets[nu] += 10**length
    else:
      alphabets[nu] = 10**length
    length-=1

alphabets = sorted(alphabets.values(), reverse=True)
ans = 0
for alpha in alphabets:
  ans += alpha * cur
  cur -= 1

print(ans)



        
    
  
    
    
      
  



  
  
      
  
      
    
      
    
  