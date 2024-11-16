import sys
input = sys.stdin.readline

N, K = map(int, input().split())

input_list = list(map(int, input().split()))

tmp = max_sum = sum(input_list[:2]) 

for i in range(N-K):
    tmp += input_list[i+K] - input_list[i]
    max_sum = max(max_sum, tmp)

print(max_sum)
