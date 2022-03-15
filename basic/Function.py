# global 키워드로 변수 지정하면 함수 바깥에 선언된 변수를 바로 참조
# 함수 안에서는 지역변수가 우선적으로 참조. 같은 이름의 전역/지역변수일 경우 지역변수 참조
# 여러개의 반환 값을 가질 수 있음
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 람다 표현식 - 함수명 없이 한 줄 에 작성할 수 있음
# sort 할때 자주 쓰임
print((lambda a, b: a+b)(3,7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

#sorted에서 key값으로 정렬 할 수 있음
print(sorted(array, key=my_key))
print(sorted(array, key=lambda x:x[1]))

# map을 이용하여 적용가능
list1 = [1, 2, 3, 4, 5]
list2= [6, 7, 8, 9, 10]
result = map(lambda a,b: a+b, list1, list2)
print(list(result))