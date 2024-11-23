import sys
import heapq

input = sys.stdin.readline
n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]

def dijkstra():
    # 최소 비용을 저장하는 우선순위 큐
    pq = []
    
    # 시작 상태: 첫 번째 집에서 각 색을 선택
    for color in range(3):
        heapq.heappush(pq, (houses[0][color], 0, color))  # (비용, 집 번호, 색상)
    
    # 최소 비용 초기화
    min_cost = [[float('inf')] * 3 for _ in range(n)]
    for color in range(3):
        min_cost[0][color] = houses[0][color]
    
    while pq:
        cost, house, color = heapq.heappop(pq)
        
        # 마지막 집에 도달한 경우
        if house == n - 1:
            return cost
        
        # 현재 집에서 다음 집으로 이동
        for next_color in range(3):
            if color != next_color:  # 같은 색상은 연속할 수 없음
                next_cost = cost + houses[house + 1][next_color]
                if next_cost < min_cost[house + 1][next_color]:
                    min_cost[house + 1][next_color] = next_cost
                    heapq.heappush(pq, (next_cost, house + 1, next_color))

# 최솟값 출력
print(dijkstra())
