def solution(X, Y):
    answer = ''
    num = "9876543210"
    
    answer = [i*min(X.count(i), Y.count(i)) for i in num]
    answer = ''.join(answer)
    
    if (answer == ''):
        answer = "-1"
    if (set(answer) == {'0'}):
        answer = "0"
    return answer