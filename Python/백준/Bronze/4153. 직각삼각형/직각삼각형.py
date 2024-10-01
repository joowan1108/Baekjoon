# Online Python-3 Compiler (Interpreter)
import sys
input = sys.stdin.readline

while(True):
    nums = list(map(int, input().strip().split()))
    if(nums.count(0)==len(nums)):
        break
    nums.sort()
    if(nums[2]**2 == nums[1]**2 + nums[0]**2):
        print("right")
    else:
        print("wrong")