# 백준에서만 사용가능
import sys
# 개행문자가 하나 붙는다
# .strip을 사용하면 해결 가능
input = sys.stdin.readline
from itertools import permutations

T = int(input())
for _ in range(T):
    k = int(input())

    # list compregension
    # words = [input().rstrip() for _ in range(k)]
    words = []
    for _ in range(k):
        # 오른쪽 공백을 삭제하는 rstrip()
        word = input().rstrip()
        words.append(word)
# 1. 이중 for 반복문)
    for i in range(k):
        for j in range(k):
            # 같은 걸 뽑았다면 넘어간다
            if i == k:
                continue

            # 둘을 이어 붙이고
            word = words[i] + words[j]
            # 회문 여부 검사
            # 회문이라면?
            if word == word[::-1]:
                print(word)

print(0)

# 2. permutations 패키지를 사용
# 순열 모듈을 이용해서 단어 2개를 뽑은 후
for w1, w2 in permutations(words, 2):
    # 둘을 이어 붙이고
    new_word = w1 + w2
    # 회문 여부를 검사
    if word == word[::-1]:                         
        # 출력 후 break
        print(word)
        break

# 찾지 못했다면?
# 비정상적으로(즉 break을 만나면)종료가 되면 else에 들어가지 않음
# 정상적으로 실행이 되면 else절으로 들어감
else:
    # 0 출력
    print(0)