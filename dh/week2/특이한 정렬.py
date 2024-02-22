def sort_function(num,n):
    return (abs(num-n), -num)

def solution(numlist, n):
    answer = []
    
    answer = sorted(numlist, key=lambda x: sort_function(x, n))
    return answer