# Create an empty list called my_list
my_list = []

# Append the elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Print my_list to verify the result
print(my_list) 
#extending the list
my_list.extend([50 , 60 ,70])
print(my_list) 

#removing last element from my_list
del my_list[-1]
print(my_list) 

#sorting my_list in ascending order
my_list.sort()

# Print the sorted list
print(my_list)

# Find and print the index of the value 30
index_30 = my_list.index(30)
print("Index of value 30:", index_30)