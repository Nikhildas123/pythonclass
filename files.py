
# file = open("files.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("files.txt", "r")
# line1 = file.readline()
# print(line1)
# file.close()

# file = open("files.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()

# file = open("files.txt", "w")
# file.write("Hello, World!")
# file.close()

# file = open("files.txt", "w")
# lines = ["Hello\n", "Welcome to Python file handling\n"]
# file.writelines(lines)
# file.close()


# file = open("files.txt", "a")
# file.write("Appended text.\n")
# file.close()

# with open("files.txt", "r") as file:
#  content = file.read()
#  print(content)

# position = file.tell()
# print(position)

# file = open("files.txt", "r")
# file.seek(5) 
# print(file.read())
# file.close()



# try:
#     file-open("filesss.txt","r")
#     content=file.read()
# except FileNotFoundError:
#     print("file not found!")
# finally:
#     file.close()

# x=-5
# if x<0:
#     raise Exception("negative numbers are not allowed")

class negativenumbererror(Exception):
    pass
def check_number(num):
    if num<0:
        raise NegativeNumberError("Negative numbers are not allowed!")
try:
 check_number(-10)
except NegativeNumberError as e:
 print(e)