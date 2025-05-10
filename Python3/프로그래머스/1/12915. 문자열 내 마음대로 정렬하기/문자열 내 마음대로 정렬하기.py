def solution(strings, n):
    for i in range(len(strings)):
        if n==0:
            continue
        else:
            strings[i] = strings[i][n]+strings[i][:n] + strings[i][n+1:]
    strings.sort()
    
    for i in range(len(strings)):
        if n==0:
            continue
        else:
            strings[i] = strings[i][1:n+1] + strings[i][0] + strings[i][n+1:]
    
    return strings
    
        