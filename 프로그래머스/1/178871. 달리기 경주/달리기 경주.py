# def solution(players, callings):
#     for i in range(len(callings)):
#         idx = players.index(callings[i])
#         players[idx-1], players[idx] = players[idx], players[idx-1]
#     return players

# 시간초과 == list.index() 오래걸림

def solution(players, callings):
    dic = {}
    # player idx 설정
    for i in range(len(players)):
        dic[players[i]]=i
    
    for i in range(len(callings)):
        # 호명된 선수의 idx
        idx = dic[callings[i]]
        
        prev_player = players[idx-1]
        players[idx-1], players[idx] = players[idx], prev_player

        # 교환된 플레이어의 위치 정보를 업데이트합니다.
        dic[callings[i]], dic[prev_player] = idx-1, idx

        
    return players