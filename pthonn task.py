# You are given a string containing only ( and ). Determine whether the string is balanced

a= input("Enter the string: ")
count = 0
for i in a:
    if i == "(":
        count+=1
    else:
        count-=1
    if count == 0:
        print("balanced")   
    else:
        print("no balanced")    


#You are given a sentence. Find the longest word in the sentence. 
# If multiple words havethesame length, return the first one.

sentence=input("Enter the sentence:").split()
longest=""
for i in sentence:
    if len(i)>len(longest):
        longest=i
print(f"Longest word:{longest}")


