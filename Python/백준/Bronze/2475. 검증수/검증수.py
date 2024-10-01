# Online Python-3 Compiler (Interpreter)
import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))

total_sum=0
for i in range(len(nums)):
    total_sum+=nums[i]**2

serial = total_sum%10
print(serial)
        
