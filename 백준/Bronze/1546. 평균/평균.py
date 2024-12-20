import statistics

N = int(input())
lst = list(map(int,input().split()))

lstMax = max(lst)
total = []

for i in lst:
    total.append(i/lstMax*100)

print(statistics.mean(total))