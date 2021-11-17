# Q1 - 
# The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following: 123..n
# Notice the end argument in print. By default, successive print statements print in newline. 
# As this question requires the integers to be printed in the same line, this method modifies the default print behavior. 
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1): 
        print(i, end='')

# Q2 - Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Explanation - https://www.youtube.com/watch?v=vzG6hDMGI0M

def minion_game(string):
    # your code goes here
    st_sc, kev_sc = 0, 0
    vowels = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vowels:
            kev_sc += len(string) - i
        else:
            st_sc += len(string) - i
    
    if kev_sc > st_sc:
        print('Kevin', kev_sc)
    elif kev_sc < st_sc:
        print('Stuart', st_sc)
    else:
        print('Draw')

 # Q3 - Integer division vs float division
a = 3
b = 5
print(a//b)  # integer division
# prints 0
print(a/b)   # float division
# prints 0.6

# Q4 - Find the number of occurances of a substring in a string. 
# 'cdc' in 'abcdcdc' should return 2

def count_substring(string, sub_string):
    counter = 0    
    for i in range(len(string) - len(sub_string) + 1):
        if sub_string == string[i: i+len(sub_string)]:
            counter += 1

    return counter

# Q5 - 
