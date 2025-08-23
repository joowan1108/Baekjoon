import sys
input = sys.stdin.readline

"""
dp 배열에 현재까지 받은 이익을 저장한다.

미래에 얻을 수 있다고 생각한 이익dp[i+Ti]과 현재 벌 예정인 이익 (Pi) + 지금까지의 이익(dp[i])을 비교 
"""

n= int(input())
dp = [0]*(n+1)

T = []
P = []

for _ in range(n):
  t,p = map(int,input().split())
  T.append(t)
  P.append(p)

for i in range(n):
  for j in range(i+T[i], n+1):
    dp[j] = max(dp[j], P[i] + dp[i])


print(max(dp))




