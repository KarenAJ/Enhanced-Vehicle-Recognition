import cv2
 
# Read the images
foreground = cv2.imread("blending_pics/surf.jpeg")
background = cv2.imread("blending_pics/building.jpg")
alpha = cv2.imread("blending_pics/galaxy.jpeg")
 
# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)
 
# Normalize the alpha mask to keep intensity between 0 and 1
alpha = alpha.astype(float)/255
 
# Multiply the foreground with the alpha matte
foreground = cv2.multiply(alpha, foreground)
 
# Multiply the background with ( 1 - alpha )
background = cv2.multiply(1.0 - alpha, background)
 
# Add the masked foreground and background.
outImage = cv2.add(foreground, background)
 
# Display image
cv2.imshow("foreground", foreground/255)
cv2.imshow("background", background/255)
cv2.imshow("alpha", alpha/255)
cv2.imshow("outImg", outImage/255)
cv2.waitKey(0)

