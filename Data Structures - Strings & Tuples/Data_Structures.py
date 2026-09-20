#Strings & Tuples
#1. String Concatenation:
""" Write a Python program that takes two strings i.e string 1 “Hello ”, string 2 get name as
input from the user and concatenates them together. Display the concatenated string as
the output."""
string1="Hello "
string2=input("Enter your name: ")
result=string1+string2
print(result)
string3=" , welcome to Python programming"
print(result+string3)
#2. String Slicing and Indexing:
"""Write a Python program using the above concatenated string as input and performs the
following tasks:
a. Print the first character of the string.
b. Print the last character of the string.
c. Print the first 5 characters of the string.
d. Print the last 11 characters of the string.
e. Print the string in reverse.
f. Use slicing and print the word “Python” from the existing string.
"""
input_string = result + string3
first_char = input_string[0]
last_char = input_string[-1]
first_five_chars = input_string[:5]
last_eleven_chars = input_string[-11:]
reversed_string = input_string[::-1]
slice_from_excisting_string = input_string[26:32]  # Slicing to get "Python"

print("First character of the string:", first_char)
print("Last character of the string:", last_char)
print("First 5 characters of the string:", first_five_chars)
print("Last 11 characters of the string:", last_eleven_chars)
print("String in reverse:", reversed_string)
print("Word 'Python' from the existing string:", slice_from_excisting_string)

# 3. String Methods:
"""Write a Python program that takes a string, strM = “Python beginner tutorial” and
perform the following tasks:
a. Convert the sentence to uppercase.
b. Convert the sentence to lowercase.
c. Use Capitalize and return the sentence to the original input form.
d. Count the total number of occurrences of character ‘t’ in the string.
e. Replace all occurrences of “Python” with “Machine Learning” in the input string
strM = “Python beginner tutorial”   """
strM = "Python beginner tutorial"
uppercase_str = strM.upper()
lowercase_str = strM.lower()
capitalized_str = strM.capitalize()
no_of_occurrences= strM.count('t')
replaced_str = strM.replace("Python", "Machine Learning")
print(strM)
print(uppercase_str)
print(lowercase_str)
print(capitalized_str)
print(no_of_occurrences)
print(replaced_str)

# Tuples
"""Create 1st tuple with values -> (10, 20, 30), 2nd tuple with values -> (40, 50, 60):
a. Concatenate the two tuples and store it in “t_combine”
b. Repeat the elements of “t_combine” 3 times
c. Access the 3rd element from “t_combine”
d. Access the first three elements from “t_combine”
e. Access the last three elements from “t_combine”"""
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
t_combine = tuple1 + tuple2
repeated_tuple = t_combine * 3  
access_third_element = t_combine[2]
access_first_three_elements = t_combine[:3] 
access_last_three_elements = t_combine[-3:]
print("Concatenated tuple:", t_combine)
print("Repeated tuple:", repeated_tuple)
print("3rd element from t_combine:", access_third_element)
print("First three elements from t_combine:", access_first_three_elements)
print("Last three elements from t_combine:", access_last_three_elements)
