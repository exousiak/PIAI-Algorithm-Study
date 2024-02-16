#https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    answer=0
    for i in dic: 
        count=0
        for j in spell:
            if i.count(j) ==1 :
                count+=1
        if count == len(spell):
            answer +=1
    if answer > 0 :
        return 1
    else:
        return 2 
            
            
