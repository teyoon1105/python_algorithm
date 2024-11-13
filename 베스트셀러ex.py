import sys
input = sys.stdin.readline

# 입력으로 받는 반복문을 실행할 횟수
n = int(input())

# 반복문에서 저장할 딕셔너리 생성
book = dict()
max_title = []
# key값에 책 제목, values에는 갯수, 새로 나오면 새로운 key값과 values = 1 이렇게 출력
for _ in range(n):
    name = input()
    # 딕셔너리에 책 제목이 있다면?
    if name in book:
        # values 값 + 1
        book[name] = book.get(name) + 1
    # 딕셔너리에 책 제목이 없다면?
    else:
        book[name] = 1
        # key : value 쌍 생성, value = 1

# for 문을 통해 value가 가장 큰 값의 key들을 리스트에 넣고
for name, count in book.items():
    if count == max(book.values()):
        max_title.append(name)

# 해당 리스틀를 sort로 정렬해 가장 첫 값을 출력
sorted_list = sorted(max_title)
print(sorted_list[0])
