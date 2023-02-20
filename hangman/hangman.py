import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives  = 7
    while len(word_letter) > 0 and lives >0:
        

        print("YOu have %d lives left, You have used these lettter : " % lives,' '.join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print("Current  word ",' '.join(word_list))
        user_letter = input("Guess the letter : ").upper()
        

        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter %s is not in the word" % user_letter)
        elif user_letter in used_letter:
            print("YOu have already used this letter")
        else:
            print("YOu have entered an invalid letter")
    if lives == 0:
        print("Your lives are over , the correct word is ",word)
    else:
        print('You have guessed',word,'correctly')

hangman()