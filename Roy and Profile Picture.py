L = int(input())

for i in range(int(input())):
    W,H = [int(x) for x in input().split()]
    
    #Case-1
    if W<L or H<L:
        print("UPLOAD ANOTHER")
        continue
    
    #case-2
    elif W==H:
        print("ACCEPTED")
        continue
    else:
        print("CROP IT")
