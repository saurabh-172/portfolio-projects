import os
import sys
from PIL import Image


images, new_dir = sys.argv[1], sys.argv[2]
# print(os.getcwd())
# print(os.path.isdir(new_dir))


# the basename of the file
# img = Image.open(f'./{images}/pikachu.jpg')
# print(os.path.basename(img.filename))

# print(os.path.abspath(f'{images}')) # get absolute path to mentioned path/dir/file
# print(os.open('./Pokedex', os.O_RDONLY))
# gives list of dir/files in respective mentioned path/dir

# if not os.path.isdir(new_dir):
if not os.path.exists(new_dir):
    os.mkdir(f'{new_dir}')

# imgs = []
with os.scandir(f'{images}') as img_fs:
    for f in img_fs:
        # if f.is_file:
        #     print(f.name)
        img = Image.open(f'{f.path}')
        # imgs.append(imgv)
        # img.save(f"{new_dir}{os.path.basename(img.filename).split('.')[0]}.png", 'png')
        cleanname = os.path.splitext(f.name)[0]
        # print(cleanname, f.name)
        img.save(f"{new_dir}{cleanname}.png", 'png')

# for img in imgs:
#     img.save(f"./{new_dir}/{os.path.basename(img.filename).split('.')[0]}.png", 'png')