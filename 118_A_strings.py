# vowels : A E I O U Y
'''
A. String Task
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

    deletes all the vowels,
    inserts a character "." before each consonant,
    replaces all uppercase consonants with corresponding lowercase ones. 

Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

Help Petya cope with this easy task.
Input

The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.
Output

Print the resulting string. It is guaranteed that this string is not empty
'''
vowels = ['A','E','I','O','U','Y','a','e','i','o','u','y']

def remove_vowels(word) :
    word_no_vowels = []
    for letter in word :
        if letter not in vowels :
            word_no_vowels.append(letter)
            
    
    return word_no_vowels

def list_to_string(word_list) :
    required_word = ''
    for letter in word_list :
        required_word = required_word + letter
    
    return required_word

def string_to_list(word) :
    required_string = []
    for letter in word :
        required_string.append(letter)
    
    return required_string

input_word = input().lower()

word_list = string_to_list(input_word)
word_no_vowel = remove_vowels(word_list)

final_list = []

for letter in word_no_vowel :
    final_list.append(f".{letter}")




print(list_to_string(final_list))




