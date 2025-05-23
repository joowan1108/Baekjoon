import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = []

for _ in range(n):
    nums.append(list(map(int, input().rstrip())))



for i in range(1,n):
    for j in range(1,m):
        up, left, diag = nums[i][j-1], nums[i-1][j], nums[i-1][j-1]
        if nums[i][j]==1:
            nums[i][j] = min([up, left, diag]) + 1

max_ = max([max(row) for row in nums])

print(max_**2)

