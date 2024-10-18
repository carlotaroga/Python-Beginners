# fruit = 'apple'
# print(fruit)

# fruit = 'pear'
# print(fruit)

# 5 + 2

# sum = 5 + 2
# print(sum)



# print('Hello world!')
# print('What is your name?') # ask for their name
# myName = input()
# print('It is good to meet you, ' + myName)
# print('The length of your name is:')
# print(len(myName))
# print('What is your age?') # ask for their age
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.')


print("What is your name?")
name = input()
print("How old are you?")
age = input()

if name == 'Alice' and int(age) < 13:
    print("How's Wonderland?")
elif name == 'Alice':
    print("You are too old to enter through the looking glass, Alice.")
elif int(age) < 13:
    print('This is only for Alice, kiddo.')
else:
    print('You are not Alice, and you are 13 or older.')
