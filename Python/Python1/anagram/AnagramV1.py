import itertools, time, os

file = str(os.path.dirname(os.path.realpath(__file__)))+'/words_alpha.txt'
dictionary = []
with open(file,'r') as f:
    for line in f.readlines():
        new_line = str(line).replace('\n','')
        dictionary.append(new_line)

while True:        
    anagram = input('What Is The Word?\n')
    if anagram=='q': 
        break
    possibilities = []    
    output = []
    min_index = 0
    start_time = time.time()
    if len(anagram) > 10:
        print("Too Long. It'll take forever to do.")
    else:
        for x in itertools.permutations(anagram):
            y = ''.join(x)
            if not y in possibilities:
                possibilities.append(y)
                listy = sorted(possibilities)
        for i in listy:
            if i in dictionary:
                if dictionary.index(i) <= min_index:
                    continue
                else:
                    output.append(i)
                    min_index = dictionary.index(i)
            else:
                continue
        print(output)
        print('--- %s seconds ---' % (time.time() - start_time))
