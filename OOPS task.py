#Question 2: Butterfly Pattern
#Write a program to print the Butterfly Pattern like given below:
n = int(input("Enter number of rows: "))


for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

#2 You are given an array of positive integers. Your task is to reverse the digits of each element in
#the array without the use of built-in functions and return a new array with these reversed
#numbers.(Use any language.)
arr = [12, 23, 54]
reversed_arr = []

for num in arr:
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    reversed_arr.append(rev)

print(*reversed_arr)
