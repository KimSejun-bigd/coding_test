# 중복허용X
# 순서 없음 - 인덱싱이 불가능
# 리스트 혹은 문자열을 set()을 이용하거나 {} 안에 각 원소를 , 삽입하여 초기화
# !!! 데이터 조회 및 수정을 O(1)의 시간으로 처리 가능 !!!
# 합집합, 교집합, 차집합 연산 제공

# 리스트에 set()을 이용
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# {} 안에 직접 , 로 구분
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)
print(a & b)
print(a - b)

print("=========================")
# 관련함수
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가 - add
data.add(4)
print(data)

# 새로운 원소 여러 개 추가 - update
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제 - remove
data.remove(3)
print(data)