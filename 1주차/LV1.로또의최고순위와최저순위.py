def solution(lottos, win_nums):
    answer = []
    zero = 0 # 0인것 개수
    cnt = 0 # 맞는 번호 개수

    #맞는 번호
    for l in lottos:
        if l == 0:
            zero += 1 # 0 개수
        for w in win_nums:
            if w == l:
                cnt += 1 # 일치 번호 수

    if zero == 6: # 6개를 다 모른다면
        zero = 5 # 예외 처리

    # 최고, 최저 순위
    if 7 - cnt >= 6 :
        answer.append(6-zero)
        answer.append(6) # 2개 이하 맞추면 6등  
    else : 
        answer.append(7 - cnt - zero)
        answer.append(7 - cnt) # 2개 이상 맞추었을때 n 등
    
    return answer













    #ideal solution
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]