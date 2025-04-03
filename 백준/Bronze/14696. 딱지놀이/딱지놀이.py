N = int(input())

for _ in range(N):
    a = list(map(int, input().split()))
    a2 = a[1:]
    a2.sort()

    cnt_a_lst = []

    cnt_a_4 = a2.count(4)
    cnt_a_lst.append((4, cnt_a_4))

    cnt_a_3 = a2.count(3)
    cnt_a_lst.append((3, cnt_a_3))

    cnt_a_2 = a2.count(2)
    cnt_a_lst.append((2, cnt_a_2))

    cnt_a_1 = a2.count(1)
    cnt_a_lst.append((1, cnt_a_1))

    b = list(map(int, input().split()))
    b2 = b[1:]
    b2.sort()

    cnt_b_lst = []

    cnt_b_4 = b2.count(4)
    cnt_b_lst.append((4, cnt_b_4))

    cnt_b_3 = b2.count(3)
    cnt_b_lst.append((3, cnt_b_3))

    cnt_b_2 = b2.count(2)
    cnt_b_lst.append((2, cnt_b_2))

    cnt_b_1 = b2.count(1)
    cnt_b_lst.append((1, cnt_b_1))



    for x in range(4):
        if cnt_a_lst[x][1] > cnt_b_lst[x][1]:
            print('A')
            break
        elif cnt_a_lst[x][1] < cnt_b_lst[x][1]:
            print('B')
            break
    else:
        print('D')