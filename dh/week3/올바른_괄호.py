def solution(s):
    stack = []
    
    for i in s:
        if (i == '('):
            stack.append(i)
        elif (len(stack) == 0 and i == ')'):
            return False
        else:
            stack.pop()
    
    if (len(stack) == 0):
        return True
    return False