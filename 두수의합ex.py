# 백준에서만 사용가능
import sys
input = sys.stdin.readline

# 입력으로 받는 수열의 길이와, 원하는 결과값
N, M = map(int, input().split())
# 좌측 포인터 i
# 우측 포인터 j
i = j = 0

tmp = num_sum = 0

num = list(map(int, input().split()))

while True:
    # 포인터 두 사이 수열들의 합(tmp)이 결과값 M 보다 작으면
    if tmp < M:
        # 근데 오른쪽 포인터가 더 이상 올릴 수 없으면
        if j >= N:
            # 종료
            break
        
        # 그게 아니라면 
        # tmp 값에 오른쪽 포인터가 현재 가르키는 값을 더해줌
        tmp += num[j]
        # 오른쪽 포인터 j를 하나 올림
        j += 1    
        

    # 포인터 두 사이 수열드의 합(tmp)이 결과값 M 보다 크면
    elif tmp > M:
        # tmp 값에 왼쪽 포인터가 가르키던 값을 빼고
        tmp -= num[i]
        # 왼쪽 포인터를 오른쪽으로 하나 올린다
        i += 1

    # 포인터 두 사이 수열들의 합(tmp)이 결과값 M과 같으면
    else: # tmp == M
        # num_sum 값에 +1 해주고    
        num_sum += 1
        # tmp 값에서 왼쪽 포인터가 가르키던 값을 빼고
        tmp -= num[i]
        # 왼쪽 포인터를 하나 올려줌(오른쪽은 리스트 인덱싱 오류 발생 가능)
        i += 1

print(num_sum)