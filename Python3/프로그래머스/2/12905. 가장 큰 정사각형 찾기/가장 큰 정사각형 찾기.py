def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            left, diag, up = board[i-1][j], board[i-1][j-1], board[i][j-1]
            if board[i][j]==1:
                board[i][j] = min([left, diag, up]) + 1
    return max([max(row) for row in board])**2