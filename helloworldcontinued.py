def say_hello(name):
    print("Hello, " + name)

say_hello("Abigail")

def get_min(a: int, b: int) -> int:
    if (a < b):
        return a
    else:
        return b
    
# don't modify code below this line
print(get_min(10, 11))
print(get_min(5, -7))
print(get_min(20, 20))

def check_range(num: int) -> str:
    if (num < 0):
        return "negative"
    elif (num == 0):
        return "zero"
    elif (num < 10):
        return "positive single digit"
    elif (num >= 10):
        return "positive multi digit"