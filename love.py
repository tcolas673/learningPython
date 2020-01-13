from math import sqrt

print('   /|')
print('  / |')
print(' /  |')
print('/   |')

phrase = 'Giraffes\n'
print(phrase)
print(phrase.upper())
print(len(phrase))
# strings are like arrays in python
print(phrase.index('a'))
phrase2 = phrase.replace('Gi', 'Ti')
print(phrase2)
print(pow(3,2))
print(sqrt(32.7))
#all inputs
# name = input('Enter your name:')
# print(name)

friends = ['Kevin', 'Joe', 'Richard', 'Tasha']
print(friends[1:])
print(friends[1:3])
#OPEN INTERVALS?
#LIST METHODS
#https://www.programiz.com/python-programming/methods/list

def say_hi(age):
    #or, and, not
    if age < 18:
        print('You too young son') 
    else: 
        print('Yo! You can hang!')

# Dictionaries in python can be accessed in two ways Dict[key] or use Dict.get(key)
#you can add a default value to .get function Dict.get(key, 'not a valid key')


say_hi(15)
say_hi(23)

def love():
    print('I love you')

love()

print(range(5))
# up to but not including last digit
for i in range(5):
    print(i)
    love()
# do end minus start to find size
# for range(5) 5-0 = 5
# for range(3,5) 5-3 = 2
print(range(3,5))
for i in range(3,5):
    print(i)
    love()

print(list(range(0,10, 2)))
print(3%2)


friendsAgain = [['Kevin', 'Joe', 'Richard', 'Tasha'],
            ['Kevin2', 'Joe2', 'Richard2', 'Tasha2']]
print(friendsAgain[1][0])

# recursive functions
# set up a base case and then have function call itself
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

arr = [0,1,2]
# find middle 
mid = (len(arr) // 2)
print(mid)
print(arr[mid])