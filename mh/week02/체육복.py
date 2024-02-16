def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for l in lost[:]:
        for r in reserve[:]:
            if l == r:
                lost.remove(l)
                reserve.remove(r)
    
    a = len(lost)     
    for l in lost:
        for r in reserve:
            if l - 1 == r:
                reserve.remove(r)
                a -= 1
            elif l + 1 == r:
                reserve.remove(r)
                a -= 1
                
    answer = n - a
    return answer