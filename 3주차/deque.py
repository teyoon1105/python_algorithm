# 스택 : 가장 마지막에 들어온 애가 나간다
# 큐 : 들어온 순으로 나간다

from collections import deque
# deque : 양방향 연결 리스트
# 이터러블 데이터를 인자로 받는다

queue = deque([1,2,3])

print(queue)
# 오른쪽으로 데이터 입력 append
# 왼쪽으로 데이터 삭제 popleft

queue.append(5)
print(queue) # [1,2,3,5]

num = queue.popleft()
print(num, queue) # 1과 [2,3,5]