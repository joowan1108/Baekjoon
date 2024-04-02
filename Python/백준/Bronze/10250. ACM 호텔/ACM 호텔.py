import sys

input = sys.stdin.readline

T = int(input())

def get_hotel_room(guest, height, width):
    guest_height = guest % height #층 정보 #나머지
    guest_width = (guest // height)+1
    if(guest%height==0):
        guest_height=height
        guest_width-=1
    if(guest_width<10):
        guest_width = '0'+str(guest_width)
    else:
        guest_width = str(guest_width)
    return str(guest_height)+guest_width


for _ in range(T):
    height, width, n = map(int, input().split())
    result = get_hotel_room(n, height, width)
    
    print(int(result))


    
    
            
