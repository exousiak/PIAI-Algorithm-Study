# 크기가 작은 부분문자열

def solution(t, p):
    answer = 0

    # p의 길이
    len_p = len(p)

    # p의 길이만큼 t에서 잘라내 확인
    for i in range(len(t) - len_p + 1):
        part = t[i:i + len_p]

        if int(part) <= int(p):
            answer += 1

    return answer

if __name__ == "__main__":
    t = input()
    p = input()

    print(solution(t, p))