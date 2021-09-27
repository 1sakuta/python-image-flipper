#imort modules
from PIL import Image
import os

#variable to open our image
img = Image.open('./assets/rotateit.png')

#code
r_img = img.rotate(-90)
r_img.save('./assets/rotated.png')
os.remove('./assets/rotateit.png')
r_img.show()

#congratulation
print('Your image was successfully rotated!')
print('Now your new file name is rotated.png')

#click enter button to close programm
input()