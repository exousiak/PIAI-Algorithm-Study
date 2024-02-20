def solution(n):
    num_list=[]
    for i in range(1, n+1):
        if n % i == 0:
            num_list.append(i)
    return sum(num_list)