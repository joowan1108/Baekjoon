cnt = 0
    
def backtrack(n, chess, row, diag1, diag2, line):
    global cnt
    if row==n:
        cnt+=1
        return
    
    for i in range(n):
        if (row+i) in diag1 or (row-i) in diag2 or i in line:
            continue
        line.add(i)
        diag1.add(row+i)
        diag2.add(row-i)
        chess[row][i]=1
        backtrack(n, chess, row+1, diag1, diag2, line)
        chess[row][i]=0
        line.remove(i)
        diag1.remove(row+i)
        diag2.remove(row-i)
    
        
    
    
def solution(n):
    chess = [[0]*n for _ in range(n)]
    diag1 = set()
    diag2 = set()
    line = set()
    backtrack(n, chess, 0, diag1, diag2, line)
    return cnt
        