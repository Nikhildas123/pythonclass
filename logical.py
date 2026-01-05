# 1.Create a program to find the maximum and minimum of two numbers without using any loops or
# conditional statements.
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
max=((a+b)+abs(a-b))//2
min=((a+b)-abs(a-b))//2

print(f"minimum:{min}")
print(f"maximum:{max}")



# 2-Write a program to check whether two numbers are equal without using comparison operators.

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if not(a - b):
    print("numbers are equal")
else:
    print("numbers are not equal")    