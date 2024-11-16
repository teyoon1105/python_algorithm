import sys
input = sys.stdin.readline

# 반복문으로 접근할 총 입력의 갯수
n = int(input())

output_list = []

# for 반복문을 사용해서 입력을 받은 횟수만큼 반복한다
for _ in range(n):
    # score를 저장할 리스트
    score_list = []

    # 정답을 입력받는다
    answer = input()
    # 출력할 점수, 처음은 0으로 초기화를 한다
    score = 0
    # 입력받은 정답은 문자열, 문자열의 길이만큼 for 반복문을 반복하여 각 정답값에 접근한다
    for i in range(len(answer)):
        # 처음 정답이 O라면 score에 1 증가
        if i == 0:
            if answer[i] == 'O':
                score += 1
                score_list.append(score)
        # 처음 정답 이후
        else:
            # 정답이 나온다면
            if answer[i] == 'O':
                score += 1
                score_list.append(score)

            # 정답이 아니면 pass
            else:
                score = 0

    output_list.append(sum(score_list))

for output in output_list:
    print(output)

            