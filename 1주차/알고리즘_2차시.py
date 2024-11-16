gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

# 1. gems 리스트에 1이 존재하는지?
# for문을 통해 gems 리스트 안의 데이터들을 하나씩 불러옴
# 반복문을 이용해서 리스트를 순회하며
# 1 이라는 데이터가 발견되었으면 >> 찾았음을 표시하고 종료
#      
# 내가 쓴 코드
for i in gems:
    # i값이 1이면 True
    if i == 1:
        print(True)
    # 1이 아니면 False
    else:
        print(False)

# 강사님이 쓰신 1번 코드
for gem in gems:
    if gem == 1:
        print('찾았다!')
        break

# 강사님이 쓰신 2번 코드
# idx를 사용했기 때문에 해당 리스트 데이터를 수정, 접근이 용이함
# range(a,b) >> b-a 만큼의 연속된 수를 사용할 예정
for idx in range(0, 10):
    if gems[idx] == 1:
        print('찾았다')
        break

# 2. 리스트에서 가장 큰 수를 찾는 문제

# 내가 작성한 코드

# 처음 수를 가장 큰 수로 설정
# 반복문을 통해 리스트는 순회하면서
# 가장 큰 수로 설정한 값과 비교하면서 가장 큰 수를 수정해나가자

lst = [56, 23, 43, 87, 12, 457, 86]

now_max = 0

for num in lst:
    if now_max < num:
        now_max = num
    elif now_max > num:
        now_max = now_max
    else:
        pass
print(now_max)

# 강사님이 작성하신 코드
lst = [56, 23, 43, 87, 12, 457, 86]
# 갱신을 위한 값
# 아주 아주 작은 값
# -float("INF")
ans = -float("INF")
# 또는
ans = lst[0] # 어차피 최대값의 후보군 중 하나니까
# 초기값을 세팅
# 순회하면 얻은 리스트 변수가 초기값보다 크면 초기값을 리스트 변수로 갱신
# 반복

# 리스트를 선형 탐색
for num in lst:
    # 리스트 값이 후보군보다 크면
    if num > ans:
        # 갱신하기
        ans = num

print(ans)

# 3. 집계 알고리즘
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1] 
# 딕셔너리를 이용한 집계
grades = {1: 0, 2: 0, 3: 0}
# 딕셔너리에 1, 2, 3 키값을 만든다
# 각 키값의 벨류는 0으로 채운다

for gem in gems:
    # 딕셔너리는 순서가 없다 > 키값으로 접근
    grades[gem].values += 1

# 리스트를 이용한 집계
# 빈 판 만들기
grade = [0] * 4

# 반복문을 이용해서 선형 탐색
for gem in gems:
    grades[gem] += 1

print(grades)

# 해시 자료구조와 딕셔너리
# 특징 정리
    # 1. 순서가 없다
    # 2. 중복을 허용하지 않는다
    # 3. 검색이 매우 빠르다

# 딕셔너라
    # 자료를 쌍으로 저장할 때

# 집합
    # 그 외 검색이 잦을 때
    # 단순히 중복 제거할 때 등등

my_dict = {'name':'ken', 'age':20,'licence':True}

# get 매서드
# 대괄호로 없는 키값을 지정하면 오류
# get 매서드는 오류는 아니고 none값으로 반환
print(my_dict['name'])
print(my_dict.get('name'))
# my_dict.get('name', 0)
# ,를 통해 없는 키값일 때 none값이 아닌 다른 값으로 표현이 가능함

# keys, values, items
# keys값만 가져옴
print(my_dict.keys())
# values값만 가져옴
print(my_dict.values())
# keys, values쌍을 가져옴
print(my_dict.items())

# 집합
my_set = set()

# 원소삽입
# add 매서드
my_set.add(5)
print(my_set)

# 원소 삭제
# discard
# remove
# 없는 원소를 삭제하려하면
# discard의 경우 그냥 넘어감
# remove의 경우 에러가 발생
my_set.discard(5)
print(my_set)
my_set.discard(1)
my_set.remove(1)
