def solution(participant, completion):
    m = {}
    for i in participant:
        m[i] = m.get(i,0)+1
    for i in completion:
        m[i] -= 1
        
    fin = [k for k, v in m.items() if v > 0]
        
    return fin[0]