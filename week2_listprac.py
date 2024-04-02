#Python sequence data type
#list
list_a=[1, 2, 3, 4, 5] #sequence of same data type: integers
#index  0  1  2  3  4
print(list_a) #output [1, 2, 3, 4, 5]
print(list_a[2]) #printing index 2 which will give '3' as the output
list_a[0]=10 #lists are mutable(can be changed) but tuples are immutable
#assigning index 0 value"10" to change it from 1 to 10
print(list_a)# output [10, 2, 3, 4, 5]
print(len(list_a))#to get the length of list_a. Output '5'
list_a.insert(len(list_a), 6) #to add an item at a specified index
print(list_a)# output [10, 2, 3, 4, 5, 6]
list_a.append(7)# to add another item at the end of you list
print(list_a)# output [10, 2, 3, 4, 5, 6, 7]
list_a.extend([8, 9])#to add items of lists and other iterables at the end of the list
print(list_a)#output [10, 2, 3, 4, 5, 6, 7, 8, 9]
prime_number = [2, 3, 5]
print("List1", prime_number) #output List1 [2, 3, 5]
even_number=[4, 6, 8]
print("List2", even_number) #output List2 [4, 6, 8]
prime_number.extend(even_number)#joiniing two list
print("List after extend:", prime_number) #output List after extend: [2, 3, 5, 4, 6, 8]
list_a.pop(8)#to delete a value 9 which is index 8
print(list_a)#output [10, 2, 3, 4, 5, 6, 7, 8]
del list_a[7]#to delete a value 8 which is index 7
print(list_a)#output [10, 2, 3, 4, 5, 6, 7]
for item in list_a: #iterate through list; look through every item listed, each item displayed on its own
    print(item)
list_b=[1, "today", True, 3.0] #sequence of different data types: integer, string, boolean, float
print(list_b)
list_c=["skinny", "Rachel", "Wamuyu"]#sequence of same data type"string"
list_d=[1, 2, 3, [4, 5], 6, 7]#sequence of nested list
list_e=[]# an empty list
languages=["python", "Swift", "C++"]#list slicing in python
print(languages[-1])#output C++
print(languages[-3])#output python
languages[2]= 'C' #changing the 3rd item C++ to be C
print(languages)#output ['python', 'Swift', 'C']
many_languages=["Python", "Swift", "C++", "C", "Java", "Rust", "R"]
del many_languages[1]#deleting the second item
print(many_languages) # output ['Python', 'C++', 'C', 'Java', 'Rust', 'R']
del many_languages[-1] #deleting the last item
print(many_languages) # output ['Python', 'C++', 'C', 'Java', 'Rust']
del many_languages[0:2] #deleting the first two items
print(many_languages) #output ['C', 'Java', 'Rust']
many_languages.remove("Java")# removing item present at a given index; to remove "Java" from the list
print(many_languages) #output ['C', 'Rust']
my_list=['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i']
print(my_list[2:5]) #items from index 2 to index 4 ; #output ['o', 'g', 'r']
print(my_list[5:])#items from index 5 to the end ; #output ['a', 'm', 'i']
print(my_list[:])# items from beginning to the end ;  ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i']
#a list comprehension that makes each item increase by the power of two
numbers = [number*number for number in range (1,6)] 
print(numbers) #output [1, 4, 9, 16, 25]


