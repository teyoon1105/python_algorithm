# 1. 함수
    # 로직을 담아서 반복 사용 
    # 함수 내부(local), 바깥(global)

# 2. LEGB 규칙
# local 영역에서 global영역 변수를 재할당 할 수 없다
# 참조는 가능하다
# 재할당 하고 싶을 때에는 global 처리
# 변수형이 리스트라면 append로 재할당 없이 값을 추가 가능
# append(매서드)(재할당 아님)
# 참고할 때 우선순위 : Local Enclosed Global Built-in

# 3. 재귀함수
# 함수 자신으로써 정의가 되는 함수
# 똑같은 로직이 계속 반복
# while 반복문 처럼 사용 가능
# 종료조건을 잘 사용해야 함(재귀 error 발생 가능)
# 보통함수 정의 아래에 재귀 조건을 작성

# 로직이 1개 일 때 예시코드
nums = [-5, 2, 7, -3, 2, 10, 8, 6, 5, -1]
max_num = -float("INF")

def my_func(idx):
    global max_num
    # 재귀 종료 조건
    if idx == len(nums):
        print(max_num)
        return
    # 탐색(반복) 로직
    
    if max_num < nums[idx]:
        max_num = nums[idx]
    
    # 또는
    # max_num = max(nums[idx], max_num)

    my_func(idx+1)

my_func(0)

# 로직이 2개면
# 1번 로직만 재귀함수가 반복되면 반복되다가 종료조건이 되어 종료가 되면
# 바로 그 전 함수의 2번 로직이 반복된다
# 이렇게 순서대로 대기하면 쌓여있다가 본인 차례 때 실행되는걸
# 시스템 스택이라고 한다

def find(depth):
    # 종료조건
    if depth == 10:
        print("찾았당")
        return
    
    # 로직 1
    print(f'탐색하는 중, 깊이는 {depth}')
    find(depth+1)

    # 로직 2번
    print(f'올라가는 중, 깊이는 {depth}')

find(0)