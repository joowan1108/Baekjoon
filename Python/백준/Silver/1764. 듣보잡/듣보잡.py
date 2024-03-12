n, m = map(int, input().split())
n_lst = []
m_lst = []
for _ in range(n):
    n_lst.append(input())
for _ in range(m):
    m_lst.append(input())
    
n_lst.sort()
m_lst.sort()

def binary_search(arr,target):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if(arr[mid]==target):
            return True
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return False

result =[]

for p in n_lst:
    if(binary_search(m_lst, p)):
        result.append(p)

print(len(result))
for l in result:
    print(l)
    
    