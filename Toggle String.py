s = input()
st = ""
for i in s:
    if i.islower():
        st += i.upper()
    else:
        st += i.lower()
print(st)
