#이코테2021 (유투브 동빈나)
# 문자열 재정렬

input_data = input()

sum = 0
list_alpah = []

for i in input_data:
    #숫자면 더함
    if i.isdigit():
       sum += int(i)
    #알파벳이면 리스트에 담음
    else:
        list_alpah.append(i)

#리스트에 담긴 알파벳을 정렬한뒤 더한 숫자를 합쳐줌
print("".join(sorted(list_alpah))+str(sum))
