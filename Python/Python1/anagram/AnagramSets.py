#!/usr/bin/python3
import itertools, time, os

file = str(os.path.dirname(os.path.realpath(__file__)))+'/words_alpha.txt'
dictionary = set()

with open(file,'r') as f:
    for line in f.readlines():
        new_line = str(line).replace('\n','')
        dictionary.add(new_line)

while True:        
    anagram = input('What Is The Word?\n')
    if anagram=='q': 
        break
    output = set()
    start_time = time.time()
    if len(anagram) > 13:
        print("Too Long. It'll take forever to do.")
    else:
        for x in itertools.permutations(anagram.lower()):
            y = ''.join(x)
            # if y in dictionary:
            #     output.add(y)
            #     continue
            # else:
            #     continue
            output.add(y)
        if len(output) > 0:
            print(output)
        else:
            print('There were no answers')
    print('--- %s seconds ---' % (time.time() - start_time))