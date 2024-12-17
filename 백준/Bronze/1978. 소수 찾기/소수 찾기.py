def IsDecimal(num):
    for i in range(2,num):
        if num % i ==0:
            return  False
    return True

cnt =0

n = int(input())

a = list(map(int,input().split()))

for i in a:
    if(i ==1 or i==0):
        continue
    if(IsDecimal(i)==True):
        cnt +=1
print(cnt)