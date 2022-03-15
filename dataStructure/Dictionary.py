# 키와 값의 쌍을 데이터로 가지는 자료형
# 순서 없음 - 인덱싱이 불가능
# 변경 불가능한(Immutable) 자료형을 키로 사용 할 수 있음
# 해시 테이블을 이용하므로 데이터 조회/수정에 있어 O(1)의 시간에 처리 가능
# dict() 또는 {} 안에 "key":"value" 로 초기화도 가능

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

data2 = {
    "홍길동" : 97,
    "이순신" : 98
}
print(data2)
print(data2["이순신"])

if '사과' in data:
    print("'사과'를 키로 가지는 데이터 존재")

#키, 밸류만을 리스트로 뽑을 수 있음
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

#각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])