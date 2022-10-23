# def solution(n):
#     bi = list()
#     for num in range((n//2)+1) :
#         bi.append(2*num)
#         ans = sum(bi)
#     return ans

def solution(n):
    return sum([i for i in range(2, n + 1, 2)])
