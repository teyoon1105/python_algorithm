dwarfs = [int(input()) for _ in range(9)]

# 2중 for 문을 활용
# 시간 복잡도는 최고차항을 따르기 때문에
# for문의 인덱스를 조절해도 시간 복잡도는 O(N^2)

# 정답을 찾으면 flag를 통해 2중 for문을 종료
flag = False
for i in range(9):
    for j in range(i+1, 9):
        # 만약 i 번째 난쟁이 키와 j 번째 난쟁이 키를 전체 합에서 빼서 100이 된다면
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
        # 첩자는 i와 j, i,j를 보관(바로 i를 pop을 해버리면 j 값이 변함)
            spy = [i, j]
        # 2중 for문을 종료 break
            flag = True
            break
    # 1차 for문 종료 후 이 조건문으로 들어오게 만들어서
    # 2차 for문도 종료시킴
    if flag:
        break

# 하나 씩 출력하는데 (i번째와 j 번째는 출력 X)
for idx in range(9):
    if idx in spy:
        continue

    print(dwarfs[idx])

# 조합을 모듈로써 찾는 패키지 존재
from itertools import combinations
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

for combi in combinations(dwarfs, 7):
    if sum(combi) == 100:
        for dwarf in combi:
            print(dwarf)
        break

