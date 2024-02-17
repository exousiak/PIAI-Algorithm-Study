def solution(strings, n):
# 0 s[0,0]u[0,1]n[0,2] 1 bed 2 car
# strings 원소 개수만큼 반복 -> 비교위해

## strings의 index n을 비교 후, lst에 저장
## lst에 있는 idx번호 순으로 저장된 list 출력

    strings.sort()
    
    return sorted(strings,key=lambda x:x[n])