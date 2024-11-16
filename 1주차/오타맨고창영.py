#  input으로 받는 첫 숫자 == 전체 텍스트 갯수 == for문으로 반복할 횟수
T = int(input())

# 오타를 지운 문자열을 저장할 리스트
text_list = []

# 
if T >=1 and T <= 1000:
    for _ in range(T):
        # 틀린 문자열 번호와 문자열을 분리
        text_len, text = input().split(' ')
        # 오타를 수정한 text 만들기
        new_text = text[:int(text_len)-1]+text[int(text_len):]
        # 리스트에 저장
        text_list.append(new_text)
    # 리스트를 불러와서 오타 수정한 text 출력하기
    for item in text_list:
        print(item)