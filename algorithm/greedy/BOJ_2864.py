# 백준 2864번 : 5와 6의 차이
a, b = map(str, input().split())
res_min = int(str(a).replace('6', '5')) + int(str(b).replace('6', '5'))
res_max = int(str(a).replace('5', '6')) + int(str(b).replace('5', '6'))

print(res_min, res_max)