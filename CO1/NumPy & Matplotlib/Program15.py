# from google.colab import files
# uploaded = files.upload()

import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'img15.jfif'  
image = cv2.imread(image_path)


if image is None:
    print("Error: Unable to load the image.")
else:
    
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    
    roi = image[100:300, 200:400]

    
    plt.subplot(2, 2, 2)
    plt.title('Cropped ROI')
    plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
    plt.axis('off')

   
    new_size = (200, 200)
    resized_image = cv2.resize(image, new_size)

    
    plt.subplot(2, 2, 3)
    plt.title('Resized Image')
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

   
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   
    plt.subplot(2, 2, 4)
    plt.title('Grayscale Image')
    plt.imshow(grayscale_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()