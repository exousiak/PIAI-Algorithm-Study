def solution(n, s):
    divide = s//n
    if (divide == 0) :
        return [-1]
    else:
        answer = [divide for i in range(n)]
        for j in range(s%n):
            answer[j] += 1
    answer.sort()
    return answer