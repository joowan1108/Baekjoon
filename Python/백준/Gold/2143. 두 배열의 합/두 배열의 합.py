import sys
import bisect
input = sys.stdin.readline

target = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

prefix_a = [0]
for i in range(n):
  prefix_a.append(prefix_a[-1] + a[i])

prefix_b = [0]
for i in range(m):
  prefix_b.append(prefix_b[-1] + b[i])

all_segment_sums_a = []
for i in range(n):
  for j in range(i+1,n+1):    
    all_segment_sums_a.append(prefix_a[j] - prefix_a[i])

all_segment_sums_b = []
for i in range(m):
  for j in range(i+1,m+1):    
    all_segment_sums_b.append(prefix_b[j] - prefix_b[i])

"""
모든 가능한 구간 합들을 각 배열마다 구했음

정렬해서 한 쪽에 target를 다 빼고 0보다 큰 애들만 건져내서 그 애들이 다른쪽에 존재하는지 이분탐색으로 탐색
"""
possibles = [target-num for num in all_segment_sums_a]
all_segment_sums_b.sort()
ans = 0

for pos in possibles:
  left = bisect.bisect_left(all_segment_sums_b, pos)
  right = bisect.bisect_right(all_segment_sums_b, pos)
  ans += right-left

print(ans)
  




    

    
