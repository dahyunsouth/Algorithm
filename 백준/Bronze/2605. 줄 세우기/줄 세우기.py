lst = []
n = int(input())
picked_num = list(map(int, input().split()))

for i in range(n):
    lst.insert(picked_num[i], i+1)

lst = lst[::-1]

print(*lst)