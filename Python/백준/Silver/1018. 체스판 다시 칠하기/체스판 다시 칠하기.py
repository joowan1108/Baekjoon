import sys
input = sys.stdin.readline

n,m = map(int, input().split())

array = [input().strip() for _ in range(n)]

repainted = []
for pad_n in range(n-7):
    for pad_m in range(m-7):
        count_1=0
        count_2=0
        first_color = array[pad_n][pad_m]
        for i in range(pad_n, pad_n+8):
            for j in range(pad_m, pad_m+8):
                if((i+j)%2==0):
                    if(array[i][j]=='W'):
                        count_1+=1
                    else:
                        count_2+=1
                else:
                    if(array[i][j]!='W'):
                        count_1+=1
                    else:
                        count_2+=1
        repainted.append(count_1)
        repainted.append(count_2)
        
print(min(repainted))
                
            
        