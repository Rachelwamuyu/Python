#This is a topic on basic operations
print(5+6)

#1 Arithmetic operators
a=7
b=2
#addition
print('Sum:', a+b)
#subtraction
print('Subtraction:', a-b)
#Multiplication
print('Multiplication:', a*b)
#Division
print('Division:', a/b)
#Floor Division
print('Floor Division:', a//b)
#Modulo
print('Modulo:', a%b)
#a to the power of b
print('Power:', a**b)

#2 Assignment operators
#assign 10 to a
a=10
#assign 5 to b
b=5
#assign the sum of a and b to a
a+=b #a=a+b
print(a)

# 3 comparison operators
a=5
b=2
#equal to operator
print('a==b =', a==b)
#not equal to operator
print('a!=b =', a!=b)
#greater than operator
print('a>b =', a>b)
#Less than operator
print('a<b =', a<b)
#greater than or equal to operator
print('a>=b =', a>=b)
#less than or equal to operator
print('a<=b =', a<=b)

#4 logical operators
#AND operator
a = 5
b = 6
print((a > 2) and (b >= 6))

print(True and True) #True
print(True and False) #False

#Logical OR
print(True or False) #True

#Logical NOT
print(not True) #False

#python special operators : identity operators , #membership operators
#identity operators  is and is not

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1) #false
print(x2 is y2) #true
print(x3 is y3) #false

#membership operators in and not in
x = 'Hello world'
y= {1:'a', 2:'b'}
#check if 'H' is present in x string
print('H' in x) #prints true
#check if 'hello' is present in x string
print('hello' not in x) #prints true
#check if '1' key is present in y 
print( 1 in y) #prints true
#check if 'a' key is present in y 
print( 'a' in y) #prints false
