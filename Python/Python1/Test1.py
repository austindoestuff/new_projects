import os


def write_to_file(filepath, content):
    f = open(filepath, "w")
    f.write(content)
    f.close()

# write_to_file(filepath="/home/austin/Documents/Test-Data/1.txt",content="hi")

path ="/home/austin/Documents/Test-Data/"
files = os.listdir(path)
# all_files = files

for file in files:
    # print(file)
    write_to_file(filepath=os.path.join(path,file),content=file.replace('.txt',''))