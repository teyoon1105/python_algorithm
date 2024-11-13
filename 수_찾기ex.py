import sys
input = sys.stdin.readline

# 첫번째 input으로 리스트 A에 들어갈 데이터 갯 수
N = int(input())
# 두번째 input을 공백을 기준으로 나누고 A 리스트에 넣기
A = list(map(int, input().split()))
# 세번째 input으로 리스트 B에 들어갈 데이터 갯 수
M = int(input())
# 네번째 input을 공백을 기준으로 나누고 B 리스트에 넣기
B = list(map(int, input().split()))

# B의 리스트를 순회
for i in B:
    # B 데이터가 A 리스트 안에 있다면?
    if i in A:
        # 1 출력
        print(1)
    # B 데이터가 A 리스트 안에 없다면?
    else:
        # 0 출력
        print(0)