# Import libraries
import cv2

# Load Image
img = cv2.imread('Images/image_example1.jpg')

# Show image shape
print(f'Image shape: {img.shape}')

# Show info about specific pixel
print(f'Image info for pixel 100,20: {img[20, 100]}')

# Information about RGB in OpenCV are inverted
# So, img[y, x][0] = Blue; img[y, x][1] = Green; img[y, x][2] = Red;
print(f'Image Blue = {img[20, 100][0]}')
print(f'Image Green = {img[20, 100][1]}')
print(f'Image Red = {img[20, 100][2]}')

# Create a img copy to plot boxes inside image
img2 = img.copy()

# Put a rectangle in image
cv2.rectangle(img2,
              (560, 250),
              (660, 350),
              (0, 200, 0),
              3)

# Put text in a image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img2, 'Tree', (560, 380), font, 1, (0, 200, 0), 3)
cv2.imshow('Img', img2)
cv2.waitKey()
