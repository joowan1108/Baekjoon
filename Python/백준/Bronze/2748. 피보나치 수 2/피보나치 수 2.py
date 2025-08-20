import sys

input = sys.stdin.readline

n = int(input())

"""
Fn = Fn-1 + Fn-2의 문제가 반복되고 이 문제들이 합쳐짐으로써 답이 나온다
"""
if n==1 or n==2:
  print(1)
else:
  fibos = [0]*(n+1)
  fibos[1] = 1
  fibos[2] = 1
  
  for i in range(3, n+1):
    fibos[i] = fibos[i-1] + fibos[i-2]
  
  print(fibos[n])


  


