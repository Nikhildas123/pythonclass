#1-Create a set with values {1, 2, 3, 4}
myset = {1, 2, 3, 4}
print(myset)

#2-Add the value 5 to the set {1, 2, 3, 4} using a set method
my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)

#3- Remove the value 3 from the set {1, 2, 3, 4} using a set method
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)

#4- Check if 2 exists in the set {1, 2, 3, 4} .
my_set = {1, 2, 3, 4}
print(2 in my_set)

#5-Convert the list [1, 2, 2, 3, 4, 4] into a set to remove duplicates.
mylist = [1, 2, 2, 3, 4, 4]
myset = set(mylist)
print(myset)

#6-Convert the tuple (10, 20, 30) into a set.
my_tuple = (10, 20, 30)
my_set = set(my_tuple)
print(my_set)

#7- Find the union of sets {1, 2, 3} and {3, 4, 5} .
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)

#8-Find the intersection of sets {1, 2, 3} and {3, 4, 5} .
set1={1,2,3}
set2={3,4,5}
result=set1 & set2
print(result)

#9-Find the intersection of sets {1, 2, 3} and {3, 4, 5} .
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1.intersection(set2)
print(intersection)

#10- Create a copy of the set {5, 6, 7} using a set method.
set1 = {5, 6, 7}
setcopy =set1.copy()
print(setcopy)

#11-Remove all elements from the set {1, 2, 3} using one set method.
my_set = {1, 2, 3}

my_set.clear()

print(my_set)

#12-Check whether {1, 2} is a subset of {1, 2, 3} .
set1 = {1, 2}
set2 = {1, 2, 3}

helo= set1.issubset(set2)

print(helo)

#13-Check whether {1, 2, 3} is a superset of {1, 2}
set1 = {1, 2, 3}
set2 = {1, 2}

hello = set1.issuperset(set2)

print(hello)

#14-Find the symmetric difference between {1, 2, 3} and {3, 4, 5} .
set1 = {1, 2, 3}
set2 = {3, 4, 5}

dif= set1.symmetric_difference(set2)

print(dif)

#15-Add multiple elements {8, 9, 10} into {1, 2, 3} using a set method.
my_set = {1, 2, 3}

my_set.update({8, 9, 10})

print(my_set)

#16- Remove a random element from the set {1, 2, 3} using a set method
my_set = {1, 2, 3}

removed_element = my_set.pop()

print("Removed element:", removed_element)
print("Updated set:", my_set)

#17- Check if two sets {1, 2, 3} and {3, 2, 1} are equal.
set1 = {1, 2, 3}
set2 = {3, 2, 1}

are_equal = set1 == set2

print(are_equal)

#18- From the list [1, 2, 2, 3, 4, 4, 5] , extract only unique values using a set.
my_list = [1, 2, 2, 3, 4, 4, 5]

unique_values = set(my_list)

print(unique_values)

#19- Convert the set {1, 2, 3} into a list
my_set = {1, 2, 3}

my_list = list(my_set)

print(my_list)

#20-From {1, 2, 3, 4, 5} , remove {2, 4} using a set method.
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4}

set1.difference_update(set2)

print(set1)
