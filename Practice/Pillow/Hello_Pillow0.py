from PIL import Image, ImageFilter
import matplotlib.pyplot as plt



im = Image.open("Practice\\Pillow\\A_0604_8.jpg")
print(im.format, im.size, im.mode)

out = im.resize((28, 28), Image.ANTIALIAS)
im_gray = out.convert('L')

plt.imshow(im_gray, cmap='gray')
plt.show()
