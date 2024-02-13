def solution(my_str, n):  
    answer = []
    cut= ''
    for i in my_str:
        cut += i 
        if len(cut) == n:
            answer.append(cut)
            cut = ''
    if cut != '':
        answer.append(cut)
    return answer
