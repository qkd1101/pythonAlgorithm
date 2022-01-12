def solution(citations):
    citations.sort()
    h = 0
    for i in range(citations[-1],-1,-1):
        cnt_d = 0
        cnt_u = 0
        for k in citations:
            if k >= i:
                cnt_u += 1
            if k <= i :
                cnt_d += 1
        if cnt_u < i or cnt_d > i:
            continue
        if h < i:
            h = i
    return h