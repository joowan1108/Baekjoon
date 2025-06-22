import sys
input = sys.stdin.readline
string = input().rstrip()
bomb = input().rstrip()

bomb_len = len(bomb)

res = []
n=0
for s in string: 
    res.append(s)
    n+=1
    if n >= bomb_len:
        if ''.join(res[-bomb_len:]) == bomb:
            for _ in range(bomb_len):
                n-=1
                res.pop()

result = ''.join(res)
if result:
    print(result)
else:
    print("FRULA")
    



    

