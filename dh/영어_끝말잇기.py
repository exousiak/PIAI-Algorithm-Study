def solution(n, words):
    answer = []
    duplicate = []
    for i in range(len(words)):
        if (len(duplicate) == 0):
            duplicate.append(words[i])
        elif (words[i] not in duplicate):
            if (duplicate[-1][-1] == words[i][0]):
                duplicate.append(words[i])
            else:
                answer.append(i%n + 1)
                answer.append(i//n + 1)
                break
        else:
            answer.append(i%n + 1)
            answer.append(i//n + 1)
            break
        if (i == len(words)-1):
            answer.append(0)
            answer.append(0)
            break

    return answer