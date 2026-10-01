# Python List Methods and Functions

numbers = [30, 10, 20, 40, 10]

print("Original list:", numbers)

# append()
numbers.append(50)
print("append(50):", numbers)

# extend()
numbers.extend([60, 70])
print("extend([60, 70]):", numbers)

# insert()
numbers.insert(1, 15)
print("insert(1, 15):", numbers)

# remove()
numbers.remove(10)
print("remove(10):", numbers)

# pop()
removed = numbers.pop()
print("pop():", numbers)
print("Removed element:", removed)

# index()
print("index(20):", numbers.index(20))

# count()
print("count(10):", numbers.count(10))

# sort()
numbers.sort()
print("sort():", numbers)

# reverse()
numbers.reverse()
print("reverse():", numbers)

# copy()
new_list = numbers.copy()
print("copy():", new_list)

# clear()
new_list.clear()
print("clear():", new_list)

# sum()
print("sum():", sum(numbers))

# min()
print("min():", min(numbers))

# max()
print("max():", max(numbers))

# len()
print("len():", len(numbers))
