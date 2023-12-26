di = {}
n = int(input())
li = [int(x) for x in input().split()]
for i in li:
    di[i] = di.get(i,0) + 1
ma = max(di.values())
count = 0
for i in di.values():
    if ma == i:
        count += 1
print(count)
