import sys
input = sys.stdin.readline

string = input().rstrip()

word = []
result = []
in_paran = False


for s in string:
    if s=='>':
        result.append(s)
        in_paran = False

    elif s=='<':
        if word:
            for _ in range(len(word)):
                result.append(word.pop())
        result.append(s)
        in_paran = True

    elif in_paran==True:
        result.append(s)

    elif not in_paran and (s.isalpha() or s.isdigit()):
        word.append(s)

    #<>안이 아닌 빈칸일 때
    else:
        if word:
            for _ in range(len(word)):
                result.append(word.pop())
        result.append(' ')

if word:
    for _ in range(len(word)):
        result.append(word.pop())

for r in result:
    print(r, end='')

    