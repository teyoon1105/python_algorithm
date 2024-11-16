import sys
from itertools import permutations
input = sys.stdin.readline

# 첫번째 입력 : 총 케이스의 수 T
T = int(input())

output = []

# T번 반복하는 for문
for _ in range(T):

    # 한번 반복할 때 마다 주어지는 문자열 갯수
    k = int(input())

    # 저장한 리스트
    words = []
    # 문자열의 갯수만큼 반복해서 문자열을 받아와서 리스트로 저장
    for _ in range(k):
        word = input().rstrip()
        words.append(word)

    # 저장된 리스트에서 itertools permutations 모듈을 사용해
    
    # 해당 리스트를 for 반복문을 통해 2개씩 문자를 받아와
    for w1, w2 in permutations(words, 2):
        # 두 문자열의 덧셈 연산
        new_w = w1 + w2
        # reverse문을 통해 회문인지 아닌지 확인
        reverse_w = new_w[::-1]
        if new_w == reverse_w:
            output.append(new_w)
            break
    
    else:
        output.append(0)

for result in output:
    print(result)



