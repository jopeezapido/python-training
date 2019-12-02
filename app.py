"""
#variables and basic types of data

character_name = "Mike" #this is a string
character_age = "70"
character_age_number = 70.683 #you could store a number, without the quotations
is_Male = True

print ("There was a man named " + character_name + ", ")
print ("he was 70 years old.")
print ("He really liked the name " + character_name + " ,")
print ("but did not like being " + character_age + ".")


#STRINGS

print ("Giraffe\"Academy") #this is a string with a backslash to include quotations as part of the string


phrase = "Giraffe Academy"
print (phrase + " is cool") #value utilizes variable and concatenates it with a string

print ("Giraffe\nAcademy") #\n uses space between words

#String Functions- Could check and modify and value

print (phrase.upper()) #converts Phrase variable string in upper case
print (phrase.lower()) #converts Phrase variable string in lower case
print (phrase.isupper()) #results to a boolean to decide if string is upper case
print (phrase.upper().isupper()) #reads function from left to right. In this case, the result would be true
print (len(phrase)) #length function countes how many characters are there in a string
print (phrase[0]) #Note- when we work with strings, we start with 0. In this case, it would result to "G"
print (phrase.index("A")) #vice-versa of above, this would find the character in the string and returns the index number of that character. Not case-sensitive
print (phrase.replace("Giraffe", "Elephant")) #this would replace the word Giraffe and replaces it with Elephant


#NUMBERS

print(56) #prints number
print(3+4.5) #equation
print(3*(4+5))
print(10 % 3) #returns the remainer

my_num = 5
print(10 + my_num)

#number functions

print(str(my_num) + " is my favorite number") #converts a number contained in variable into a string then concatenates it with an actual string
print(abs(my_num)) #will return an absoulte number of . Absolute function
print(pow(3, 2)) #3 raised to the power of 2 Pow function
print(min(-2, 6)) #will get the lower of the two numbers shown here
print(max(10,-4)) #will get the higher of the two numnbers shown here
print(round(3.7)) #will round of to the nearest number. .5 and above will be rounded of to the next number and vice versa

from math import * #Math module- gets out and grab math functions that are not native to python. 

print(floor(3.7)) #rounds to the lowest number
print(ceil(3.7)) #rounds the number up
print(sqrt(36)) #gets the square root of the number

#GETTING INPUTS FROM USERS


name = input ("Enter your name: ")
age = input ("Enter you age: ")
print("Hi my name is " + name + "!" + "I am " + age + " years old!")
"""

#BUILDING A BASIC CALCULATOR

"""
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

total = num1 + num2 #will result to the combination of the numbers, NOT THE SUM if
#total_whole = int(num1) + int(num2) #will result to 3. Will result to an error if doing operations with non-integers numbers
total_num = float(num1) + float(num2) #will result to a the number itself. No error when doing operations with non-integers

print("Combined number is a " + total)
#print("Will result to " + total_whole) #this must be commented out cause if not, it will stop the parsing of the code
print("Decimals or non-decimal will result to " + str(total_num)) #number must be converted to string first since it cannot be concatenate with a string


#MAD LIBS GAME

leon = input("Leon is a dog and a: ")
motzi = input("Motzi is a dog and a: ")
raven = input("Raven is a dog and a: ")
bunchui = input("Bunchui is a dog and a: ")

print("Leon is also a " + leon)
print("Motzi is also a " + motzi)
print("Raven is also a " + raven)
print("Bunchui is also a " + bunchui)
"""











































    









