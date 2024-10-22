def add_things(a, b):
   result = (a * 3) + (b * 3)
   return result

add_things("love", "Gators")
output = add_things("love", "Gators")
print(output)






# this function has two parameters, and it returns a value

def drink_expenses(price, count):
   total = price * count
   return total

# assign the returned value to a new variable, result
result1 = drink_expenses(4.49, 5)
result2 = drink_expenses(6, 5)
result3 = drink_expenses(5.49, 5)

print(result1, result2, result3)


def breakfast():
    food = 'eggs'
    drink = 'coffee'
    print("Breakfast:")
    print(food, drink, "\n")

def lunch():
    food = 'salad'
    drink = 'iced tea'
    print("Lunch:")
    print(food, drink, "\n")

# run the functions
lunch()
breakfast()



# error handling: use this try/except pattern

def test_for_int(num):

    try:
        num = int(num)
        message = str(num) + " is an integer. Good job!"

    # this exception handles any entry that was NOT an integer
    except ValueError:
        message = "Error: You did not provide a whole number."

    return message

# ask for user input
response = input("Enter a number: ")

# run the function, and print what is returned
print( test_for_int(response) )

def test_for_int2(num):

    if True:
        num = int(num)
        message = str(num) + " is an integer. Good job!"

    # this exception handles any entry that was NOT an integer
    else:
        message = "Error: You did not provide a whole number."

    return message

response = input("Enter a number: ")

# run the function, and print what is returned
print( test_for_int2(response) )