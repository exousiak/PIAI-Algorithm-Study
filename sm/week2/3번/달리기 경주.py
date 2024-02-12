# def solution(players, callings):
#     for i in range(len(callings)):
#         idx = players.index(callings[i])
#         players[idx-1], players[idx] = players[idx], players[idx-1]
#     return players

# 시간초과 == list.index() 오래걸림

def solution(players, callings):
    dic = {}
    
    for i, name in enumerate(players):
        dic[name] = i
    # 결과 : {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
    
    for i in callings:
        idx = dic[i]
        ## prev_player: 딕셔너리인 dic에서의 idx 변환 위해 필요함
        prev_player = players[idx-1]
        ## 실제 위치 변환
        players[idx-1], players[idx] = players[idx], prev_player

        ## 위치 변환 후, 딕셔너리에서 idx 변환
        dic[i], dic[prev_player] = idx-1, idx

        
    return players
