# N * N
# 각 칸에 RGB 중 하나
# 구역
    # 같은 색
    # 상하좌우 인접

# [출력]
    # 적록색약인 사람이 봤을 때, 구역의 수
        # R / G / B
    # 적록색약이 아닌 사람이 봤을 때, 구역의 수
        # R, G / B

from collections import deque

def BFS(y, x):
    q.append((y, x))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<N and 0<=nx<N and MAP[ny][nx] == MAP[y][x] and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx))


N = int(input())
MAP = [list(input()) for _ in range(N)]
q = deque()

# 적록색약이 아닌 사람이 봤을 때, 구역의 수
visited = [[0] * N for _ in range(N)]
cnt_1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt_1 += 1

# 적록색약인 사람이 봤을 때, 구역의 수
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 'G':
            MAP[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt_2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i, j)
            cnt_2 += 1

print(cnt_1, cnt_2)