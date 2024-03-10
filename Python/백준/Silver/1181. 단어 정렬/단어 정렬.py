import sys
N = int(sys.stdin.readline().rstrip())
stringset = set()
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    stringset.add(s)
result = sorted(sorted(stringset), key=len)
for s in result:
    print(s)