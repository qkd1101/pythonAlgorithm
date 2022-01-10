def solution(s):
    min = 1001
    size = len(s)
    if size == 1:
        return 1
        
    for i in range(1,size):
        result = 0
        dict = []
        for k in range(0,size,i):
            dict.append(s[k:k+i])

        #문자열 제거
        cnt = 0
        temp = dict[0]
        
        while dict:
            if temp == dict[0]:
                cnt += 1
                dict.pop(0)
            else :
                if cnt != 1:
                    result += len(str(cnt)) + i
                else :
                    result += i
                cnt = 0
                temp = dict[0]
                
        # 마지막 처리
        if cnt != 1:
            result += len(str(cnt)) + len(temp)
        else :
            result += len(temp)
        if min > result:
            min = result

    return min