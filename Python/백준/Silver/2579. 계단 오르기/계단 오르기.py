import sys
input = sys.stdin.readline

n = int(input())

stairs = [0]*301
for i in range(1,n+1):
	stairs[i]=int(input())

#4개의 칸 안에서 4번째의
#수는 마지막 + 마지막-2 vs 마지막 + 마지막-1 + 마지막-3

dp = [0]*(301)

dp[1]= stairs[1]
dp[2]= stairs[1]+stairs[2]
dp[3]= max(stairs[1]+stairs[3],stairs[2]+stairs[3])

for i in range(4, len(dp)):
	dp[i]=max(stairs[i]+dp[i-2], stairs[i]+stairs[i-1]+dp[i-3])

print(dp[n])

