def caseConversion (s):
    ls = []
    for x in range(len(s)):
        
        if x==0:
            ls.append(s[x].lower())
        
        elif s[x].isupper():
            ls.append("_")
            # print(ls)
            ls.append(s[x].lower())
        else:
            ls.append(s[x])
    return ''.join(ls)

T = int(input())
for _ in range(T):
    s = input()

    out_ = caseConversion(s)
    print (out_)
