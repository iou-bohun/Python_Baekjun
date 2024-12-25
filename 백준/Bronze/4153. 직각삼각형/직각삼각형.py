while(True):
    lst = list(map(int, input().split()))
    if(lst[0] ==lst[1] ==lst[2]==0):
        break
    else:
        lst.sort()
        if (lst[2] * lst[2] == (lst[1] * lst[1] + lst[0] * lst[0])):
            print("right")
        else:
            print("wrong")