def get_score(info, lion):
    apeach_score, lion_score = 0, 0
    for i in range(11):
        if info[i] == lion[i] == 0:
            continue
        elif info[i] >= lion[i]:
            apeach_score += (10 - i)
        else:
            lion_score += (10 - i)
    return apeach_score, lion_score

lions = []

def backtrack(n, info, lion, i):
    global lions
    if i == len(info):
        lion_copy = lion[:]
        lion_copy[-1] += n 
        lions.append(lion_copy)
        return
    if n > info[i]:
        lion[i] = info[i] + 1
        backtrack(n - lion[i], info, lion, i + 1)
        lion[i] = 0 
        
    backtrack(n, info, lion, i + 1)

def solution(n, info):
    global lions
    lions = []
    lion = [0] * 11
    backtrack(n, info, lion, 0)
    max_diff = 0
    answer = [-1]

    for l in lions:
        apeach_score, lion_score = get_score(info, l)
        if lion_score > apeach_score:
            diff = lion_score - apeach_score
            if diff > max_diff:
                max_diff = diff
                answer = l
            elif diff == max_diff:
                for i in range(10, -1, -1):
                    if l[i] > answer[i]:
                        answer = l
                        break
                    elif l[i] < answer[i]:
                        break

    return answer
