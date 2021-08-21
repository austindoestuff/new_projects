#!/usr/bin/python3
import itertools, time, os, sys
from collections import Counter

file = str(os.path.dirname(os.path.realpath(__file__)))+'/words_alpha.txt'
dictionary = set()

with open(file,'r') as f:
    for line in f.readlines():
        new_line = str(line).replace('\n','')
        dictionary.add(new_line)

def solver(anagram):
        global start_time, output
        output = set()
        if anagram=='q': 
            exit()
        start_time = time.time()
        for word in dictionary:
            if len(word) == len(anagram):
                if Counter(word) == Counter(anagram):
                    output.add(word)

if __name__ == '__main__':
    for args in sys.argv[1:]:
        solver(args)
        if len(output) > 0:
            print('%s \n %s' % (args, output))
        else:
            print('There were no answers for %s' % (args.upper()))
        print('--- %s seconds ---\n' % (time.time() - start_time))