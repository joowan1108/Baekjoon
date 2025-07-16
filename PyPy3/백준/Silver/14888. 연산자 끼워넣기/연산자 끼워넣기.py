import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
"+ - * //"
maximum = -float('inf')
minimum = float('inf')

#iter는 연산 횟수, last_num은 저번 연산 결과, i는 다음 숫자 가리키는 index
def backtrack(iter, i, last_num):
  global maximum, minimum
  if iter == n-1:
    maximum = max(maximum, last_num)
    minimum = min(minimum, last_num)
    return
  for idx in range(4):
    if opers[idx]!=0:
      tmp = last_num
      #+
      if idx==0:
        last_num+=nums[i]
      #-
      elif idx==1:
        last_num-=nums[i]
      #*
      elif idx==2:
        last_num*=nums[i]
      #/
      else:
        last_num = last_num // nums[i] if last_num>=0 else -((-last_num)//nums[i])
      opers[idx]-=1
      backtrack(iter+1, i+1, last_num)
      opers[idx]+=1
      last_num = tmp


backtrack(0,1,nums[0])
print(maximum)
print(minimum)