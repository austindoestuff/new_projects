#!/usr/bin/python3

old_name = input('Enter your name: ').lower()
new_name = (old_name.replace('o', 'oob').replace('a', 'oob').replace('e', 'oob').replace('i', 'oob').replace('u', 'oob'))
print()
print('"' + new_name + '"')
print('This is your new name!')
print()
print('Would you like to keep it?')
print()
print('Type: "YES" or "NO"')

# ANSWER
answer = input().upper()
y = ['YES', 'SURE', 'YES PLEASE', 'OKAY', 'WHY NOT', 'GO AHEAD', 'Y', 'ABOSOLUTELY', 'OF COURSE']
if answer in y:
    print()
    print('Congratulations, ' + new_name + '!')
    print()
else:
    print()
    print('Too bad...I liked it')
    print()