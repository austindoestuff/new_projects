#!/usr/bin/python3
old_name = input('Enter your name: ').lower()
print('What letter would you like to replace? ')
print('or...all vowels, consonants, maybe everything?')
replaced = input().lower()
new_string=[]
print('With what? ')
replacement = input()
vowels = ['vowels', 'a, e, i, o, u', 'a, e, i, o, and u', 'aeiou', 'vowel']
consonants = ['consonants', 'constants', 'consinants', 'consenants', 'consanents', 'consonents', 'consonant']
everything = ['everything', 'everythin', 'yes', 'ye']

#vowels
if replaced in vowels:
    for x in old_name:
        
        if x in (['a','e', 'i', 'o', 'u']):
            new_name = x.replace(x,replacement)
            new_string.append(new_name)
        else:
            new_string.append(x)
    new_name = "".join(new_string)
else:
    new_name = old_name.replace(replaced,replacement)
#consonants
if replaced in consonants:
    for x in old_name:
        if not x in ([' ', 'a','e', 'i', 'o', 'u']):
            new_name = x.replace(x,replacement)
            new_string.append(new_name)
        else:
            new_string.append(x)
    new_name = "".join(new_string)
else:
    new_name = old_name.replace(replaced,replacement)
#everything
if replaced in everything:
    for x in old_name:
        if not x in ([' ']):
            new_name = x.replace(x,replacement)
            new_string.append(new_name)
        else:
            new_string.append(x)
    new_name = "".join(new_string)
else:
    new_name = old_name.replace(replaced,replacement)
print()
print(new_name)
print('This is your new name!')
print()
print('Would you like to keep it?')
print()
print('Type: "YES" or "NO"')

# ANSWER
answer = input().upper()
y = ['YES', 'SURE', 'YES PLEASE', 'OKAY', 'WHY NOT', 'GO AHEAD', 'Y', 'ABOSOLUTELY', 'OF COURSE', 'YOU BET', 'YOU BET!', 'YE']
if answer in y:
    print()
    print('Congratulations, ' + new_name + '!')
    print()
else:
    print()
    print('Too bad...I liked it')
    print()