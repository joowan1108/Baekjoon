import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

trash = []
cards = deque([i for i in range(1,n+1)])

length = n
while length>1:
    trash.append(cards.popleft())
    length-=1
    if length==1:
        break
    cards.append(cards.popleft())

for t in trash:
    print(t, end=' ')

print(cards[-1])
