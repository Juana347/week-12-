# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

#my_list = ['apple', 'banana', 'cherry']
#print(my_list[0])         # apple
#print(my_list[1:])        # ['banana', 'cherry']

#my_list.append('grape')
#print(my_list)

#my_list.pop(1)
#print(my_list)

# numbers = [3, 1, 4, 2]
#numbers.sort()
#print(numbers)

# collections are used to store multiple items in a single variable
# lists are ordered collections of items
# lists are mutable, meaning you can change their content
# lists are created using square brackets []
list_of_fruits = ["apple", "banana", "cherry", "date"]
print(list_of_fruits) # ['apple', 'banana', 'cherry', 'date']
print (type(list_of_fruits)) 
# Accessing items in a list
print(list_of_fruits[0]) #apple
print(list_of_fruits[1])
print(list_of_fruits[-1])
print(list_of_fruits[1:3])
# reversing a list
list_of_fruits.reverse()
print(list_of_fruits)
print(list_of_fruits[::-1])
# Appending items to a list
list_of_fruits.append("elderberry") #add items to the end of the list
print(list_of_fruits)
list_of_fruits.append("strawberry")
list_of_fruits.append("orange")
list_of_fruits.extend(["fig", "grape", "honeydew"])
#add multiple items to the end of the list
print(list_of_fruits)
# popping items from a list
popped_item = list_of_fruits.pop()
# removes and returns the last item
print(popped_item) # honeydew
print(list_of_fruits)
# inserting items at a specific index 
list_of_fruits.insert(1, "blueberry")
print(list_of_fruits)
# removing a specific item by value 
list_of_fruits.remove("banana")
print(list_of_fruits)
list_of_fruits.insert(3,"banana")
list_of_fruits.sort() # sorts the list in ascending order
print(list_of_fruits)
# Why use lists? instead of individual variables 
# imagine you have 100 items to manage
list_of_items = list(range(1, 1001))
print(list_of_items)
print(len(list_of_items)) # 1000
popped_item = list_of_items.pop(3)
print(popped_item)
# extend by a 1000 more items 
list_of_items.extend(range(1001, 2001))
print(len(list_of_items)) # 2000

# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.