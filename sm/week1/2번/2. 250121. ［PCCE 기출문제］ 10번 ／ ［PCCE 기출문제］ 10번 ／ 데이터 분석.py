# data = ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
def solution(data, ext, val_ext, sort_by):
    ans = []
    
    for i in data:
        if ext == 'code' and i[0] < val_ext:
            ans.append(i)
        elif ext == 'date' and i[1] < val_ext:
            ans.append(i)
        elif ext == 'maximum' and i[2] < val_ext:
            ans.append(i)
        elif ext == 'remain' and i[3] < val_ext:
            ans.append(i)
        
### lambda에 대한 이해 : lambda x : x[0]
    # 아래서 쓰인 lambda함수는 ans 원소(?) 에 대한 정의
    # x[0] = code , x[1] = date, x[2] = maximum, x[3] = remain
### sort( key : key 기준 정렬   or    reverse=True : 역순정렬 )
### 새로운 정렬된 리스트를 반환하는 함수는 'sorted 함수'이고, 리스트 자체를 정렬시켜버리는 것은 'sort 함수'
    if sort_by == 'code':
        ans.sort(key=lambda x: x[0])
    elif sort_by == 'date':
        ans.sort(key=lambda x: x[1])
    elif sort_by == 'maximum':
        ans.sort(key=lambda x: x[2])
    elif sort_by == 'remain':
        ans.sort(key=lambda x: x[3])
    
    return ans
