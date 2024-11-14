T = int(input())

def bin_search(l, r, target, count):
    # 1페이지와 가장 마지막 페이지를 더해서 2로 나눠 C값을 구하고
    c = int((l+r)/2)

    # C값과 target값을 비교
    # 3가지 경우의 수
    # 1. target > C
    if target > c:
    # - 400페이지와 C값을 더하고(즉 L값 C로 갱신) 2로 나눠서 C값을 다시 만들기
        return bin_search(c, r, target, count+1)
    # 2. target < C
    elif target < c:
    # - 1페이지와 C값을 더하고(즉 R값 C로 갱신) 2로 나눠서 C값을 다시 만들기
        return bin_search(l, c, target, count+1)
    # 3. target == C
    else:
        return count
    # - 탐색 횟수 depth를 구하고 A, B의 값 중 더 작은 값에 해당하는 아이 출력

for tc in range(T):
    p, pa, pb = map(int, input().split())
    a_count = bin_search(1, p, pa)
    b_count = bin_search(1, p, pb)
    if a_count > b_count:
        print('B')
    elif a_count < b_count:
        print('A')
    else:
        print('무승부')


# while 반복문으로 실행
def binary_search(l, r, target, count):
    while True:
        c = int((l+r)/2)

        if c == target:
            return count
        
        elif c > target:
            r = c
            
        else:
            l = c
        
        count += 1

