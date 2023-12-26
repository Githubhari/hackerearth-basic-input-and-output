word = list(input())
di = {}
for i in word:
    di[i] = di.get(i,0)+1
x = di['z']
y = di['o']
if (2*x) == y:
    print("Yes")
    quit()
print("No")
