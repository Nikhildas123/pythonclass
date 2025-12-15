#1--Create a list [1,2,3] and add 4 to the end using a list method.
a = [1,2,3]
a.append(4)
print(a)

#2--Given [10,20,30], remove 20 using a list method.
b = [10,20,30]
b.remove(20)
print(b)

#3--From [5,3,9,1], sort the list in ascending order using a list method.
c = [5,3,9,1]
c.sort()
print(c)

#4-- From [1,2,3,4,5], extract [2,3,4] using slicing only.
d= [1,2,3,4,5]
print(d[1:4])

#5--Reverse [1,2,3,4] using slicing (no loops).
e= [1,2,3,4]
print(e[::-1])

#6-- Combine [1,2] and [3,4] into one list using list operations.
f = [1,2] + [3,4]
print(f)

#7--Convert [7,8] into [7,8,7,8] using list operations.
g = [7,8]
g= g * 2
print(g)

#8-- Check if 3 exists in [1,2,3,4] using a list operator.
print(3 in [1,2,3,4])

#9--Count how many times 2 appears in [1,2,2,3,2] using a list method.
print([1,2,2,3,2].count(2))

#10-- Remove the last element from ["a","b","c","d"] using a list method.
h = ["a","b","c","d"]
h.pop()
print(h)

#11-- Insert "x" at index 1 in ["a","b","c"] using a list method.
i = ["a","b","c"]
i.insert(1,"x")
print(i)

#12-- Replace the element at index 2 in [10,20,30,40] with 99 using indexing.
j = [10,20,30,40]
j[2] = 99
print(j)

#13-- Convert range(5) into a list using list functions.
k = list(range(5))
print(k)

#14-- Using slicing, extract every 2nd element from [1,2,3,4,5,6] → expected [2,4,6].
l = [1,2,3,4,5,6]
print(l[1::2])

#15-- Remove all elements from [1,2,3] using one list method.
m = [1,2,3]
m.clear()
print(m)

#16-- Copy a list [4,5,6] using only list tools (no modules).
n= [4,5,6]
copy_list = n.copy()
print(copy_list)

#17--Convert [1,2,3] into a nested list [[1,2,3]] using list operations.
o = [1,2,3]
o= [o]
print(o)

#18--Extend [1,2] with [3,4,5] using a list method.
p= [1,2]
p.extend([3,4,5])
print(p)

#19-- Using list repetition, create a list ["hello","hello","hello"].
q = ["hello"] * 3
print(q)

#20-- Remove the element at index 2 from [10,20,30,40] using a list method.
r = [10,20,30,40]
r.pop(2)
print(r)