import os

path = '/home/austin/Documents/Test-Data'

files = os.listdir(path)

for f in files:
    print(f)

for file in files:
    source_fp=os.path.join(path,file)
    #print('old fp:', source_fp)

    target_fp=os.path.join(path,"new_"+file)
    #print('target:',target_fp)
    # os.rename(file, os.path.join(path,file))

    os.rename(source_fp, target_fp)

files = os.listdir(path)

for f in files:
    print(f)

for file in files:
    source_fp=os.path.join(path,file)
    #print('old fp:', source_fp)

    target_fp=os.path.join(path,file.replace('new_',''))
    #print('target:',target_fp)
    # os.rename(file, os.path.join(path,file))

    os.rename(source_fp, target_fp)

files = os.listdir(path)

for f in files:
    print(f)