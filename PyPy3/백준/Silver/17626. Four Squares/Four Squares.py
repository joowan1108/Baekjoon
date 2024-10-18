import sys, math
input = sys.stdin.readline

n = int(input())

nums = [i for i in range(1,50000+1)]
dp=[0]*(50000+1)


for num in nums:
	if(int(math.sqrt(num))**2==num):
		dp[num]=1

for i in range(2,len(dp)):
	t=1e9
	for j in range(1, int(math.sqrt(i))+1):
		t=min(t,dp[i-j**2])
		dp[i]=t+1
print(dp[n])


	

	