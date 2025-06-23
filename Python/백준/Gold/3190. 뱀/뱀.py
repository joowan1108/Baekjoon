import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

apples = set()
q = deque()
q.append((1,1))
worm = set()
worm.add((1,1))

moves = dict()
moves['up'] = (-1,0)
moves['right'] = (0,1)
moves['down'] = (1,0)
moves['left'] = (0,-1)

for _ in range(k):
    row, col = list(map(int, input().split()))
    apples.add((row,col))

l = int(input())
commands = ['n']*(10001)
for _ in range(l):
    x,c = input().split()
    x = int(x)
    commands[x] = c

cur_move = 'right'
time = 0
while True:
    time += 1

    cur_head_h, cur_head_w = q[0]
    dh, dw = moves[cur_move]
    next_head_h, next_head_w = cur_head_h+dh, cur_head_w+dw
    #자기 자신이나 벽 닿을 때
    if (next_head_h, next_head_w) in worm or (next_head_h<1 or next_head_h>n) or (next_head_w<1 or next_head_w>n):
        break

    #간 곳에 사과 있을 때
    if (next_head_h, next_head_w) in apples:
        apples.remove((next_head_h, next_head_w))
        q.appendleft((next_head_h, next_head_w))
        worm.add((next_head_h, next_head_w))

    else:
        #사과 없다면 움직이고 꼬리 제거
        q.appendleft((next_head_h, next_head_w))
        worm.add((next_head_h, next_head_w))
        h,w = q.pop()
        worm.remove((h,w))

    if commands[time]!='n':
        if commands[time]=='L':
            if cur_move == 'right':
                cur_move = 'up'
            elif cur_move == 'left':
                cur_move = 'down'
            elif cur_move == 'up':
                cur_move = 'left'
            else:
                cur_move = 'right'
        else:
            if cur_move == 'right':
                cur_move = 'down'
            elif cur_move == 'left':
                cur_move = 'up'
            elif cur_move == 'up':
                cur_move = 'right'
            else:
                cur_move = 'left'

print(time)
    






