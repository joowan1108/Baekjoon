import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    total = 1
    n = int(input())
    clothes = defaultdict(list)
    
    for _ in range(n):
        clothe, category = map(str, input().rstrip().split())
        clothes[category].append(clothe)
    
    for category in clothes:
        total *= (len(clothes[category]) + 1)
    
    total -= 1 
    print(total)
