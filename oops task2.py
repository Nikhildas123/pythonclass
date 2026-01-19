# 1.You are given a sentence. Reverse each word individually while keeping the word order the same.

# a = input("Enter a sentence: ")
# b = a.split()
# result = []

# for i in b:
#     rev = ""
#     for j in i:
#         rev = j + rev
#     result.append(rev)
# print(" ".join(result))



#2-You are given a list of strings. Find the longest common prefix among them.
def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for s in strings[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]

        if prefix == "":
            break

    return prefix


arr = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(arr))
