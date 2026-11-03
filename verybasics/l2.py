numbers = [10, 20, 30, 40, 50]

print("Total:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Average:", sum(numbers) / len(numbers))

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")