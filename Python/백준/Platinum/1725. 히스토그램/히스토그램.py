import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = 0
for _ in range(n):
  i = int(input())
  if not stack:
    stack.append([i, 1])
    continue

  if stack[-1][0] < i:
    stack.append([i, 1])
    continue

  elif stack[-1][0] == i:
    stack[-1][1] += 1
    continue

  else:
    while stack:
      num, freqs = stack.pop()
      ans = max(ans, num * freqs)

      if not stack:
        stack.append([i, freqs + 1])
        break

      if stack[-1][0] > i:
        stack[-1][1] += freqs
      elif stack[-1][0] == i:
        stack[-1][1] += freqs + 1
        break
      else:
        stack.append([i, freqs + 1])
        break

while stack:
  num, freqs = stack.pop()
  ans = max(ans, num * freqs)

  if stack:
    stack[-1][1] += freqs

print(ans)
