import sys
input = sys.stdin.readline

n = int(input())

road_len = list(map(int, input().split()))
price = list(map(int, input().split()))
#i에 대해 price[i]가 가야하는 거리는 road_len
"""
왼쪽부터 시작

시작점보다 더 싼 주유소를 찾을 때까지 거리를 계속 간다
더 싼 주유소를 찾았다면 지금까지 간 거리를 찾기 전의 주유소 가격으로 계산하고 주유소를 갈아탐 

이를 반복 --> greedy: 싼 주유소를 계속 고르는 과정

"""

len_went = road_len[0]
cur = price[0]
total_cost = 0
#마지막 price는 안 봐도 된다
for i in range(1,n-1): 
  tmp = cur
  cur = min(cur, price[i])
  if tmp != cur:
    #지금까지 간 거리는 전 주유소 가격으로
    total_cost += len_went * tmp
    #이제부터 갈 거리 초기화
    len_went = road_len[i]
  else:
    len_went += road_len[i]

#주유소가 안 바꼈다면 지금까지 간 거리 * 주유소 가격으로 cost 추가
total_cost += len_went*cur

print(total_cost)
    
  




  