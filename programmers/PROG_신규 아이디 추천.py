import re

def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub('[^a-z0-9._-]', '', new_id)
    # 3단계
    new_id = re.sub('[.]{1,}', '.', new_id)
    # 4단계
    new_id = re.sub('^[.]', '', new_id)
    new_id = re.sub('[.]$', '', new_id)
    # 5단계
    if new_id == '':
        new_id+='a'
   # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = re.sub('[.]$', '', new_id)
    # 7단계
    if len(new_id) <=2:
        c = new_id[-1]
        new_id += c*(3-len(new_id))
    return new_id

if __name__ == '__main__':
    # print(solution('...!@BaT#*..y.abcdefghijklm'))
    print(solution('abcdefghijklmn.p'))
    # solution('')