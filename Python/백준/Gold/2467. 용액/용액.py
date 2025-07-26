import sys
input = sys.stdin.readline

n = int(input())
liqs = list(map(int, input().split()))

"""
+인 것과 -인 것 분리해서 각각 정렬 (-는 내림차순)
투 포인터로 구한다.
값이 음수면 + pointer를 증가 값이 양수면 - pointer를 증가

동일한 용액 종류에서 답이 나오는 경우 확인은 마지막에 한다
"""
compare = float('inf')
ans = (0,0)

positive = []
negative = []
for liq in liqs:
  if liq < 0:
    negative.append(liq)
  else:
    positive.append(liq)

pos, neg = 0,0
positive.sort()
negative.sort(reverse=True)

len_pos = len(positive)
len_neg = len(negative)

if len_pos>=1 and len_neg>=1:
  while pos < len_pos and neg < len_neg:
    test = positive[pos] + negative[neg]
    if abs(test) < compare:
      compare = abs(test)
      ans = (negative[neg], positive[pos])
      
    if test > 0:
      neg+=1
    else:
      pos+=1

#동일한 종류 조합 확인
positive_win = False
negative_win = False

#동일한 종류가 +,- 섞은 것보다 0에 가까운 경우
if len_pos >=2:
  test = positive[0] + positive[1]
  if abs(test) < compare:
    positive_win = True
    compare = abs(test)
    ans = (positive[0], positive[1])
    
if len_neg >=2:
  test = negative[0] + negative[1]
  if abs(test) < compare:
    positive_win = False
    negative_win = True
    ans = (negative[1], negative[0])

print(f"{ans[0]} {ans[1]}")

  




    
  




