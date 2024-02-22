from collections import deque

n = int(input())
adventures = list(map(int, input().split()))
adventures.sort()
adventures = deque(adventures)
result = 0  # 여행을 떠날 수 있는 그룹 수의 최댓값
count = 0

# 남아있는 모험가의 수가 현재 모험가의 수보다 클 경우 반복
while len(adventures) >= adventures[0]:
    value = adventures.popleft()

    # 1일 경우 혼자 그룹 생성
    if value == 1:
        result += 1
    else:
        # adventures에서 value명 pop
        for i in range(value):
            # 같아야만 그룹 생성 가능
            if value != adventures[0]:
                break
            else:
                count += 1

        # value명 모였는지 확인
        if count == value:
            result += 1

print(result)