# 실전에서 유용한 표준 라이브러리

# 내장함수(sum(), min(), max(), eval(), sorted() 등..)
# itertools - 반복되는 형태의 데이터 처리에 유용(순열, 조합 자주사용)
# heapq - 힙(heap) 자료구조 제공(우선순위 큐 기능 구현하기 위해)
# bisect - 이진탐색(Binary Search) 기능 제공
# collections - 덱(deque), 카운터(Counter) 등의 자료구조 포함
# math - 필수적 수학적 기능 제공(팩토리얼, 제곱근, 최대공약수[GCD], 삼각함수 관련, 파이)

# *****************
# **** 내장함수 ****
# *****************

# sum() - 리스트의 합 구할 수 있음
result = sum([1, 2, 3, 4, 5])
print(result)

#min(), max() - 최소 최대
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval() - 사람이 표현한 수식을 실제 계산해서
result = eval("(3+5)*7")
print(result)

# sorted() - 반복 가능한 객체의 원소를 정렬
result = sorted([9, 1, 8, 5, 4])
reversed_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reversed_result)

# sorted() with key
array = [('홍길동',35), ('이순신',29), ('김철수',94)]
result = sorted(array, key=lambda x:x[1], reverse=True)
print(result)




# ****************************
# **** itertools(순열,조합) ****
# ****************************

# 순열 : 서로다른 n개에서 r개를 순서 상관있이 선택하여 나열 - nPr
# 조합 : 서로다른 n개에서 r개를 순서 상관없이 선택하여 나열 - nCr
from itertools import permutations
data = ['A', 'B', 'C']

# 순열: 3개 중에서 3개를 선택하는 경우의 수(순서 상관있음)
result = list(permutations(data, 3))
print(result)

from itertools import combinations
data = ['A', 'B', 'C']

# 조합: 3개 중에서 2개를 선택하는 경우의 수(순서 상관없음)
result = list(combinations(data, 2))
print(result)

#중복순열: 3개중 2개를 선택하는 모든 순열(중복허용
from itertools import product
data = ['A', 'B', 'C']

result = list(product(data, repeat=2))
print(result)

#중복조합: 3개중 2개를 선택하는 모든 조합(중복허용)
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))
print(result)


# *****************
# **** Counter ****  반복가능한 객체에서 내부의 원소가 몇번씩 등장했는지 알려줌
# *****************
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))


# ********************
# **** maht.gcd() ****
# ********************
# 최대공약수, 최소공배수 구할 수 있음
import math

# 최소공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14
print(math.gcd(a, b))
print(lcm(a, b))