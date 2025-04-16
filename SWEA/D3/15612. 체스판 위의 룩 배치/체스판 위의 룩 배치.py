T = int(input())
for tc in range(1, T+1):
    board = [list(input()) for _ in range(8)]
    cnt = 0     # 룩의 개수
    cnt_visited_i = [0] * 8
    cnt_visited_j = [0] * 8

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                cnt += 1
                cnt_visited_i[i] += 1
                cnt_visited_j[j] += 1

    if cnt == 8 and all(x == 1 for x in cnt_visited_i) and all(x == 1 for x in cnt_visited_j):
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')
