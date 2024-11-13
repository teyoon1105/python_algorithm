import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
# 누적합 리스트 만들기
acc = [0]
for num in nums:
    acc.append(acc[-1] + num)

# acc = [0] + accumulate(nums)

for _ in range(N):
    i, j = map(int, input().split())
    acc[j+1] - acc[i]
