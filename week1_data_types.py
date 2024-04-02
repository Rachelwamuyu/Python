#python numeric data types - int, float, complex
num1 = 5
print(num1, 'is of type', type(num1))
num2 = 2.0
print(num2, 'is of type', type(num2))
num3 = 1+2j
print(num3, 'is of type', type(num3))

#example of  python list data type
languages=['swift', 'Java', 'Python']
# access element at index 0
print(languages[0]) #swift

# access element at index 2
print(languages[2]) #Python

#create a tuple
product = ('Microsoft', 'Xbox', 499.99)
# access element at index 0
print(product[0]) #Microsoft

# access element at index 1
print(product[1]) #Microsoft

#string data types
name = 'Python'
print(name)
message = 'Python for beginners'
print(message)

#creates a set named student_id. You cannot call an item in a set by using the index, you just have to call the entire set
student_id = {112, 114, 116, 118, 115}
#display student_id elements
print(student_id)
#display type of student_id
print(type(student_id))

#dictionary data type
#creates a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', "Italy": 'Rome', 'England': 'London'}
print(capital_city)

print(capital_city['Nepal']) #prints Kathmandu
print(capital_city['Kathmandu']) #throws away error