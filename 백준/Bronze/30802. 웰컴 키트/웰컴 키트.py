N = int(input())
list = input().split()
llist= input().split()
a =0
for i in list:
    if(int(i)%int(llist[0])) ==0:
        a+=(int(i) // int(llist[0]))
    else:
        a+=(int(i) // int(llist[0]))+1
b= N//int(llist[1])
c = N%int(llist[1])

print(a)
print(b,c)