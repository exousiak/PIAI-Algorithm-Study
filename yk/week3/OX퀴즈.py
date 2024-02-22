def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split(" = ")
        for j in range(0,1) :
            if eval(i[0]) == int(i[-1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer
