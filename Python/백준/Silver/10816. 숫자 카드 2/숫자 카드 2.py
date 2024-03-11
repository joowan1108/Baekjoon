from collections import Counter
n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

freq = Counter(n_lst)
n_set = set(n_lst)
n_set = sorted(n_set)

def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while start <=end:
        mid = (start+end)//2
        if(target == arr[mid]):
            return True
        elif(target > arr[mid]):
            start = mid+1
        else:
            end = mid-1
    return False
freq_lst = []
for num in m_lst:
    if(binary_search(n_set, num)):
        freq_lst.append(freq[num])
    else:
        freq_lst.append(0)
for s in freq_lst:
    print(s, end=' ')
    