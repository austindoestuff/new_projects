#!/usr/bin/python3
old_name = input('Enter your name: ').lower()
replaced = input('What letter would you like to replace?\nor...all vowels, consonants, maybe everything?\n').lower()
replacement = input('With what?\n')
#
vowels = ['vowels', 'a, e, i, o, u', 'a, e, i, o, and u', 'aeiou', 'vowel']
consonants = ['consonants', 'constants', 'consinants', 'consenants', 'consanents', 'consonents', 'consonant']
everything = ['everything', 'everythin', 'yes', 'ye']
new_string = []
#
def translate1(vowel_letters):
    for x in old_name:
        if x in vowel_letters:
            new_name = x.replace(x,replacement)
            new_string.append(new_name)
        else:
            new_string.append(x)
def translate2(other_options):
    for x in old_name:
        if not x in other_options:
            new_name = x.replace(x,replacement)
            new_string.append(new_name)
        else:
            new_string.append(x)

#vowels
if replaced in vowels:
    v_replacement = ['a','e', 'i', 'o', 'u']
    translate1(v_replacement)
    new_name = "".join(new_string)
#consonants
elif replaced in consonants:
    other_options = [' ', 'a', 'e', 'i', 'o', 'u']
    translate2(other_options)
    new_name = "".join(new_string)
#everything
elif replaced in everything:
    other_options = ([' '])
    translate2(other_options)
    new_name = "".join(new_string)
else:
    new_name = old_name.replace(replaced,replacement)
print('\n' + new_name)
print('\nThis is your new name!')
print('\nWould you like to keep it?')
print('Type: "YES" or "NO"')

# ANSWER
answer = input().upper()
y = ['YES', 'SURE', 'YES PLEASE', 'OKAY', 'WHY NOT', 'GO AHEAD', 'Y', 'ABOSOLUTELY', 'OF COURSE', 'YOU BET', 'YOU BET!', 'YE']
if answer in y:
    print('\nCongratulations, ' + new_name + '!\n')
else:
    print('\nToo bad...I liked it\n')