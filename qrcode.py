import qrcode
import random

img = qrcode.make('https://instagram.com/swcris')
print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (330,330)



img.save('code_'+str(random.randint(1000,9999)) + ('.png'))






#instalar biblioteca qrcode = pip install qrcode
#pra instalar no python3 = python3 -m pip install qrcode

#instalar a biblioteca pillow = pip install pillow
# python3 -m pip install pillow
