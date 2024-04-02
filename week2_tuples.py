var1 = ("hello") #type function to know which class a variable/ value belongs to
print(type(var1)) #output <class 'str'>
var2 = ("hello",) #creating a tuple with one element
print(type(var2)) #output <class 'tuple'>
var3 = "hello", #not using parenthesis
print(type(var3)) #output <class 'tuple'>
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")#accessing tuple elements using indexing
print(letters[0]) #output p
print(letters[5]) #output a
print(letters[-1]) #output z
print(letters[-3]) #output m
my_tuple = ("a", "p", "p", "l", "e")
print(my_tuple.count("p")) #output 2
print(my_tuple.index("l")) #output 3
