def generate_numbers(limit):

    number = 1

    while number <= limit:
        yield number
        number += 1


for value in generate_numbers(5):
    print(value)