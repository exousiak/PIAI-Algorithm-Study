def solution(rsp):
    dic = {'0': '5',
          '2': '0',
          '5': '2'}
    answer=[]
    for i in rsp:
        answer.append(dic[i])
    return ''.join(answer)