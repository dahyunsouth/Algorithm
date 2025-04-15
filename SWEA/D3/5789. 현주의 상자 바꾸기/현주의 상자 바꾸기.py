T = int(input())

for tc in range(1, T+1):

    N, Q = map(int, input().split())

    boxes = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())

        for n in range(L-1, R):
            boxes[n] = i

    print(f'#{tc}', *boxes)