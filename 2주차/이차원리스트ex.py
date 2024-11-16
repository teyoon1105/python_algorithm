# 파리잡기

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    files = [list(map(int, input().split())) for _ in range(N)]

    # 정답 초기화(0)
    ans = 0
    # 2중 for 문으로 files를 순회하며
    for r in range(N-M+1):
        for c in range(N-M+1):
        # r, c를 기준으로 잡아(tmp = 0)
            tmp = 0
            # 2중 for 문으로 MxM만큼 순회하며
            for i in range(r, r+M):
                for j in range(c, c+M):
                    tmp += files[i][j]
                # 파리 개수 세어주기

            # 정답 갱신
            ans = max(ans, tmp)

    # 정답 출력 
    print(f'#{tc} {ans}')

# 풍선팡
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split()) for _ in range(N))]

    # 2차원 리스트를 순회하면서
        # tmp = 0
        # r, c에서 델타탐색(4방향)

        # ans 갱신

    # ans 출력