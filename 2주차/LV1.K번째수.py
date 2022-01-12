def solution(array, commands):
    answer = []
    while commands:
        list = commands.pop(0)
        temp = array[list[0]-1:list[1]]
        temp.sort()
        answer.append(temp[list[2]-1])
    return answer