import sys
input = sys.stdin.readline

n,m = list(map(int, input().split()))
answer = []

def get_all(iter, comb):
  if iter==m:
    answer.append(comb)
    return

  for i in range(1, n+1):
    get_all(iter+1, comb+[i])

get_all(0, [])
for ans in answer:
  for a in ans:
    print(a, end=' ')
  print()

    