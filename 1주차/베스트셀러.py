import sys
input = sys.stdin.readline


n = int(input())

# 구조화

# 빈 딕셔너리 제작
sales_info = {}
# 반복문을 돌며
for _ in range(n):
    # 책 제목을 ㅇ입력받고
    book_name = input()

# 1. 조건문을 통한 분기

    # 만약 딕셔너리에ㅔ 해당 제목이 없다면? => 생성
    if book_name not in sales_info:
        sales_info[book_name] = 1
    # 있다면> => 1 더해주기
    else:
        # sales_info[book_name] += 1
        sales_info[book_name] = sales_info[book_name] + 1

# 2. get 매서드 활용하기(없는 키값을 넣어도 에러가 발생 X)
    sales_info[book_name] = sales_info.get(book_name, 0) + 1

# 3. defaultdict 활용하기
# 외부에서 모듈 가져오기
from collections import defaultdict
sales_info = defaultdict(list)
# defaultdict = default값이 정해져 있는(values의 디폴트값(우리가 설정 가능)이 정해져 있다)

for _ in range(n):
    book_name = input()
    sales_info[book_name] = sales_info[book_name] + 1

# 4. Counter 모듈 활용
from collections import Counter
# Counter : 목적이 집계인 함수
# list comprehension, 지능형 리스트 : sales_info = [input() for _ in range(n)]
sales_info = []
for _ in range(n):
    book_name = input()
    sales_info.append(book_name)
sales_info = Counter(sales_info)

# 연산
# 1. 반복 갱신
max_sales_count = 0
max_sales_book = ""

# 딕셔너리를 반복하면 key값만 나옴
for x in sales_info:
    if sales_info[name] >= max_sales_count and max_sales_book > name:
        max_sales_book = name

# 2. 정렬
# key 값에는 정렬 기준이 들어옴
# lambda 값에는 앞 이터러블 데이터 덩어리들이 들어옴
# 1. 책 판매 횟수의 내림차순으로 : -x[1]
# 2. 책 제목의 오름차순으로 : x[0]
# 정렬 기준은 1번째는 x[1] 즉 팔린 책의 갯수
# 
sorted_sales_info = sorted(sales_info.items(), key=lambda x: (-x[1], x[0]))
print(sorted_sales_info[0][0])

# 조건1 : 가장 많이 팔린 책
# 조건2 : 제목이 사전순으로 가장 앞선 책
