def solution(number, k):
    answer = ''
    num_list = [int(x) for x in list(number)] # 숫자 나누기 
    listt = [] # 숫자를 담을 리스트
    num_length = len(number) - k # 문제에서 요구하는 리스트 크기
    for i in range(len(number)):
        while k > 0 and listt and listt[-1] < num_list[i]: 
            listt.pop()
            k -= 1
        if k == 0: 
            listt += num_list[i:] # 뒤에 남은 숫자들 붙여줌
            break # k가 0이면 더이상 이 과정을 진행할 수 없으니까 break
        listt.append(num_list[i]) # 숫자 추가
    if len(listt) > num_length: #숫자를 담은 리스트가 정답길이보다 길면 슬라이싱
        listt = listt[:num_length]
    answer = ''.join(map(str,listt)) #리스트들 join함수로 합쳐줌
    return answer