T = int(input())

# 테스트 케이스 만큼 반복
for tc in range(T):
    N = int(input())
    # 1. 공백을 기준으로 split
    # 2. int를 사용해 명시적 형변환
    # 3. 리스트로 감싸준다
    # map(f, iterable)
    # 각 덩어리에 함수를 적용시켜줌
    nums = list(map(int, input().split()))
    # 초기값
    now_max = -float("INF")
    now_min = float("INF")
    for num in nums:
        if now_max < num:
            now_max = num
        if now_min > num:
            now_min = num
    
    ans = (now_max - now_min)

    print("#{} {}".format(tc,ans))