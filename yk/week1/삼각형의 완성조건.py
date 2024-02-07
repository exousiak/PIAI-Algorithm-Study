# https://school.programmers.co.kr/learn/courses/30/lessons/120868

def solution(sides):
    a = max(sides)
    b = min(sides)
    i= a-b+1
    count=0
    while(a>i):
        count+=1
        i+=1
    while(a+b>i):
        i+=1
        count+=1
    return count
        
        
