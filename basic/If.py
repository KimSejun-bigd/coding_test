# 조건문 if ~ elif ~! else
# in, not in - 다수의 데이터를 담는 자료형에서 사용(리스트, 튜플, 문자열, 딕셔너리 전부 가능)
# if문에서 아무것도 처리하고 싶지 않을때 pass 키워드
a = 5

if a >= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a >= -10")
else:
    print("-10 > a")

# 논리연산자 and, or, not
a = 15

if a <= 20 and a >= 0:
    print("Yes")

score = 85

if score >= 80:
    pass
else:
    print('80점미만')
print("끝")