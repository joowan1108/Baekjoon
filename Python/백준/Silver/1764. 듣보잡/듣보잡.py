import sys
input = sys.stdin.readline

n,m = map(int, input().split())
first = set([input().strip() for _ in range(n)])
second = set([input().strip() for _ in range(m)])

tmp = list(first&second)
tmp.sort()
print(len(tmp))
for name in tmp:
    print(name)