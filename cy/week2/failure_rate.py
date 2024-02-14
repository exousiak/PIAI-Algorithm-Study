# 2019 KAKAO BLIND RECRUITMENT > 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 실패율 계산 함수
def getFailRate(N, stages):
    fail_rate = []
    # 특정 스테이지를 클리어하지 못한 플레이어 수를 저장할 변수
    fail_num = 0

    for i in range(1, N + 1):
        # 해당 스테이지를 클리어하지 못한 플레이어의 수
        count = stages.count(i)

        # 해당 스테이지를 모두 도달했거나 도달하지 못했다면
        if count == 0:
            fail_rate.append((i, 0))
        else:
            # len(stages) - fail_num : 스테이지에 도달한 플레이어 수
            fail_rate.append((i, count / (len(stages) - fail_num)))
            fail_num += count

    return fail_rate

def solution(N, stages):
    answer = []

    # 실패율 계산
    fail_rate = getFailRate(N, stages)

    # 실패율에 따라 내림차순 정렬
    fail_rate = sorted(fail_rate, key = lambda x: x[1], reverse = True)

    # fail_rate는 (스테이지, 실패율) tuple을 가지므로 r[0] append
    for r in fail_rate:
        answer.append(r[0])

    return answer