def solution(arr):
    answer = []
    n = None;
    
    for value in arr:
        if(value != n):
            answer.append(value)
        n = value
    return answer