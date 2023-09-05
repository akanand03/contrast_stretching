import cv2
import matplotlib.pyplot as plt

# Read the 'lena.jpg' image
image = cv2.imread('lena.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Apply contrast stretching method
    maxiI = 250
    miniI = 3

    maxoI = 155
    minoI = 0

    stretched_image = image.copy()

    # Get height and width of the image
    height, width, _ = image.shape

    for i in range(0, height - 1):
        for j in range(0, width - 1):
            # Get the pixel value
            pixel = stretched_image[i, j]

            # 1st index contains red pixel
            pixel[0] = (pixel[0] - miniI) * ((maxoI - minoI) / (maxiI - miniI)) + minoI

            # 2nd index contains green pixel
            pixel[1] = (pixel[1] - miniI) * ((maxoI - minoI) / (maxiI - miniI)) + minoI

            # 3rd index contains blue pixel
            pixel[2] = (pixel[2] - miniI) * ((maxoI - minoI) / (maxiI - miniI)) + minoI

            # Store new values in the pixel
            stretched_image[i, j] = pixel

    # Display the original and stretched images
    plt.figure(figsize=(12, 6))

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Stretched image
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(stretched_image, cv2.COLOR_BGR2RGB))
    plt.title('Stretched Image')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
