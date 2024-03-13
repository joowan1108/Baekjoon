import sys

n, m = map(int, (sys.stdin.readline()).split())

trees = list(map(int, (sys.stdin.readline()).split()))

start = 0
end = max(trees)
result = 0
while start<=end:
    mid = (start+end)//2
    sum = 0
    for t in trees:
        if(t>mid):
            sum+=t-mid
    if(sum>=m):
        result = mid
        start = mid + 1
    else:
        end = mid-1
        
    

print(result)

    




