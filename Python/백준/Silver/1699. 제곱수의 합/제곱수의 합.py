import sys
import  math
input = sys.stdin.readline

"""
dp[i]에 자연수 i가 최소 몇개의 제곱수로 표현되는지 저장

이때 dp[i+제곱수] = min(dp[i+제곱수], dp[i]+1)로 update
제곱수는 n보다 작은 제곱수 중 하나를 골라 모든 i에 대해서 적용해야 한다.
"""
n = int(input())
dp = [sys.maxsize]*(n+1)
dp[0] = 0
squares = []
for i in range(1, int(math.sqrt(n))+1):
  if i**2 <= n:
    squares.append(i**2)

for i in range(1, n+1):
  for sq in squares:
      if i - sq >= 0:
          dp[i] = min(dp[i], dp[i - sq] + 1)

        
print(dp[n])
  

    
