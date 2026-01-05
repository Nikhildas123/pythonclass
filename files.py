
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

file = open("files.txt", "r")
file.seek(5) 
print(file.read())
file.close()