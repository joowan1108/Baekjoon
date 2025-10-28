import sys
input = sys.stdin.readline

string = input().rstrip()
str = [str(s) for s in string]
stack = []

num = 0
mult = 1
valid = True

for i in range(len(str)):
  #괄호가 열리자마자 안에 있는건 * k가 된다.
  if str[i] == '(':
    stack.append(str[i])
    mult *= 2
  elif str[i] == '[':
    stack.append(str[i])
    mult *= 3
  elif str[i] == ']':
    if not stack or stack[-1] == '(':
      valid = False
      break
    elif stack[-1] == '[' and str[i-1] == '[':
      #바로 닫힐 때
      num+=mult
    # 닫힌 괄호가 왔다는 것은 []의 곱하는 효과가 끝난 것
    stack.pop()
    mult //= 3
  else:
    if not stack or stack[-1] == '[':
      valid = False
      break
    elif stack[-1] == '(' and str[i-1] == '(':
      num+=mult
    # 닫힌 괄호가 왔다는 것은 ()의 곱하는 효과가 끝난 것
    stack.pop()
    mult //= 2



if valid and not stack:
  print(num)
else:
  print(0)
    
