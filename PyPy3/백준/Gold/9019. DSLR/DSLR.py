import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
moves = ['D', 'S', 'L', 'R']

for _ in range(T):
    start, end = map(int, input().split())
    visited = [False] * 10000

    def bfs(start):
        q = deque()
        q.append((start, ''))
        visited[start] = True
        
        while q:
            s, commands = q.popleft()
           
            if s == end:
                print(commands)
                break
            
            for move in moves:
                if move == 'D':
                    tmp = (2 * s) % 10000 
                elif move == 'S':
                    tmp = 9999 if s == 0 else s - 1 
                elif move == 'L':
                    num = s // 1000
                    tmp = (s % 1000) * 10 + num 
                else: 
                    num = s % 10
                    tmp = (s // 10) + 1000 * num 
                
                if not visited[tmp]:
                    visited[tmp] = True
                    q.append((tmp, commands + move))
           
    bfs(start)
