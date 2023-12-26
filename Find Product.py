n = int(input())
li = [int(x) for x in input().split()]
prod = 1
for i in li:
    prod = (prod*i)%(10**9+7)
print(prod)
