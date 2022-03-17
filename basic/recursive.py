# 재귀 함수
# 자기 자신을 다시 호출하는 함수
# 문제에서 재귀를 사용하려면 반드시 종료조건을 넣어줘야함!
# 차례대로 호출되었다가 가장 나중에 호출된 메서드부터 리턴 -> 스택형식

#팩토리얼 구현

#재귀X
def factorial_interative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#재귀O
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복으로 구현 : ', factorial_interative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))

# ===========================================================

# 최대공약수 계산(유클리드 호제법)
# 두 자연수 A, B (A>B)에 대해 A를B로 나눈 나머지를 R이라고 할 때
# A와 B의 최대공약수는  B와 R의 최대공약수와 같다

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192, 162))