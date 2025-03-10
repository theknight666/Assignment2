#user input
num = int(input("Enter a number 2: "))

# Checking the number
if num % 2 == 0:
    result = "even"
else:
    result = "odd"

print(f"{num} is an {result} number.")