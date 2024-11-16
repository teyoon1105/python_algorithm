n = int(input())

# fibo(n) = fibo(n-1) + fibo(n-2) (단 n >= 2)

# 갱신해줄 fibo_n 값

def fibo(N):

    # 종료 조건
    if N <= 1:
        return N
    
    # 탐색 로직
    return fibo(N-1) + fibo(N-2)

fibo(n)

n = int(input())
# 각 항의 값들을 append 해 줄 리스트
# 중복되는 계산을 하지 않고 여기서 뽑아 사용해 시간 복잡도를 낮춰준다
memo = [0, 1]

for _ in range(n-1):
    memo.append(memo[-1] + memo[-2])

print(memo[n])