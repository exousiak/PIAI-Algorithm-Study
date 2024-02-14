# 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963?language=python3

def solution(name, yearning, photo):
    answer = []
    count = 0

    for p in photo:
        # count 초기화
        count = 0
        for i, n in enumerate(name):
            if n in p:
                # name[i]의 그리움 점수는 yearning[i]
                count += yearning[i]

        answer.append(count)

    return answer