import string
import random
alphabet =  string.ascii_letters + string.punctuation
uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
special_character = list(string.punctuation)

def password_generator():
    
    password = []
    for letter in range(6):
        letter = random.choice(lowercase)
        password.append(letter)
    password.append(random.choice(uppercase))
    password.append(random.choice(special_character))
    random.shuffle(password)
        
    print(''.join(password))
password_generator()

def password_checker(password):
    if len(password) != 9:
         return False
    has_upper = False
    has_special = False
    for char in password:
        if char in special_character:
            has_special = True
        elif char.isupper():
            has_upper = True
    return has_special and has_upper

password = 'suckmeaE@'

if password_checker(password):
    print('valid password')
else:
    print("invalid password")
            



   
