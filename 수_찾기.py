# 백준에서만 사용가능
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())
# add없이 한번에 감싸기 가능
A = set(map(int, input().split(' ')))
M = int(input())
B = list(map(int, input().split(' ')))
# 아래에 있는 배열을 순회하면서
for num in B:
    # 위에 있는 배열에 검색
    if num in A:
        # 있으면 1출력
        print(1)
    else:
        # 없으면 0출력
        print(0)
