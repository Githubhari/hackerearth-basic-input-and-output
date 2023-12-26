de = input()
inv = False
if (int(de[0]) + int(de[1]))%2 != 0:
    inv = True
if(de[2] in "AEIOUY"):
    inv = True
if (int(de[3])+int(de[4]))%2 != 0:
    inv = True
if (int(de[4]) + int(de[5]))%2 != 0:
    inv = True
if (int(de[7]) + int(de[8]))%2 != 0:
    inv = True
if inv:
    print("invalid")
else:
    print("valid")
