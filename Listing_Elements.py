# Creates an empty list
my_list = []

# Appends elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserts the value 15 at the second position (index 1)
my_list.insert(1, 15)

# Extendss the list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from the list
my_list.pop()

# Sorts the list in ascending order
my_list.sort()

# Finds and prints the index of the value 30
index_of_30 = my_list.index(30)
print("The index of 30 in the list is:", index_of_30)
