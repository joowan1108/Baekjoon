import sys
input = sys.stdin.readline

k,n = map(int, input().split())

lines = [int(input()) for _ in range(k)]

#범위가 정해져있는 상태에서 조건을 만족하는 값을 구하는 것
def binarysearch(arr):
    start = 1
    end = max(arr)
    while start<=end:
        mid = (start+end)//2
        count=0
        for line in lines:
            #나머지가 만들 수 있는 랜선의 개수
            count+=(line//mid)
        if(count>=n): #--> 최대 랜선 길이를 구하는 것이므로 count>=n을 해야함
        
            #만들어지는 랜선의 개수가 너무 많다면 자르는 길이가 너무 짧은 것
            start=mid+1
        else:
            #만들어지는 랜선의 개수가 적다면 자르는 길이를 늘려야 한다
            end = mid-1
    return end
    
print(binarysearch(lines))
