'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

N = int(input())
data = [int(x) for x in input().split()]


# Write your code here
num = 0
for i in data:
    num *= 10
    num += int(i%10)

ans = "No"
if (num%10) == 0:
    ans = "Yes"

print(ans)
