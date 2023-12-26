n = int(input())
for i in range(n):
    green,red = [int(x) for x in input().split()]
    students = int(input())
    di = {}
    for i in range(students):
        prob1,prob2 = [int(x) for x in input().split()]
        di[1] = di.get(1,0) + prob1
        di[2] = di.get(2,0) + prob2
    valu = di.values()
    # print(valu)
    val1 = max(valu) * min(green,red)
    val2 = min(valu) * max(green,red)
    print(val1+val2)
