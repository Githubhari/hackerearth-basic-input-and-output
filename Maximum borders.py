t = int(input())
# print(t)
for i in range(t):
    n,m = [int(x) for x in input().split()]
    st = []
    for j in range(n):
        # print(j)
        st.append(input())
    ma = 0
    for k in st:
        count = 0
        for h in range(len(k)):
            if k[h] == '#':
                count += 1
        if ma<count:
            ma = count
    print(ma)
