def solution(s):
    answer = True
    stack=[]
    for value in s:
        if(value =="("):
            stack.append(value) 
        else:
            if(len(stack) ==0): answer = False
            else:
                stack.pop()
    if(stack !=[]): answer = False
    return  answer