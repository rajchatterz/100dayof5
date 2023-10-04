print("Welcome to the pyPassword Generator!")
nr_letters = int(input("How many letteres would you like to use in your password?\n"))
nr_symbol = int(input(f"How many symbols you like to use\n"))
nr_numbers = int(input("How many numbers you like to use?"))
letters = ['a','b','c','d','e','f','A','B','C','D','E']
numbers = ['0','1','2','3','4','5','6','7','8']
symbols = ['!','@','#','$']
password =[]
import random
for char in range(1,nr_letters+1):
    rand_char = random.choice(letters)
    password+=rand_char
for char in range(1,nr_symbol+1):
    rand_char = random.choice(symbols)
    password+=rand_char
for char in range(1,nr_numbers+1):
    rand_char = random.choice(numbers)
    password+=rand_char
    
print(password)
random.shuffle(password)
print(password)
new_pass = ""
for char in password:
    new_pass+=char
    
print(new_pass)


