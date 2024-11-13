# 난쟁이 키를 입력받을 빈 리스트를 만들기
dwarfs = []

# 9번의 for문을 통해 리스트에 난쟁이 키 값 받기
for _ in range(9):
    dwarfs.append(int(input()))

dwarfs.sort()

# 2명의 키를 뺀 값이 100이 되는 2 난쟁이를 2중 for문으로 찾기
for i in range(8):
    for j in range(i+1,9):
        if sum(dwarfs)-dwarfs[i]-dwarfs[j] == 100:
            # 찾은 i번째, j번째 난쟁이들을 리스트에 담기
            spy = [i, j]
# 해당 리스트에 들어가 있으면 다음
for idx in range(9):
    if idx in spy:
        continue

    print(dwarfs[idx])