# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    start = 0

    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            start = 0
        else:
            if start % 2 == 0:
                answer += s[i].upper()
                start += 1
            else:
                answer += s[i].lower()
                start += 1

    return answer