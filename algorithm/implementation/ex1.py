# 구현(Implementation)
# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
# 예시)
# 1. 알고리즘은 간단, 코드가 지나치게 길어지는 문제
# 2. 실수 연산을 다루고 특정 소수점 자리까지 출력해야 하는 문제
# 3. 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 4. 적절 한 라이브러리를 찾아서 사용해야 하는 문제

# 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬의 의미로 사용
# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 '방향벡터' 가 자주 사용
#         동  북  서 남
# ex) dx=[0, -1, 0, 1]
#     dy=[1, 0, -1, 0]

#이코테2021 (유투브 동빈나)
# 상하좌우

N = int(input())
map = list(input().split())

#초기위치
x=0
y=0
#     L  R   U  D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in map:
    if i == 'L':
        nx = x + dx[0]
        ny = y + dy[0]
    elif i == 'R':
        nx = x + dx[1]
        ny = y + dy[1]
    elif i == 'U':
        nx = x + dx[2]
        ny = y + dy[2]
    elif i == 'D':
        nx = x + dx[3]
        ny = y + dy[3]
    if (nx >= N or nx <0) or (ny >= N or ny <0) :
        continue
    x, y = nx, ny

print(x+1,y+1)
