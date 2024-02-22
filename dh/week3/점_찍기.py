def solution(k, d):
    answer = 0
    d_2 = d**2
    for i in range(0, d+1, k):
        y = int((d_2 - i**2)**(0.5))
        answer += (y // k) + 1
    
    return answer