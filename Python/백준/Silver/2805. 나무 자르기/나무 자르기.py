import sys
input = sys.stdin.readline

n,m = map(int, input().split())

trees = list(map(int, input().split()))

def binarysearch():
    start = 0
    end = max(trees)
    while start<=end:
        result=0
        mid = (start+end)//2
        for t in trees:
            if(t>=mid):
                result+=(t-mid)
        #부족하다면
        if result<m:
            end = mid-1
        else:
            start = mid+1
    print(end)

binarysearch()