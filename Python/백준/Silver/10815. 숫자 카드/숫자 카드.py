import sys

n = int(sys.stdin.readline().rstrip())

n_lst = list(map(int, (sys.stdin.readline().rstrip()).split()))

n_lst.sort()

m = int(sys.stdin.readline().rstrip())

m_lst = list(map(int, (sys.stdin.readline().rstrip()).split()))

def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if(arr[mid] == target):
            return 1
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return 0

for num in m_lst:
    print(binary_search(n_lst, num), end=' ')


    




