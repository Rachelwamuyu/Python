#Write a program that accepts user input to create a list of integers. 
#Then, compute the sum of all the integers in the list.

    # Accept user input to create a list of integers
def main():
    input_str = input("Enter integers separated by spaces: ")
    integers = [int(x) for x in input_str.split()]

    # Compute the sum of all the integers in the list
    total_sum = sum(integers)

    # Display the result
    print("The sum of the integers is:", total_sum)

if __name__ == "__main__":
    main()

#Create a tuple containing the names of five of your favorite books. 
#Then, use a for loop to print each book name on a separate line.
books = ("The Bible","Adventures of Tintin", "Gifted Hands", "Purpose Driven Life", "The Daily bread")
for favourite in books:
    print(favourite)

#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
#Ask the user for input and store the information in the dictionary. 
#Then, print the dictionary to the console.
def main():
    # Create an empty dictionary to store person's information
    person_info = {}

    # Ask user for input
    name = input("Enter person's name: ")
    age = input("Enter person's age: ")
    favorite_color = input("Enter person's favorite color: ")

    # Store information in the dictionary
    person_info['Name'] = name
    person_info['Age'] = age
    person_info['Favorite Color'] = favorite_color

    # Print the dictionary to the console
    print("Person's Information:")
    for key, value in person_info.items():
        print(key + ':', value)

if __name__ == "__main__":
    main()

#Write a program that accepts user input to create two sets of integers. 
#Then, create a new set that contains only the elements that are common to both sets.

def main():
    # Accept user input to create the first set of integers
    input_str1 = input("Enter integers separated by spaces for the first set: ")
    set1 = set(map(int, input_str1.split()))

    # Accept user input to create the second set of integers
    input_str2 = input("Enter integers separated by spaces for the second set: ")
    set2 = set(map(int, input_str2.split()))

    # Create a new set containing only the elements that are common to both sets
    common_elements = set1.intersection(set2)

    # Print the new set
    print("Common elements in both sets:", common_elements)

if __name__ == "__main__":
    main()

#Create a program that stores a list of words. 
#Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

def main():
    # Store a list of words
    word_list = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "blueberry"]

    # Use list comprehension to create a new list containing words with odd number of characters
    odd_length_words = [word for word in word_list if len(word) % 2 != 0]

    # Print the new list
    print("Words with odd number of characters:", odd_length_words)

if __name__ == "__main__":
    main()
