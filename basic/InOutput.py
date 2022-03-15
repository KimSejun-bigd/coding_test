import sys

n = int(input())

#입력 받는 부분 이런식으로
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

#입력 변수가 적을 때는 이런 식으로도 가능
a, b, c = map(int, input().split())
print(a,b,c)

# 빠르게 입력 받기
# sys 라이브러리 안에 sys.stdin.readline() 메서드 이용
# 단, 입력후 엔터(Enter)가 줄 바꿈으로 입려되므로 rstrip() 메서드 함께 사용
# 이진탐색, 정렬 등에서 자주 쓰임 - 입력받아야 할 값이 많은 경우

data = sys.stdin.readline().rstrip()
print(data)
