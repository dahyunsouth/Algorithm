# 남학생은 남학생끼리
# 여학생은 여학생끼리
# 한 방에는 같은 학년만
# 한 방에 한 명 ㄱㄴ

# K: 한 방에 배정할 수 있는 최대 인원 수
# [출력] 필요한 방의 최소 개수
# N: 수학여행에 참가하는 학생 수
# S: 학생의 성별
    # 0: 여 / 1: 남
# Y: 학년

N, K = map(int, input().split())
lst = [[0]*2 for _ in range(6)] # 성별(S) 2, 학년(Y) 6

for _ in range(N):
    S, Y = map(int, input().split())
    lst[Y-1][S] += 1

room_cnt = 0
for i in range(6):  # 학년(Y)
    for j in range(2):  # 성별(S)
        if lst[i][j] % K == 0:                  # K의 배수이면
            room_cnt += (lst[i][j] / K)
        else:                                   # K로 나누어떨어지지 않으면
            room_cnt += (lst[i][j]//K + 1)      # 그 학생을 위해 방 하나가 더 필요함

print(int(room_cnt))