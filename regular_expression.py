import re
#1
text = "Hello world"
print(re.search(r"world", text))

#2
text = "Hello world"
print(re.match(r"Hello", text))
print(re.match(r"world", text))


#3
text = "I have 2 apples and 5 oranges."
print(re.findall(r"\d+", text))

text = "The price is 45 dollars, 30 cents, and 50 rupees."
print(re.findall(r"\d+", text))

#4
text = "I have 2 apples and 5 oranges."
for match in re.finditer(r"\d+", text):
 print(match.group(), "at", match.start())


 #5
 text = "Hello 123, welcome 456!"
print(re.sub(r"\d+", "number", text))


#6
text = "apple, orange; banana, grape"
print(re.split(r"[;,]", text))

#7
text = "John: 34, Alice: 45, Bob: 23"
print(re.findall(r"(\w+): (\d+)", text)) 

#8
pattern = re.compile(r"\d+")
text = "123 apples and 456 oranges"
print(pattern.findall(text))
#9
text = "HELLO world"
print(re.search(r"hello", text, re.IGNORECASE))

#10
text = """first line
second line
third line"""
# Find all lines starting with 's'
print(re.findall(r"^s\w+", text, re.MULTILINE))
# ['second']
# Find all lines ending with 'e'
print(re.findall(r"\w+e$", text, re.MULTILINE))
# ['line', 'line']

#11
text = "Hello\nWorld"
# Normal dot (.) → won't cross newline
print(re.search(r"Hello.*World", text))
# None

#12
email = "user@example.com"
if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
 print("Valid email")
else:
 print("Invalid email")


 #13
 text = "Card: 1234-5678-9012-3456"
print(re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", "****-****-****-****", text))
