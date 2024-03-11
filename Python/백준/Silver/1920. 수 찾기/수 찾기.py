n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

def binary_search(array, target):
    start, end = 0, len(array)-1
    while(start<=end):
      mid = (start+end)//2
      if(target==array[mid]):
        return 1
      elif(target>array[mid]):
        start = mid+1
      else:
        end = mid-1
    return 0

for i in range(m):
    print(binary_search(a, b[i]))