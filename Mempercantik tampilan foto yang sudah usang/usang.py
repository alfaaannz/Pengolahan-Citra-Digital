import imageio
from skimage import exposure, color, filters
import matplotlib.pyplot as plt

image = imageio.imread('usang.jpg')

grayscale_image = color.rgb2gray(image)

enhanced_image = exposure.adjust_gamma(grayscale_image, gamma=0.5)
enhanced_image = exposure.rescale_intensity(enhanced_image, in_range='image', out_range=(0, 1))

denoised_image = filters.median(enhanced_image)

equ_image = exposure.equalize_hist(denoised_image)

sharpened_image = exposure.rescale_intensity(denoised_image - 1 * filters.laplace(denoised_image))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].imshow(image)
axes[0].set_title('Original Image')

axes[1].imshow(sharpened_image, cmap='cubehelix') # Mengatur filter menggunakan cmap
axes[1].set_title('Processed Image')

plt.show()
