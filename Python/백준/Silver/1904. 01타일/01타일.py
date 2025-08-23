import sys
input = sys.stdin.readline

"""
1이랑 2로 N을 채우는 모든 가짓수 구하기
dp[i]는 크기가 i인 수열의 개수이다. 
"""

n = int(input())
dp = [0]*(1000001)
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
  dp[i] = (dp[i-1]+dp[i-2])%15746

print(dp[n])

