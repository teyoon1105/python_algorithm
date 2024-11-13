import sys
input = sys.stdin.readline

# 총 몇개의 출퇴근 기록이 있는지 확인
n = int(input())
# 빈 집합을 만들고 해당 집합에 
ATT = set()

# split 값이 enter면 넣고, 없으면 빼기
for _ in range(n):
    name, stat = input().split()
    if stat == 'enter':
        ATT.add(name)
    elif stat == 'leave':
        ATT.discard(name)

# 사전 영문명 내림차순으로 정렬
sorted_ATT = sorted(ATT, reverse=True)

for name in sorted_ATT:
    print(name)

