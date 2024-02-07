def solution(name, yearning, photo):
    
    # photo[2][3] size일때, for문은 3번 돌아야 함
    # 이중 for문 생각 남 ..
    ## 
    name2yearn={}
    score=[]
    for i in range(len(yearning)):
        name2yearn[name[i]]=yearning[i] 
        
    for j in photo:
        score2=0
        for k in j:
            if k in name2yearn:
                score2 += name2yearn[k]
        
        score.append(score2)
        
    return score
