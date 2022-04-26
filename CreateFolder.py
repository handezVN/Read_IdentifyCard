# Python program to explain os.mkdir() method

# importing os module
import cv2

img = cv2.imread("3.jpg");

print(type(img))
print(img.shape)

vungchon = img[1045:1170,1100:1900];
cv2.imshow("Chon",vungchon)
cv2.waitKey();