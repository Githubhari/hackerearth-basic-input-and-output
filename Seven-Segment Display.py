matchsticks = [6,2,5,5,4,5,6,3,7,6]

#part-1

T = int(input())
for i in range(T):
    num_of_matchsticks = 0
    num = input()
    for i in num:
        num_of_matchsticks += matchsticks[int(i)]

    #part-2
    if num_of_matchsticks%2 == 0:
        print("1"*(num_of_matchsticks//2))
    else:
        num_of_matchsticks -= 3
        print("7"+("1"*(num_of_matchsticks//2)))
