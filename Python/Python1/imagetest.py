from PIL import Image
import os

path = '/home/austin/Pictures/Pictures/Other Crap'
files = os.listdir(path)

for f in files:
    try:
        with Image.open(r"/home/austin/Pictures/Pictures/Other Crap/" + f) as pic:
            # pic = pic.resize((520, 300))
            pic.show()
            new_name = input('New Name?')
            source_fp=os.path.join(path,f)
            target_fp=os.path.join(path, new_name+'.png')
            os.rename(source_fp, target_fp)
    except NameError:
        pass