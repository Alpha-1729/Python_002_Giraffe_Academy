#!/usr/bin/python3
# Building A Translator

"""
>>>> In this we are replacing all the letter in a string with g/G if the letter is a vowel.
>>>>
>>>>
>>>>
>>>>
"""

def translate(phrase):
    translate = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translate = translate + "G"
            else:
                translate = translate + "g"
        else:
            translate = translate + letter
    return translate

print(translate(input("Enter the phrase: ")))
