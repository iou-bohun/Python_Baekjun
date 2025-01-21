
def solution(progresses, speeds):
    answer =[]
    cnt = 0
    ans = 0
    while(len(progresses)>0):
        if(progresses[0] + cnt*speeds[0])>=100:
            ans = ans+1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if(ans>0):
                answer.append(ans)
                ans =0
            cnt = cnt+1
    answer.append(ans)
    return answer

