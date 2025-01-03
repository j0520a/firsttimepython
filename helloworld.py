#indent your if statements and functions!!!
#so python knows when to check before running
#the code. Otherwise, it will run if not indented.
#must be indented twice if nested


def greet():
    print("My name is Josh")

def add_numbers(a, b):
    print("The result is ")
    print(a + b)

def multiply_numbers(a, b):
    print("The result is ")
    print(a * b)

def print_phrases(phrase_one, phrase_two):
    print(phrase_one + " " + phrase_two)

greet()
print("Hello World")
print("I'm learning Python ")
add_numbers(2,2)
multiply_numbers(4,4)
print_phrases("You are", "a dummy")


#from NeetCode tutorial
def farewell(item):
    print("Goodbye, " + item)

farewell("Bob")
farewell("Charlie")




# don't modify below this line
farewell("NeetCode")

def two_sum(a, b):
    print(a + b)

def three_sum(a, b, c):
    print(a + b + c)

two_sum(7, 10)
three_sum(3,5,8)


# do not modify below this line
two_sum(10, 9)
three_sum(5, 14, 6)

def product(a, b):
    return a * b



# don't modify below this line
print(product(2, 4))
print(product(8, 2))
print(product(4, 8))
print(product(8, 8))

def check_equal(x, y) -> bool:
    return x == y

def check_not_equal(x, y) -> bool:
    return x != y

def check_less_than(x, y) -> bool:
    return x < y

def check_greater_than(x, y) -> bool:
    return x > y

def check_less_than_or_equal(x, y) -> bool:
    return x <= y

def check_greater_than_or_equal(x, y) -> bool:
    return x >= y

# Don't change below this line
print("2 is equal to 2:", check_equal(2, 2))
print("-2 is equal to 2:", check_equal(-2, 2))

print("-2 is not equal to 2:", check_not_equal(-2, 2))
print("2 is not equal to 2:", check_not_equal(2, 2))

print("2 is less than 3:", check_less_than(2, 3))
print("3 is less than 3:", check_less_than(3, 3))

print("3 is greater than 2:", check_greater_than(3, 2))
print("3 is greater than 2:", check_greater_than(3, 3))

print("3 is less than or equal to 3:", check_less_than_or_equal(3, 3))
print("4 is less than or equal to 3:", check_less_than_or_equal(4, 3))

print("3 is greater than or equal to 3:", check_greater_than_or_equal(3, 3))
print("2 is greater than or equal to 3:", check_greater_than_or_equal(2, 3))