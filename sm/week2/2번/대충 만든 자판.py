# def solution(keymap, targets):
    
#     answer =[]
    
#     for sen in targets:
#         pres = 0
#         for char in sen:
#             find=False
#             for key in keymap:
#                 if char in key:
#                     pres +=key.index(char)+1
#                     find=True
#                     break
#             if not find:
#                 pres = -1
#                 break
#         answer.append(pres)
        
#     return answer


        # keymap 수만큼 해야하는데 ..?
        # keymap 수만큼 반복 -> 
#         for j in range(len(keymap)): 
#             # 첫번째 keymap에서의 값 ( 'ABACD'라면 k는 A B A C D 가 됨)
#             for k in range(targets[i]):
#                 if keymap[j][] == k
    
#     answer = []
#     return answer


def solution(keymap, targets):
    answer=[]
    dic = {}
    for i in keymap:
        for j, idx in enumerate(i):
            if idx in dic:
                dic[idx] = min(j+1, dic[idx])
            else:
                dic[idx]=j+1
    for t in targets:
        ret = 0
        for j in t:
            if j not in dic:
                ret = -1
                break
            ret +=dic[j]
        answer.append(ret)

    return answer
