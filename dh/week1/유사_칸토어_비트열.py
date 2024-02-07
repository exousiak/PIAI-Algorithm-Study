# 초기 풀이
# def solution(n, l, r):
#     answer = 0
#     for i in range(l-1,r):
#         if ((i%5 != 2) and ((i//5)%5 != 2)):
#             answer += 1
#             print(i, " ")
    
#     return answer

def check(i):
    if i % 5 == 2:
        return False
    if i < 5:
        return True

    return check(i // 5)

def solution(n, l, r):
    answer = 0
    for i in range(l-1,r):
        if check(i):
            answer += 1
    
    return answer
