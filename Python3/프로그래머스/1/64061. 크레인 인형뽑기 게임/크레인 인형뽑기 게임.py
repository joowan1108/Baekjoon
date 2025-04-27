def solution(board, moves):
    container = []
    new_board = []
    ans = 0
    handle = -1
    #move의 번호가 그 column이도록 만들기
    for j in range(len(board[0])):
        tmp = []
        for k in range(len(board)):
            tmp.append(board[k][j])
        new_board.append(tmp)
    
    #0 다 없애기
    for i in range(len(new_board)):
        for j in range(len(new_board[0])):
            new_board[j] = [b for b in new_board[j] if b!=0]
    
    for b in new_board:
        print(b)
    
    moves = [m-1 for m in moves]
    for move in moves:
        if new_board[move]:
            handle = new_board[move].pop(0)
            if container:
                if container[-1]==handle:
                    container.pop()
                    ans += 2
                else:
                    container.append(handle)
            else:
                container.append(handle)
            handle=-1
    return ans
    
    
            