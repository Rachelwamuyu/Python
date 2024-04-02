#type conversion and comments
#declare and initialize two variables
num1 = 6
num2 = 9
#print the output
print('This is output')

#python implicit type conversion
#converting integer to a float
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

#displaying new value and resulting data type
print('value:', new_number)
print('Data Type:',  type(new_number))

#explicit type conversion
num_string ='12'
num_integer = 23
print('Data type of num_string before Type Casting:', type(num_string))

#explicit type conversion

num_string = int(num_string)
print('Data type of num_string after Type Casting:', type(num_string))
num_sum = num_integer + num_string
print('Sum:', num_sum)
print('Data type of num_sum:', type(num_sum))



