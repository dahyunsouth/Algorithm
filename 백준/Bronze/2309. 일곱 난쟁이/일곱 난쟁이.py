heights = []
for _ in range(9):
    height = int(input())
    heights.append(height)

from itertools import combinations

heights = combinations(heights, 7)
heights = list(heights)

lst = []

for comb in heights:
    if sum(comb) == 100:
        for elem in comb:
            lst.append(elem)
        break

lst.sort()
for elem in lst:
    print(elem)