from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')
# print(img.size)
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
# resize = crooked.resize((300, 300))

# crop the image
'''
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('blur.png', 'png')
'''

'''
# astro resizing/converting to thumbnail
img = Image.open('astro.jpg')

# thumbnail() better than resize()
img.thumbnail((400,400))
img.save('thumbnail.jpg')

'''