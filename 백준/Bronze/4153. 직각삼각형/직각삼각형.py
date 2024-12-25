while(True):
    lst = list(map(int, input().split()))
    if(lst[0] ==lst[1] ==lst[2]==0):
        break
    else:
        lst.sort()
        a = lst[2]
        b = lst[1]
        c = lst[0]
        if (a * a == (b * b + c * c)):
            print("right")
        else:
            print("wrong")