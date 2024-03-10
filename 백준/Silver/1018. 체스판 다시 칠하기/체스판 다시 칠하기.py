n, m = map(int, input().split())
board = []
coloring = []

for _ in range(n):
    board.append(input())
    
for x_start in range(n-7):
    for y_start in range(m-7):
        b_cnt = 0
        w_cnt = 0
        
        for i in range(x_start, x_start+8):
            for j in range(y_start, y_start+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else:
                    if board[i][j] != 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1
        
        coloring.append(b_cnt)
        coloring.append(w_cnt)
        
print(min(coloring))