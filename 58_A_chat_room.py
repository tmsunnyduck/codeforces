'''
A. Chat room
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.
Input

The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.
Output

If Vasya managed to say hello, print "YES", otherwise print "NO".
'''
def string_to_list(word) :
    required_string = []
    for letter in word :
        required_string.append(letter)
    
    return required_string

def list_to_string(word_list) :
    required_word = ''
    for letter in word_list :
        required_word = required_word + letter
    
    return required_word

s = input()
hello = ['h','e','l','o']

ideal = '12334'

found_h = 0
found_e = 0
found_l = 0
found_o = 0

word = ''

for index in range(len(s)) :
    if s[index] == 'h' and found_h != 1:
        word = word + '1'
        found_h = found_h + 1
    
    if s[index] == 'e' and found_e != 1 :
        word = word + '2'
        found_e = found_e + 1

    if s[index] == 'l' and found_l != 2 :
        word = word + '3'
        found_l = found_l + 1
    
    if s[index] == 'o' and found_o != 1 :
        word = word + '4'
        found_o = found_o + 1

if word == ideal :
    print('YES')
else :
    print('NO')