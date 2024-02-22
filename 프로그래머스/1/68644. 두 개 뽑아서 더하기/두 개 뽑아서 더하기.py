def solution(numbers):
    
    ## tuple을 하나 만들기 (더해진 값이 같은 경우 안넣어도 되니)
    ## 같은 수 3개이상 == 안해도 됨
    # 먼저 수를 정렬해준다(오름차순)
    
    lst=[]
    a = set()
    for i in numbers:
        if i not in a:
            if numbers.count(i)>=2:
                lst.append(i)
                lst.append(i)
                a.add(i)
                continue
            lst.append(i)
            a.add(i)
#### 많아야 2개씩만 있게 됨
    sum_num=set()
    
    # 이중 for 문 써야 하나 ..?
    for i in range(len(lst)):
        ## lst 개수 - i 번 반복
        for j in range(i+1,len(lst)):
            sum_num.add(lst[i] + lst[j])
            
    sum_num = sorted(list(sum_num))
                           
    return sum_num