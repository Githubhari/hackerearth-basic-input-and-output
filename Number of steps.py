n = int(input())
i = 0
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
mi = min(a)
count = 0

#Note : the logic is behind the min value of 'a' list only
#and that min value may change in the process or may not also
#and according our constraint the values inside 'a' or 'b' list must be
#>=0 or <=5000
while n>i:
    if mi<0:
        print(-1)
        quit()
    while a[i]>mi:
        a[i] -= b[i]
        count +=1
    if a[i]<mi:
        mi = a[i]
        i = 0
    else:
        i +=1
print(count)
