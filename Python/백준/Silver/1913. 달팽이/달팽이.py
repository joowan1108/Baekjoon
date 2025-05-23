import sys

input = sys.stdin.readline

N = int(input())
target = int(input())

arr = [[0]*N for _ in range(N)]

start_col = 0
end_col = N-1

start_row = 0
end_row = N-1

num = N**2

h,w = 0,0

def is_target(number):
    if number == target:
        return True
    return False


while start_col <= end_col and start_row <= end_row:
    for i in range(start_row, end_row+1):
        arr[i][start_col] = num
        if is_target(num):
            h,w = i, start_col
        num-=1
    start_col += 1
    
    for i in range(start_col, end_col+1):
        arr[end_row][i] = num
        if is_target(num):
            h,w = end_row, i
        num-=1
    end_row-=1

    for i in range(end_row, start_row-1, -1):
        arr[i][end_col] = num   
        if is_target(num):
            h,w = i, end_col
        num -= 1
    end_col-=1

    for i in range(end_col, start_col-1, -1):
        arr[start_row][i] = num
        if is_target(num):
            h,w = start_row, i
        num -= 1
    start_row+=1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()

print(f"{h+1} {w+1}")


    