import sys

input = sys.stdin.readline

num_buildings = int(input())
buildings = []
for _ in range(num_buildings):
    buildings.append(int(input()))

can_watch = [0]*num_buildings

stack = [(buildings[0],0)]

for i in range(1,num_buildings):
    while stack:
        if buildings[i] >= stack[-1][0]:
            h,idx = stack.pop()
            can_watch[idx]=i-idx-1
        else:
            break
    stack.append((buildings[i], i))

if stack:
    for h,idx in stack:
        can_watch[idx] = num_buildings-1-idx
        

print(sum(can_watch))



