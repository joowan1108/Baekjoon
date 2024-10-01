# Online Python-3 Compiler (Interpreter)
import sys
import math
input = sys.stdin.readline

T = int(input().strip())
#15층 14호실
arr=[[0 for _ in range(14)] for _ in range(15)]
arr[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#arr를 미리 만들어야함
def calculateArr(floor, room):
    fillval = 0
    for r in range(room+1):
        fillval += arr[floor-1][r]
    arr[floor][room] = fillval
    
for i in range(14):
    for j in range(14):
        calculateArr(i+1,j)

for _ in range(T):
    k = int(input())
    n=int(input())
    print(arr[k][n-1])
    
