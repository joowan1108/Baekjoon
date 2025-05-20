import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

lst = [arr[0]]

for i in range(0, len(arr)):
    if lst[-1] < arr[i]:
        lst.append(arr[i])
    else:
        idx = bisect_left(lst, arr[i])
        lst[idx]=arr[i]
        

print(len(lst))
        
