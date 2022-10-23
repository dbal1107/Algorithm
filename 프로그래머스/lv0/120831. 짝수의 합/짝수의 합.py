def solution(n):
    bi = list()
    for num in range((n//2)+1) :
        bi.append(2*num)
        ans = sum(bi)
    return ans