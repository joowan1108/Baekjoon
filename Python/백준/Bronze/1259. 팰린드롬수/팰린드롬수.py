import sys
input = sys.stdin.readline

while True:
    palin=1
    temp = input().strip()
    if(temp=='0'):
        break
    elif(len(temp)==1):
        print("yes")
    elif(len(temp)==2):
        if(temp[0]==temp[1]):
            print("yes")
        else:
            print("no")
    else:
        mid = len(temp)//2
        for i in range(mid):
            k=len(temp)-1-i
            if(temp[i]!=temp[k]):
                palin=0
        if(palin==1):
            print("yes")
        else:
            print("no")