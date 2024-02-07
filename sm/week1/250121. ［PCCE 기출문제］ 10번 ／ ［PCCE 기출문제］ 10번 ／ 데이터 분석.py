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
    if sort_by == 'code':
        ans.sort(key=lambda x: x[0])
    elif sort_by == 'date':
        ans.sort(key=lambda x: x[1])
    elif sort_by == 'maximum':
        ans.sort(key=lambda x: x[2])
    elif sort_by == 'remain':
        ans.sort(key=lambda x: x[3])
    
    return ans
