def solution(n, lost, reserve):
    answer = n
    reservecopy = reserve.copy()
    lostcopy = lost.copy()
    for value in reservecopy:
        if value in lostcopy:
                lost.remove(value)
                reserve.remove(value)
                print(lost)
    lost.sort()
    reserve.sort()
    for value in reserve:
        min = value -1
        max = value +1
        for n in lost:
            if(n == min):
                lost.remove(min)
            elif(n == max):
                lost.remove(max)
    return answer -len(lost)