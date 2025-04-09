N = int(input())    # 수의 개수

nums = []   # 입력받은 수들을 저장할 list

for _ in range(N):
    i = int(input())
    nums.append(i)

# 1. 중복 제거
set(nums)

# 2. 오름차순 정렬
nums.sort()

for num in nums:
    print(num)