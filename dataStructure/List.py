#리스트 컴프리헨션

#1차원 리스트 초기화
array = [i for i in range(20) if i % 2 ==1]
print(array)

#2차원 리스트 초기화 방법
_2array = [[0] * 6 for _ in range(5)]
print(_2array)

# append
# sort()
# sort(reversed=True) 내림차순
# reverse() 원소 뒤집기
# insert(a, b) 인덱스a에 3 차가
# count(a) 값이 a인 데이터 개수
# remove(a) 값이 a인 데이터 삭제 - 한개만 삭제가능!

# 여러
a = [1, 2, 3, 4, 5, 5, 5]
removed_set = {3,5}

result = [i for i in a if i not in removed_set]
print(result)