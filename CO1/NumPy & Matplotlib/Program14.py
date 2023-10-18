from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
image = Image.open("image.jpg")
gray_image = image.convert('L')
gray_array = np.array(gray_image)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(np.array(image))
plt.title('Original Image')
plt.axis('off')
plt.subplot(1,2,1)
plt.imshow(gray_array, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Grayscale Image')
plt.axis('off')
plt.show()