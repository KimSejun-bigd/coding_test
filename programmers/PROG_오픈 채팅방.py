def solution(record):
    answer = []
    list_id = []
    mapping_id_nickname = {}

    for r in record:
        split_record = list(r.split(' '))
        list_id.append(split_record[1])
        if split_record[0] == 'Enter':
            mapping_id_nickname[split_record[1]] = split_record[2]
            answer.append(split_record[1]+'님이 들어왔습니다.')
        elif split_record[0] == 'Leave':
            answer.append(split_record[1]+'님이 나갔습니다.')
        else:
            mapping_id_nickname[split_record[1]] = split_record[2]

    for i in range(len(answer)) :
        id =  answer[i][0:(answer[i].index('님이 '))]
        answer[i] = answer[i].replace(id, mapping_id_nickname[id])
    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))