# [PCCE 기출문제] 9번 / 이웃한 칸
# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    # 정수를 저장할 변수 n을 만들고 board의 길이를 저장
    n = len(board)

    # 같은 색으로 색칠된 칸의 개수를 저장할 변수 count 생성
    count = 0

    # h, w의 변화량을 저장할 정수 리스트 생성
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    # 반복문 수행
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]

        if (0 <= h_check < n) and (0 <= w_check < n):
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count