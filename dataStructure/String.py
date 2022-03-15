# 문자열 + 문자열 => Concat 가능
# 곱셈 연산의 경우 문자열이 그 값만큼 여러번 더해짐
# 문자열의 특정 인덱스 값을 변경할 수는 없다(Immutable)

a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a*3)

a = "ABCDEF"
print(a[2:4])

#a[2] = 'a' 문자열 중 특 정 인덱스만 변경 불가!