nums = [3, 5, 1, 4, 2]

max_num = -float('INF')

for idx in range(3):                # N-M+1번 반복
    tmp = sum(nums[idx:idx+3])      # 슬라이싱을 통한 구간합 계산
    max_num = max(max_num, tmp)     # 갱신

print(max_num)

# 3,5,1의 합
# 5,1,4의 합
# 1,4,2의 합
# 이렇게 중복이 되는 합 부분이 있음

nums = [3, 5, 1, 4, 2]

tmp = max_num = sum(nums[:3])       # 첫 번째 구간합 구하기

for idx in range(2):                # 첫 번째는 이미 구했으므로
    tmp += nums[idx+3] - nums[idx]  # 새로운 구간합은 양 옆에서 빼고 더해주면 된다(슬라이딩 윈도우)
    max_num = max(max_num, tmp)     # 갱신

print(max_num)
# 첫 부분 합만 구하고
# 그 다음 부턴, 추가되는 부분만 더하고, 빠지는 건 빼고ß