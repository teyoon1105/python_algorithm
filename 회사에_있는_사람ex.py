import sys
input = sys.stdin.readline

# 총 몇 명의 사람인지 input으로 체크
n = int(input())

# 데이터 셋 제작(해시, 집합 사용)
company = set()
# n번에 걸쳐서 로그가 입력
for _ in range(n):
    # 입력을 받은 후
    name, status = input().split()
    # 상태가 enter라면? => 데이터 셋에 추가
    if status == 'enter':
        company.add(name)
    # 상태가 leave라면? => 데이터 셋에서 삭제
    elif status == 'leave':
        # remove는 오류가 날 수도 있음
        company.discard(name)

# 데이터 셋을 역순으로 정렬 
sorted_company = sorted(company, reverse=True)
# sort 매서드 vs sorted 함수
# sort 매서드 : 원본 리스트 변경
# sorted 함수 : 원본 리스트 그대로, 새로운 객체 생성, 이터러블 데이터에 사용되는데 반환값은 리스트

# 하나 씩 출력
for name in sorted_company:
    print(name)
