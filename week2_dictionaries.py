#dictionary data type
#creating a dictionary of same data type (string) named capital_city
capital_city = {'Nepal': 'Kathmandu', "Italy": 'Rome', 'England': 'London'}
print("Initial deictionary:" ,capital_city) #output: Initial deictionary: {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print (capital_city.keys()) #output: dict_keys(['Nepal', 'Italy', 'England'])
print (capital_city.values()) #output : dict_values(['Kathmandu', 'Rome', 'London'])
print(capital_city['Nepal']) #output Kathmandu
capital_city["Japan"] = "Tokyo" #adding more elements in python dictionary
print("Updated Dictionary:" ,capital_city) #output: Updated Dictionary: {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London', 'Japan': 'Tokyo'}
#print(capital_city['Kathmandu']) #throws away error
#creating a dictionary of different data type (string and integer) named numbers
numbers = {1: "one", 2: "two", 3: "three"}
print(numbers) # output: {1: 'one', 2: 'two', 3: 'three'}
numbers["55"]="fifty five"
print("Added element:" ,numbers)#adding more elements in the dictionary
student_id ={111: "Erick" , 112:"Kyle" , 113:"Butters"}
print("Initial Dictionary:" , student_id) # output : Initial Dictionary: {111: 'Erick', 112: 'Kyle', 113: 'Butters'}
student_id[112] = "Stan" #changing the value of the dictionary
print("Updated dictionary:" , student_id) #output:Updated dictionary: {111: 'Erick', 112: 'Stan', 113: 'Butters'}
#accessing elements from dictionary
print(student_id[113]) #output Butters
print(student_id[111]) #output Erick
#removing elements form dictionary
print("Initial dictionary:", student_id) # output: Initial dictionary: {111: 'Erick', 112: 'Stan', 113: 'Butters'}
del student_id[111]
print("Updated dictionary:", student_id) #output: Updated dictionary: {112: 'Stan', 113: 'Butters'}
#del student_id #this deletes the whole dictionary
#print(student_id) #output : NameError: name 'student_id' is not defined because it has deleted everything
print(len(student_id)) #length of the dictionary is two
#membership test for Dictionary Keys
squares = {1:1, 3:9, 5:25, 7:49, 9:81}
print(1 in squares) #output: True
print(2 not in squares) #output: True
print(49 in squares) #output: False
#iterating through the dictionary
for i in squares: 
    print(squares[i])
    """output
    1
    9
    25
    49
    81
    """
    
