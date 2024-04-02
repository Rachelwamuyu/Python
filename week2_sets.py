student_id = {112, 114, 116, 118, 115} #creating a set of integer type
print("Student ID", student_id) #output: Student ID {112, 114, 115, 116, 118}
vowel_letters = {"a", "e", "i", "o", "u"}#creating a set of string type
print("Vowel letters:", vowel_letters)#output: Vowel letters: {'e', 'a', 'u', 'i', 'o'}
mixed_set = {"Hello", 101, -2, "Bye"}#creating a set of mixed data type
print("Set of mixed data types:", mixed_set) #output: Set of mixed data types: {'Hello', 101, -2, 'Bye'}

empty_set = set() #creates an empty set
empty_dictionary = {} #creates an empty dictionary
print("Data type of empty_set is:", type(empty_set))#output: Data type of empty_set is: <class 'set'>
print("Data type of empty_dictionary is:", type(empty_dictionary)) #output Data type of empty_dictionary is: <class 'dict'>
#duplicate items in a set
numbers = {2, 4, 6, 6, 2, 8}
print(numbers) #output {8, 2, 4, 6}
#to add items to a set
numbers = {21, 34, 54, 12}
print("Initial set:", numbers) #output: Initial set: {34, 12, 21, 54}
numbers.add(32)
print("Updated set", numbers) #output: Updated set {32, 34, 12, 21, 54}
#update items in a set
companies={"Lacoste", "Ralph Lauren"}
tech_companies = {"apple", "google", "apple"}
companies.update(tech_companies)
print(companies) #output ; {'apple', 'Lacoste', 'Ralph Lauren', 'google'}
#to remove an element from a list
companies.discard("apple")
print(companies) #output {'Lacoste', 'Ralph Lauren', 'google'}
#iterate over a set
fruits = {"apple", "peach", "Mango"}
for fruit in fruits: #for loop to access each fruit
    print(fruit)
    #output
    """
        apple
        peach
        Mango
        """
even_numbers = {2,4,6,8,10} #finding number of set in elements
print("Set:", even_numbers)  #output Set: {2, 4, 6, 8, 10}
print("Total elements:", len(even_numbers))# output Total elements: 5
#union of two sets
A = {1, 3, 5} #first set
B = {0, 2, 4} #second set
print ("Union using | ", A | B) #output :Union using |  {0, 1, 2, 3, 4, 5}
print ("Union using union ()", A.union(B))  #output : Union using union () {0, 1, 2, 3, 4, 5}
#intersection of two sets
A = {1, 3, 5} #first set
B = {1, 2, 3} #second set
print ("Intersection using & ", A & B)  #output : Intersection using &  {1, 3}
print ("Intersection using intersection ()", A.intersection(B))  #output : Intersection using intersection () {1, 3}
#Differnce between two sets
A = {2, 3, 5} #first set
B = {1, 2, 6} #second set
print ("Difference using - ", A - B) #output :Difference using -  {3, 5}
print ("Difference using difference ()", A.difference(B))  #output : Difference using difference () {3, 5}
#Symmetric Differnce between two sets
A = {2, 3, 5} #first set
B = {1, 2, 6} #second set
print (" Symmetric Difference using ^ ", A ^ B) #output :Symmetric Difference using ^  {1, 3, 5, 6}
print ("Difference using symmetric_difference ()", A.symmetric_difference(B))  #output : Difference using symmetric_difference () {1, 3, 5, 6}
#Checking if two sets are equal
A = {1, 3, 5} #first set
B = {5, 3, 1} #second set
if A == B:
    print("Set A and Set B are equal") #output : Set A and Set B are equal
else:
    print ("Set A and Set B are not equal ")



