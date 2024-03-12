import sys

n = int(sys.stdin.readline())
lst = list(map(int, input().split()))

lst_unique = sorted(set(lst))

def binary_search(arr, t):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if(arr[mid] == t):
            return mid
        elif(arr[mid]>t):
            end = mid-1
        else:
            start = mid+1
    return None

for num in lst:
    num = binary_search(lst_unique, num)
    print(num, end = ' ')




