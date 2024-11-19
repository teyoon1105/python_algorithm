T = int(input())
# 델타 셋팅
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())

    # 비어있는 N x N 2차원 리스트를 만든다
    snail = [[0]*N for _ in range(N)]

    # 0, 0 시작점으로 오른쪽으로 이동
    r, c = 0, 0
    # 방향
    # 우 > 하 > 좌 > 상 > 우 > 하 > ...
    # + 1씩 하다가 4부턴 0으로 reset
    d = 0


    # 1~N^2까지 반복하며 
    for i in range(1,N**2+1):
        # r, c에 현재 값 입력
        snail[r][c] = i
        # 새로운 좌표 찍기(nr, nc)
        nr, nc = r+dr[d], c+dc[d]

        # 좌표 유효성
        # 1. index
        # 2. 좌표점에 0이 아닌 값이 있다면
        # 조건1 and 조건2 and 조건3 중 조건 3까지 넘어왔다는 것은 조건1, 조건2가 이미 True로 되었다는 뜻
        # 즉 아래 조건에서 인덱스 오류가 발생하지 않는다
        if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
            # 유효 O > nr, nc를 지금 좌표로 이동
            r, c = nr, nc
        else:
            # 유효 X > 방향이동
            d = (d+1)%4
            nr, nc = r+dr[d], c+dc[d]
            r,c = nr, nc

print(f'#{tc}')
for line in snail:
    print(*line)