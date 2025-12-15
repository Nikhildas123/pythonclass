
user1 = float(input("Enter first number: "))
user2 = float(input("Enter second number: "))


operator = input("Enter operator (+, -, *, /): ")


if operator == '+':
    print("Result:", user1 + user2)

elif operator == '-':
    print("Result:", user1 - user2)

elif operator == '*':
    print("Result:", user1 * user2)

elif operator == '/':
    if user2 != 0:
        print("Result:", user1 / user2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("zero")
