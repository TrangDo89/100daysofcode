import random
#this code is reference from 100 day of code
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Welcome to the Password Generator!")

num_number = int(input("Please enter the number of numbers in password: "))
print()
num_symbol = int(input("Please enter the number of symbol in password: "))
print()
num_letter= int(input("Please enter the number of letter in password: "))
print()

# this code is my work
result = ""
for i in range(num_letter):
    random_letter = random.randint(0, len(letter) - 1)
    result += letter[random_letter]

for i in range(num_symbol):
    random_symbol = random.randint(0, len(symbol) - 1)
    result += symbol[random_symbol]

for i in range(num_number):
    random_int = random.randint(0, len(number) - 1)
    result += number[random_int]

print(result)
