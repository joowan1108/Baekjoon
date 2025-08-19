import sys
import math
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n, m = map(int, input().strip().split())
    print(math.comb(m, n))
















