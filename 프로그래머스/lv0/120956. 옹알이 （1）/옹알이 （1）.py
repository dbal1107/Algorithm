can = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    li = 0
    for i in babbling:
        for j in can:
            if j + j in i:
                continue
            if j in i:
                i = i.replace(j, ' ')
        if len(i.strip()) == 0:
            li += 1
    return li