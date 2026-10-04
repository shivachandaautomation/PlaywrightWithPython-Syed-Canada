# Python set methods and examples

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)

# add() - adds a single element
my_set.add(6)
print("After add(6):", my_set)

# update() - adds multiple elements
my_set.update([7, 8, 9])
print("After update([7, 8, 9]):", my_set)

# remove() - removes an element; raises error if not found
my_set.remove(3)
print("After remove(3):", my_set)

# discard() - removes an element without error if missing
my_set.discard(10)
print("After discard(10):", my_set)

# pop() - removes and returns a random element
popped = my_set.pop()
print("Popped item:", popped)
print("Set after pop():", my_set)

# clear() - empties the set
my_set.clear()
print("Set after clear():", my_set)

# union() - combines sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a.union(set_b))

# intersection() - common elements
print("Intersection:", set_a.intersection(set_b))

# difference() - elements in set_a not in set_b
print("Difference:", set_a.difference(set_b))

# symmetric_difference() - elements in exactly one set
print("Symmetric difference:", set_a.symmetric_difference(set_b))

# issubset() - checks if one set is subset of another
print("Is {1, 2} subset of set_a?", {1, 2}.issubset(set_a))

# issuperset() - checks if one set contains another
print("Is set_a superset of {1, 2}?", set_a.issuperset({1, 2}))

# copy() - creates a copy
copy_set = set_a.copy()
print("Copy of set_a:", copy_set)

# len() - number of elements
print("Length of set_a:", len(set_a))

# in operator - membership check
print("2 in set_a:", 2 in set_a)

# set() from list to remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

# --------------------------------------------------
# Python tuple methods and examples

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)
print("\nTuple:", my_tuple)

# count() - counts occurrences of an element
print("Count of 20:", my_tuple.count(20))

# index() - returns index of first occurrence
print("Index of 30:", my_tuple.index(30))

# len() - number of items
print("Length of tuple:", len(my_tuple))

# concatenation
print("Concatenated tuple:", my_tuple + (60, 70))

# repetition
print("Repeated tuple:", my_tuple * 2)

# membership check
print("40 in my_tuple:", 40 in my_tuple)

# slicing
print("Slice [1:4]:", my_tuple[1:4])

# min() and max()
print("Min:", min(my_tuple))
print("Max:", max(my_tuple))

# tuple() converts a list to tuple
list_numbers = [1, 2, 3, 4]
print("Tuple from list:", tuple(list_numbers))

# nested tuple example
nested_tuple = ((1, 2), (3, 4))
print("Nested tuple:", nested_tuple)
print("First element of nested tuple:", nested_tuple[0])


