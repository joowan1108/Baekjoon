import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

"""
부분 연속합에 하나의 숫자로 바꾸나 아니면 지금까지의 합 + 숫자로 바꾸나를 반복함.

부분 연속합의 최댓값을 하나의 변수에 저장
"""
max_val = float('-inf')
ans = float('-inf')
for i in range(n):
  max_val = max(nums[i], max_val+nums[i])
  ans = max(ans, max_val)

print(ans)
  


