input_data = input()

# 나이트가 이동할 수 있는 방향
rows = ["a", "b", "c", "d", "e", "f", "g", "h"]
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

x, y = 0, int(input_data[1])

for i in range(8):
    if rows[i] == input_data[0]:
        x = i + 1
        break

count = 0

for step in steps:
    # 이동하고자 하는 위치 확인
    nx = x + step[0]
    ny = y + step[1]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)