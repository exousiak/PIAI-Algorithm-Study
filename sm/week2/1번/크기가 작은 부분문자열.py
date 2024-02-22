def solution(t, p):
    
    lst = []
    ### len(t) - len(p) 번 뽑아 리스트화 하면 됨
    ### 7 -  3  == 4
    ### 문자열 추출
    cnt = len(t) - len(p) 
    
    for i in range(cnt+1):
        num = t[i:i+len(p)]
        lst.append(num)
        
    sml = 0
    for i in range(len(lst)):
        if int(lst[i]) <= int(p):
            sml +=1 
            
    return sml

# 
