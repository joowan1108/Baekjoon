import sys
input = sys.stdin.readline

s = str(input()).rstrip()
n = len(s)
"""
뒤에는 0, 앞에는 합이 3의 배수여야함
"""

nums = []
for a in s:
  nums.append(int(a))

nums.sort(reverse=True)
ans = 0

if nums[-1] == 0:
  nums.pop()
  if sum(nums)%3 == 0:
    ans = ''.join(map(str, nums)) + '0'
    print(int(ans))
  else:
    print(-1)
else:
  print(-1)

      
  



  
  
      
  
      
    
      
    
  