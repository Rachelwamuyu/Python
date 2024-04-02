str = "Hello world"
print (str) #output Hello world
print (str[0])#prints the first character of the string. Output H
print (str[2:5])#output llo
print (str[2:])#output llo world
print (str * 2) # prints the string two times. Output : Hello worldHello world
print (str + "Test") #prints concateneted (joined) string. Output : Hello worldTest
message = "Hola Amigos"
#message[0] = "H" #strings are immutable. Characters cannot be changed
print (message) 
                #output: #Traceback (most recent call last):
                #File "c:\Users\Wamz\Documents\python\week2_tuples.py", line 16, in <module>
                #3 message[0] = "H"
                #~~~~~~~^^^
                #TypeError: 'str' object does not support item assignment
message = "Hello friends"
print (message) # output Hello friends
message = """" 
Never gonna give up
never gonna let you down
"""
print (message)#prints multiline string 
#Never gonna give up
#never gonna let you down
str1 = "Hello, world!"
str2 = "I love Python"
str3 = "Hello, world!"
#comparing strings
print(str1 == str2)#output False
print(str1 == str3) #output True
greet = "Hello,"
name = "John"
result = greet + name #joining two strings / concatenation
print(result)# output  Hello,John
greet = "Hello"
for letter in greet: #iterating through a string
    print (letter)
greet = "Hello"
print(len(greet))# to find the length of a string. Output: 5
#testing if a substring exist within a string
print("a" in "program")# output true
print ("at" not in "battle")#output false
#escape sequence in python
#example = "He said, "what's there?"" #SyntaxError: unterminated string literal (detected at line 44)
#print (example) 
example = "He said, \"what's there?\"" #to avoid erro when using double quotes, use the escape character \
print (example) #output : He said, "what's there?"
name ="Rachel" #string formatting (f strings)
country = "Kenya"
print (f"{name} is from {country}") #output: Rachel is from Kenya
