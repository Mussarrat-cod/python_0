def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print(add(10, 20))
print(subtract(20, 10))
print(multiply(5, 4))
print(divide(20, 5))