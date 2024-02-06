import matplotlib.pyplot as plt
from PIL import Image
import glob
import json

imageFiles=open('F:/450 project/Project/backend/imageName.json')
img_arr=json.load(imageFiles)
location='F:/450 project/Project/backend/'
images = []
for f in img_arr:
    images.append(Image.open(location+f))

print(len(images))

print(images[313])
plt.imshow(images[313], cmap='gray')
plt.show()