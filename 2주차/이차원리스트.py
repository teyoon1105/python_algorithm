matrix =[[3, 7, 9], 
         [4, 2, 6], 
         [8, 1, 5]]

# 순회
# 행기준
for r in range(3):
    for c in range(3):
        print(matrix[r][c])

# 열기준        
for c in range(3):
    for r in range(3):
        print(matrix[r][c])

# 전치
for r in range(3):
    for c in range(3):
        if c > r:
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c] 

print(matrix)

# zip 함수를 이용한 전치
# 리스트 안에 튜플이 있음
print(list(zip(*matrix)))


# 델타 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

matrix =[[3, 7, 9], 
         [4, 2, 6], 
         [8, 1, 5]]

r, c = 1, 1
# raw 한칸 위로 보기
matrix[r+dr[0]][c+dc[0]]

# 반복문을 이용해서 탐색
r, c = 1, 1
for d in range(4):
    nr, nc = r+dr[d], c+dc[d]
    # 유효한 좌표인지 확인
    if 0 <= nr < 3 and 0 <= nc < 3:
        print(matrix[nr][nc])
