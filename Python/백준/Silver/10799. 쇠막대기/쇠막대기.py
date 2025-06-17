import sys

input = sys.stdin.readline

parens = list(input().rstrip())

before = parens[0]

answer = 0
bar_cnt = 0

for i in range(1, len(parens)):
    if parens[i]==')' and before=='(':
        answer+=bar_cnt
    elif parens[i]==')' and before==')':
        bar_cnt-=1
        answer+=1
    elif parens[i]=='(' and before=='(':
        bar_cnt+=1



    before = parens[i]

print(answer)
