import random
import string

def generate_password (length, letters, numbers, symbols):
    charr =''
    if letters=='y':
        charr += string.ascii_letters
        
    if numbers=='y':
        charr += string.digits
        
    if symbols=='y':
        charr += string.punctuation
       
    print("password is",''.join(random.choice(charr) for i in range(length)))

length = int(input("Enter password length: "))
        
while length <= 0:
    length = int(input("Again Enter password length: "))

letters = input("Include letters (y/n): ").lower()
numbers = input("Include numbers (y/n): ").lower()
symbols = input("Include symbols (y/n): ").lower() 


generate_password(length, letters, numbers, symbols)
