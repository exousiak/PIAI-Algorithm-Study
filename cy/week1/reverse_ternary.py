# 3진법으로 나타낸 n을 앞뒤로 뒤집은 후 반환하는 함수
def getTernary(n, result):
    # 재귀함수 중단 조건
    if n // 3 == 0: return result + str(n % 3)

    result += str(n % 3)
    n = n // 3

    return getTernary(n, result)

def solution(n):
    answer = 0

    inverse = getTernary(n, '')

    # 십진법 수로 바꾸기
    n = len(inverse) - 1

    for i in inverse:
        answer += int(i) * (3 ** n)
        n -= 1

    return answer

if __name__ == "__main__":
    n = int(input())

    print(solution(n))