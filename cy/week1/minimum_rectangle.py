# 완전탐색 > 최소직사각형

def solution(sizes):
    answer = 0

    # weight, height를 따로 다룰 수 있도록 리스트 생성
    weights = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]

    for i in range(len(sizes)):
        # 어떤 명함이든 weight가 height 보다 크도록 리스트 정리
        if weights[i] < heights[i]:
            weights[i], heights[i] = heights[i], weights[i]

    answer = max(weights) * max(heights)

    return answer

if __name__ == "__main__":
    # 명함 개수
    n = int(input())

    # 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열
    sizes = []

    for _ in range(n):
        sizes.append(list(map(int, input().split())))

    print(solution(sizes))