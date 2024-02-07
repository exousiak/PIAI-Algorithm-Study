def solution(my_string):
    ans = []
    for i in my_string:
        if i.isupper() == True:
            ans.append(i.lower())
        else:
            ans.append(i.upper())
    return ''.join(ans)