n = int(input())
grids = list(input())
ans = "YES"

for i in range(len(grids)):
    if grids[i] == '.':
        grids[i] = 'B'
for i in range(len(grids)-1):
    if grids[i] == 'H' and grids[i+1] == 'H':
        ans = "NO"

if ans == "YES":
    print(ans)
    print("".join(grids))
else:
    print(ans)
