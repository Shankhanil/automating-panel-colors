import cv2
img = cv2.imread('T-Shirt_UVMaps_Naming convention.png', 0) 
cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU,img)

contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    # draw a white rectangle to visualize the bounding rect
    cv2.rectangle(img, (x, y), (x + h, y + w), 255, 1)

cv2.drawContours(img, contours, -1, (128, 128, 0), 1)

cv2.imwrite("output.png",img)