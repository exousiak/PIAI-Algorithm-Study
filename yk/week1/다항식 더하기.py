def solution(polynomial):
    answer=[0,0]
    poly = polynomial.split(" + ")
    for i in poly:
        try:
            answer[1] += int(i)
        except:
            i = i.replace('x','')
            if i == '':
                answer[0] += 1
            else:
                answer[0] += int(i)
    if answer[0] == 0 :
        return '{}'.format(answer[1])
    elif answer[1] == 0:
        if answer[0] == 1:
            return 'x'
        else :
            return '{}x'.format(answer[0])
    else:
        if answer[0] == 1:
            return 'x + {}'.format(answer[1])
        else :
            return '{}x + {}'.format(answer[0], answer[1])
